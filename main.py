from flask import Flask, render_template
from register import RegisterForm

app = Flask(__name__)
app.config["SECRET_KEY"] = "hello hello world dlrow olleh"

@app.route('/', methods = ["GET", "POST"])
def main():
    return render_template("base.html", title="Main")

@app.route('/students', methods = ["GET", "POST"])
def students():
    array = ["Иван Петров", "Пётр Ильич", "Василий Сидоров"]
    return render_template("all_students.html", title="List Students",
                           list_students = array)


@app.route('/login', methods = ["GET", "POST"])
def login():
    return render_template("login.html", title="Authorization")

@app.route('/register', methods = ["GET", "POST"])
def register():
    form = RegisterForm()
    return render_template('register.html', title='Регистрация', form=form)


if __name__ == '__main__':
    app.run()