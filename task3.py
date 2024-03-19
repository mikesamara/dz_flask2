'''
Создать страницу, на которой будет форма для ввода имени
и возраста пользователя и кнопка "Отправить"
При нажатии на кнопку будет произведена проверка
возраста и переход на страницу с результатом или на
страницу с ошибкой в случае некорректного возраста.

'''
from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form.get('username')
        age = int(request.form.get('age'))
        if age >= 16:
            return render_template('task3(good).html', name=name, age=age)
        return render_template('task3(error).html', name=name, age=age)
    return render_template('task3.html')








if __name__ == '__main__':
    app.run(debug=True)