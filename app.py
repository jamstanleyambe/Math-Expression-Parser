from email.parser import Parser

from flask import Flask, request, render_template
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


class Parser:
    def __init__(self, expression):
        self.expression = expression
        self.index = 0

    def parse(self):
        return self.parse_expression()

    def parse_expression(self):
        result = self.parse_term()
        while self.index < len(self.expression) and self.expression[self.index] in ('+', '-'):
            op = self.expression[self.index]
            self.index += 1
            term = self.parse_term()
            if op == '+':
                result += term
            elif op == '-':
                result -= term
        return result

    def parse_term(self):
        result = self.parse_factor()
        while self.index < len(self.expression) and self.expression[self.index] in ('*', '/'):
            op = self.expression[self.index]
            self.index += 1
            factor = self.parse_factor()
            if op == '*':
                result *= factor
            elif op == '/':
                result /= factor
        return result

    def parse_factor(self):
        if self.expression[self.index] == '(':
            self.index += 1
            result = self.parse_expression()
            self.index += 1  # Move past closing parenthesis
            return result
        else:
            start = self.index
            while self.index < len(self.expression) and self.expression[self.index].isdigit():
                self.index += 1
            return int(self.expression[start:self.index])



