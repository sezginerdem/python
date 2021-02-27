from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def head():
    return render_template("index.html", number1 = 12, number2 = 27)

@app.route("/second")
def second():
   return render_template("index.html", hazirlayan = "Sezgin")
if __name__ == "__main__":
    app.run(debug = True)