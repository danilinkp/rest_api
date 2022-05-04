import json
import os
import random
from pprint import pprint

from requests import get

from data import db_session, users_api
from flask import Flask, url_for, request, render_template, Blueprint, make_response, jsonify
from werkzeug.utils import redirect
from data.jobs import Jobs
from data.users import User

app = Flask(__name__)

app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


@app.route('/')
@app.route('/index')
def load_photo():
    return redirect('/member')


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)


@app.route('/member', methods=['POST', 'GET'])
def form_sample():
    if request.method == 'GET':
        with open('templates/information.json') as j_file:
            f = j_file.read()
            data = json.loads(f)
            pprint(data)
            number = random.choice([str(i) for i in range(1, len(data) + 1)])
            dict_for_html = data[number]
            return render_template('load_photo.html', information=dict_for_html)


def user_add():
    db_sess = db_session.create_session()
    user = User()
    user.surname = "1"
    user.name = "12"
    user.age = 231
    user.position = "1"
    user.speciality = "res132earch engineer"
    user.address = "132"
    user.email = "123@mars.org"
    user.city = "Москва"




    db_sess.add(user)


    db_sess.commit()


@app.route('/users_show/<int:user_id>', methods=['POST', 'GET'])
def show(user_id):
    try:
        path = os.path.join(f'{os.getcwd()}/static')

        os.remove(path + '/' + 'map.png')
    except Exception:
        pass

    city = get(f'http://localhost:8085/api/city/{user_id}').json()
    information = {
        'city': city['city'],
        'name': city['name'],
        'image': '../static/map.png'
    }

    geocoder_request = f"http://geocode-maps.yandex.ru/1.x/?apikey=40d1649f-0493-4b70-98ba-98533de7710b&geocode={information['city']}&format=json"
    response = get(geocoder_request)
    json_response = response.json()
    toponym = json_response["response"]["GeoObjectCollection"]["featureMember"][0]["GeoObject"]
    first = list(map(float, toponym['Point']['pos'].split()))
    map_request = f"http://static-maps.yandex.ru/1.x/?ll={first[0]},{first[1]}&spn=0.02,0.02&l=sat"
    response = get(map_request)


    map_file = "static/map.png"
    with open(map_file, "wb") as file:
        file.write(response.content)
    return render_template('users_show.html', information=information)


if __name__ == '__main__':
    db_session.global_init("db/blogs.db")
    app.register_blueprint(users_api.blueprint)
    app.run(port=8085, host='127.0.0.1')
