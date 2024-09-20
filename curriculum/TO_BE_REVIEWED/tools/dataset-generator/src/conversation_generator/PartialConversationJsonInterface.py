import json
from random import choice
from tqdm import tqdm

from conversation_generator.flow import flow, generateRandomString


def generate_dataset(size):
    data = {}
    data['version'] = '0.1'

    paragraphs = []
    f = flow()
    for _ in tqdm(range(size)):
        dialogue, intent, vals = f.create_dialogue()
        dialogue, intent, vals = crack_conversation(dialogue, intent, vals)
        # if vals[0][1] == 'CANNOTANSWER':
        #     print("All values removed, restarting loop")
        #     i -= 1
        #     continue
        paragraph = {'context': dialogue}
        qas_list = []
        for q in vals:
            qas = {
                'id': generateRandomString(32),
                'question': q[0][0]
            }
            if q[1] == True: # isImpossible
                qas['answers'] = []
                qas['is_impossible'] = True
            else:
                ans = {"answer_start": dialogue.find(q[0][1]), "text": q[0][1]}
                qas['answers'] = [ans]
                qas['is_impossible'] = False
            qas_list.append(qas)
        paragraph['qas'] = qas_list

        paragraphs.append(paragraph)
        # print(i)

    data['data'] = [{}]
    data['data'][0]['paragraphs'] = paragraphs
    json_data = json.dumps(data)
    with open('squad_like_data_{0}.json'.format(size), 'w') as outfile:
        json.dump(json.JSONDecoder().decode(json_data), outfile)

    return json_data


def crack_conversation(dialogue, intent, vals):
    dialogue = dialogue.replace("\n", " ")
    s = dialogue.split(" ")
    random_stop = choice(range(0, len(s)))
    sub_dialoge = " ".join(s[0:random_stop])
    sub_dialoge = sub_dialoge.strip()
    sub_vals = []
    for item in vals:
        if item[0] in sub_dialoge and item[1] in sub_dialoge:
            # tuple with the original key: value pair along with a boolean isImpossible
            sub_vals.append((item, False))
        else:
            newItem = item.copy()
            newItem[1] = ''
            sub_vals.append((newItem,True))
    # sub_vals = [x for x in vals if x[1] in sub_dialoge and x[0] in sub_dialoge]
    # print(dialogue)
    # print(sub_dialoge)
    # print(vals)
    # print(sub_vals)
    return sub_dialoge, intent, sub_vals


generate_dataset(5000)


