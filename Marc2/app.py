from flask import Flask
from flask import render_template
from flask import request


app = Flask(__name__)


@app.route('/index/<title>')
def main(title):
    return render_template('base.html', title=title)


@app.route('/training/<profession>')
def training(profession):
    data = {
        "prof": profession
    }
    return render_template('profession.html', data=data)


if __name__ == "__main__":
    app.run(port=8080, host='127.0.0.1')