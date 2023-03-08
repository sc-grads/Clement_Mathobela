from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    name = 'clement'
    return render_template('assessment.html',name=name)
    
if __name__ == '__main__':
    app.run(debug = True)