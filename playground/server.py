from turtle import color
from flask import Flask, render_template
app= Flask(__name__)

@app.route('/play')
def index():
    color='aquamarine'
    num_of_boxes=3
    return render_template('index.html', num_of_boxes=num_of_boxes, color_input=color)

@app.route('/play/<int:x>')
def multiple_boxes(x):
    color='aquamarine'
    return render_template('index.html', num_of_boxes=x, color_input=color)

@app.route('/play/<int:x>/<color>')
def change_color(x, color):
    return render_template('index.html', num_of_boxes=x, color_input=color)

if __name__=="__main__":
    app.run(debug=True)