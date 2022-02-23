from flask import Flask, render_template

app = Flask(__name__)
image = None
information = {'title': 'Анкета',
               'surname': 'Wathy',
               'name': 'Mark',
               'education': 'выше среднего',
               'profession': 'штурман марсохода',
               'sex': 'male',
               'motivation': 'Всегда мечтал застрять на Марсе',
               'ready': 'True'

               }


@app.route('/training/<prof>')
def index(prof):
    return render_template('base.html', title=prof)


@app.route('/list_prof/<list>')
def list_prof(list):
    profes = ["инженер-исследователь", "пилот", "строитель", "экзобиолог", "врач",
              "инженер по терраформированию",
              "климатолог", "специалист по радиационной защите", "астрогеолог", "гляциолог",
              "инженер жизнеобеспечения", " метеоролог", "оператор марсохода", "киберинженер", "штурман",
              "пилот дронов"]
    return render_template('base2.html', form=list, profs=profes)


@app.route('/answer/<title>/<surname>/<name>/<education>/<profession>/<sex>/<motivation>/<ready>')
def answer(title, surname, name, education, profession, sex, motivation, ready):
    global information
    information['title'] = title
    information['surname'] = surname
    information['name'] = name
    information['education'] = education
    information['profession'] = profession
    information['sex'] = sex
    information['motivation'] = motivation
    information['ready'] = ready



    return render_template('base.html', title='just')

@app.route('/auto_answer')
def auto_answer():

    return render_template('auto_answer.html', info=information)



if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
