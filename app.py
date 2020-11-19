from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route('/')
def index(): 
    return render_template('index.html')




@app.route('/line')
def line():
    return render_template('line.html')



    
@app.route('/heat')
def heat():
    return render_template('heat.html')


    
@app.route('/infographics')
def infographics():
    return render_template('infographics.html')





@app.route('/custom')
def custom():
    return render_template('custom.html')





if __name__ == "__main__":
    app.run()