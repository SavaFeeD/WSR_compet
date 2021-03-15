import pickle
import numpy as np
import sklearn
import pandas as pd

def setup(filename):
    with open(filename, 'rb') as f:
        model = pickle.load(f)
    return model


def start():
    print('Привет друг, тебя приветсвует гомо-бот!')
    flag = True
    while flag:
        name = input('Введи имя: ')
        if name != '':
            flag = False
            view_info()
        else:
            flag = True


# вывод информации о боте
def view_info():
    print('что-то')
    command = input('>>> ')
    handler(command)


# проверка на ввод команд
def handler(command):
    if command == '0':
        skills()


def skills():
    print('Введите свои умения (q - чтобы закончить):')
    flag = False
    list_skills = []

    text = input()
    if text != 'q':
        text = text.split('-')
        list_skills.append({
            'name': text[0],
            'rate': round(float(text[1]))
        })
        flag = True

    while flag:
        text = input()
        if text == 'q':
            flag = False
        else:
            text = text.split('-')
            list_skills.append({
                'name': text[0],
                'rate': round(float(text[1]))
            })

    print('что-то')
    preprocessing(list_skills)


def preprocessing(list_skills):
    vectorizer('text')
    pass


def vectorizer(text):
    vocab = setup('data/vocab.sav')
    tfidf = sklearn.feature_extraction.text.TfidfVectorizer(vocabulary=vocab)
    vector = tfidf.fit_transform(text)
    predict(vector)


def predict(vector):
    model = setup('data/model_compet_classification.sav')
    cluster = model.predict(vector)[0]

    clusters_list = setup('data/clusters.sav')
    print(clusters_list[clusters_list['cluster'] == cluster]['titles'])


