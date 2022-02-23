from flask import Flask,  render_template

app = Flask(__name__)
image = None


@app.route('/training/<prof>')
def index(prof):
    return render_template('base.html', title=prof)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
