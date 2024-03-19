'''Создать страницу, на которой будет форма для ввода числа
и кнопка "Отправить"
При нажатии на кнопку будет произведено
перенаправление на страницу с результатом, где будет
выведено введенное число и его квадрат.
'''

from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        number = float(request.form.get('num'))
        data = {'number': number, 'squer': number**2}
        return render_template('task4_1.html', data=data)
    return render_template('task4.html')






if __name__ == '__main__':
    app.run(debug=True)