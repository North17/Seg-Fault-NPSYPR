from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route('/')
def index(): 
    return render_template('index.html')

@app.route('/custom')
def custom():
    return render_template('custom.html')


if __name__ == "__main__":
    app.run()