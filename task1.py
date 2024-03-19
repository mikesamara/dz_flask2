'''Создать страницу, на которой будет форма для ввода текста и
кнопка "Отправить"
При нажатии кнопки будет произведен подсчет количества слов
в тексте и переход на страницу с результатом.'''

from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form.get('text')

        len_name = len(name.split())
        return render_template('task1-1.html', name=len_name)
    return render_template('task1.html')






if __name__ == '__main__':
    app.run(debug=True)
