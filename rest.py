from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', result=None)

@app.route('/add', methods=['POST'])
def add_numbers():
    try:
        a = float(request.form['a'])
        b = float(request.form['b'])
        result = a + b
        return render_template('index.html', result=result)
    except (ValueError, KeyError):
        return render_template('index.html', result="Invalid input!")

if __name__ == '__main__':
    app.run(debug=True)
