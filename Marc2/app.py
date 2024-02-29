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


if __name__ == "__main__":
    app.run(port=8080, host='127.0.0.1')