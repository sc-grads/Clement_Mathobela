from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return '<h1>Welcome to puppy latin, use 127.0.0.1:7500/puppy_name to see</h1>'
    
@app.route('/<name>')
def puppy_latin(name):
    if name[-1].lower() != 'y':
        return name + 'y'
    else :
        return name[0:-1] + 'iful'
        
if __name__ == '__main__':
    app.run(debug=True)