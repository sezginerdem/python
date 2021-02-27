from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def head():
    first = "This is my first condition experience in Flask"
    return render_template("index.html", Sezgin = True)

@app.route("/for")
def for_example():
    names = ['Erdem', 'Sezgin', 'Metin', 'Defne', 'Elif']
    return render_template("test.html", name = names)






if __name__ == '__main__':
    app.run(debug = True)