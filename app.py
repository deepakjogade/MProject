from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def getstarted():
    return render_template('getstarted.html')

@app.route('/login/')
def login():
    return render_template('login.html')

@app.route('/signup/')
def signup():
    return render_template('signup.html')

@app.route('/home/')
def home():
    return render_template('index.html')
    

@app.route('/about/')
def about():
    return render_template('about.html')


if __name__ == "__main__":
    app.run()