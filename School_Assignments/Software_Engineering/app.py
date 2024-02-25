from flask import Flask
app = Flask(__name__)

@app.route('/assignment5')
def assignment5():
    return "This is for assignment 5 in CS 3203"

@app.route('/about')
def about():
    return "Student's name: John Doe, Date: 10/23/2023"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
    