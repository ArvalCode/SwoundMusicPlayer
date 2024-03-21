from flask import Flask, render_template
import os


app = Flask(__name__)

@app.route('/')
def index():
    dir_list = os.listdir("music") 
    print(dir_list)
    return render_template('home.html', the_title='Music Player App', music = dir_list)


if __name__ == '__main__':
    app.run(debug=True)