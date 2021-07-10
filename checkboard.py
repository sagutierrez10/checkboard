from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html', row=8, col= 8 )  

@app.route('/play/<horizontal>/<vertical>')
def repeat(horizontal, vertical):
    return render_template('index.html', row= int(horizontal), col= int(vertical))  

@app.route('/play/<horizontal>/<vertical>/<string:color1>/<string:color2>')
def color(horizontal, vertical, color1, color2):
    return render_template('index.html', row= int(horizontal), col=int(vertical), color1= color1, color2= color2)  

if __name__=="__main__":
    app.run(debug=True)