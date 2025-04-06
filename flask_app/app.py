from flask import Flask
import time
app = Flask(__name__)
@app.route('/')
def hello():
    return "Hello World from Harsh Khandelwal!"
@app.route('/compute')
def compute():
    def fibonacci(n):
        if n <= 1:
            return n
        return fibonacci(n - 1) + fibonacci(n - 2)
    result = fibonacci(30)
    return f"Fibonacci(30): {result}"
