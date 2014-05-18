from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    author = "Monica"
    name = "Pritesh" 
    return render_template('index.html', author=author, name=name)

if __name__ == '__main__':
    app.run()
