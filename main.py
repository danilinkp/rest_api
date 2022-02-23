from flask import Flask, render_template

app = Flask(__name__)
image = None


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


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
