import json

from conversation_generator.flow import flow


def generate_dataset(size):
    data = {'version': '0.1'}
    f = flow()
    paragraphs = []
    for i in range(size):
        dialogue, intent, vals = f.create_dialogue()
        paragraph = {'context': dialogue}
        qas_list = []
        for q in vals:
            qas = {'question': q[0]}
            ans = {"answer_start": dialogue.find(q[1]), "text": q[1]}
            qas['answers'] = [ans]
            qas_list.append(qas)
        paragraph['qas'] = qas_list

        paragraphs.append(paragraph)

    data['data'] = [{}]
    data['data'][0]['paragraphs'] = paragraphs
    json_data = json.dumps(data)
    with open('data' + str(size) + '.json', 'w') as outfile:
        json.dump(json.JSONDecoder().decode(json_data), outfile)

    print(json_data)
    return json_data


generate_dataset(10 ** 5)
