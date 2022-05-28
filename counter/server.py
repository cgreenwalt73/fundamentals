from flask import Flask, render_template, request, session, redirect
app=Flask('__name__')
app.secret_key='key'

@app.route('/')
def root():
    if 'count' not in session:
        session['count']=1
    else:
        session['count']+=1
    if 'visits' not in session:
        session['visits']=1
    else:
        session['visits']+=1
    return render_template('index.html')

@app.route('/destroy_session')
def clear():
    session.clear()
    return redirect('/')

@app.route('/double_count')
def button_count():
    session['count']+=1
    return redirect('/')

@app.route('/increment_by', methods=['POST'])
def increment_by():
    session['count']= session['count'] + int(request.form['increment'])-1
    return redirect('/')

if __name__=='__main__':
    app.run(debug=True)