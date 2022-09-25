from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route("/")
@app.route("/home")
def home():
    return render_template('index.html')

@app.route("/login")
def login():
    return render_template('login.html')

@app.route("/students")
def students():
    return render_template('student.html')

@app.route("/teachers")
def teachers():
    return render_template('teachers.html')



if __name__ == "__main__":
  app.run(debug=True ,port=3000)



