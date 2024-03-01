from flask import Flask
from flask import render_template
from flask import request, redirect
import json
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired


app = Flask(__name__)

app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


@app.route('/index/<title>')
def main(title):
    return render_template('base.html', title=title)


@app.route('/training/<profession>')
def training(profession):
    data = {
        "prof": profession
    }
    return render_template('profession.html', data=data)


@app.route('/list_prof/<list>')
def list_prof(list: str):
    data = {
        "list": list,
        "professions": [
            "инженер-исследователь",
            "пилот",
            "строитель",
            "экзобиолог",
            "врач",
            "инженер по терроформированию",
            "климатолог",
            "специалист по радиационной защите",
            "астрогеолог",
            "гляциолог",
            "инженер жизнеобеспечения",
            "метеоролог",
            "оператор марсохода",
            "киберинженер",
            "штурман",
            "пилот дронов"
        ]
    }
    return render_template('profs.html', data=data)


@app.route('/answer')
@app.route('/auto_answer')
def answer():
    data = {
        'title': "Анкета",
        'surname': "Watny",
        "name": "Mark",
        "education": "выше среднего",
        "profession": "штурман марсохода",
        "sex": "male",
        "motivation": "Всегда мечтал застрять на Марс!",
        "ready": "True"
    }
    return render_template('auto_answer.html', data=data)


@app.route('/distribution')
def distribution():
    data = {
        "title": "Размещение",
        "peoples": [
            'Ридли Скотт',
            'Энди Уир',
            'Марк Уотни',
            'Венката Капур',
            'Тедди Сандерс',
            'Шон Бин',
        ]
    }
    return render_template('distribution.html', data=data)


@app.route("/member")
def member():
    with open('templates/members.json', "rt", encoding="utf8") as f:
        members = json.loads(f.read())
    data = {
        "members": members
    }
    return render_template('member.html', data=data)


@app.route('/table/<male>/<int:age>')
def table(male, age):
    data = {
        "male": male,
        "age": age
    }
    return render_template('table.html', data=data)


class LoginForm(FlaskForm):
    your_id = StringField('id астронавта', validators=[DataRequired()])
    your_pwd = PasswordField('Пароль астронавта', validators=[DataRequired()])
    kap_id = StringField('id капитана', validators=[DataRequired()])
    kap_pwd = PasswordField('Пароль капитана', validators=[DataRequired()])
    submit = SubmitField('Доступ')


@app.route('/login')
def login():
    data = {
        "title": "Аварийный доступ"
    }
    form = LoginForm()
    if form.validate_on_submit():
        return redirect('/success')
    return render_template('login.html', data=data, title='Авторизация', form=form)


images = ["img/marc1.png",
          "img/marc2.png",
          "img/marc3.png"]

@app.route('/galery', methods=['POST', 'GET'])
def galery():
    data = {
        "title": "Красная планета",
        "images": images
    }
    if request.method == 'POST':
        f = request.files['file']
        f.save(f"static/img/{f.filename}")
        images.append(f"img/{f.filename}")
    return render_template('galery.html', data=data)


if __name__ == "__main__":
    app.run(port=8080, host='127.0.0.1')