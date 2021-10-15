from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'secured'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process ():
    print("got post info")
    session['name'] = request.form['name']
    session['location'] = request.form['location']
    session['language'] = request.form['language']
    session['comment'] = request.form['comment']
    return redirect('/result')

@app.route('/result')
def result():
    print(request.form)
    return render_template("result.html")

if __name__=="__main__":
    app.run(debug=True)