'''Создать страницу, на которой будет форма для ввода имени
и кнопка "Отправить"
При нажатии на кнопку будет произведено
перенаправление на страницу с flash сообщением, где будет
выведено "Привет, {имя}!".'''

from flask import Flask, render_template, request, flash, redirect, url_for

app = Flask(__name__)
app.secret_key='49562cda0f124d03e0890b77cd94db43ce4b580bebf0fc434ac590f718698f0f'

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form.get('username')
        flash(f'Привет, {name}', 'success')
        return redirect(url_for('index'))
    return render_template('task5.html')






if __name__ == '__main__':
    app.run(debug=True)