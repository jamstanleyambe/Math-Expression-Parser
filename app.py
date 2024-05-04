from flask import Flask, request, render_template

from parser import Parser

app = Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/parse', methods=['POST'])
def parse_expression():
    expression = request.form['expression']
    result = Parser(expression).parse()
    return render_template('result.html', expression=expression, result=result)

if __name__ == '__main__':
    app.run(debug=True)
