from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def flores_amarillas():
    return render_template('flores_amarillas.html')

if __name__ == '__main__':
    app.run()
