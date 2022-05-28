from flask import Flask, render_template
app=Flask(__name__)

@app.route('/')
def root():
    color1='red'
    color2='black'
    x=8
    y=8
    return render_template('index.html', color1=color1, color2=color2, rows=x, columns=y)

@app.route('/<int:x>')
def change_rows(x):
    color1='red'
    color2='black'
    y=8
    return render_template('index.html', color1=color1, color2=color2, rows=x, columns=y)

@app.route('/<int:x>/<int:y>')
def change_rows_and_columns(x,y):
    color1='red'
    color2='black'
    return render_template('index.html', color1=color1, color2=color2, rows=x, columns=y)

@app.route('/<int:x>/<int:y>/<string:color1>/<string:color2>')
def change_colors_too(x,y,color1,color2):
    return render_template('index.html', rows=x, columns=y, color1=color1, color2=color2)

if __name__=="__main__":
    app.run(debug=True)