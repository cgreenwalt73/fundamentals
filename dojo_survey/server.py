from flask import Flask, render_template, request, session, redirect
app=Flask('__name__')
app.secret_key='key'

@app.route('/')
def root():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def submit_form():
    session['name']=request.form['name']
    session['location']=request.form['location']
    session['language']=request.form.getlist('language')
    session['comment']=request.form['comment']
    return redirect('/result')

@app.route('/result')
def submissions():
    return render_template('database.html')

if __name__=='__main__':
    app.run(debug=True)