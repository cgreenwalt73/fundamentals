from flask import Flask, render_template, redirect, request, session
import random
app=Flask('__name__')
app.secret_key='key'

@app.route('/')
def root():
    session['num']=random.randint(1,100)
    session['count']=0
    return render_template('index.html')

@app.route('/check', methods=['POST'])
def check_number():
    session['guess']=int(request.form['guess'])
    session['count']+=1
    return redirect('/result')

@app.route('/result')
def results():
    return render_template('results.html')

@app.route('/clear')
def clear():
    session.clear()
    return redirect('/')

if __name__=='__main__':
    app.run(debug=True)