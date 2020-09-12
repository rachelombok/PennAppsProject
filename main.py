from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, World!"

@app.route("/home")
def salvador():
    return render_template('home.html')

@app.route("/class")
def course():
    return render_template('class.html')

if __name__ == "__main__":
    app.run(debug=True)
