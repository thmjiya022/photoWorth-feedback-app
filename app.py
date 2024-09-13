from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    if request.method == "POST":
        post_experience = request.form["post_experience"]
        like_system = request.form['like_system']
        favorite_feature = request.form["favorite_feature"]

if __name__ == '__main__':
    app.debug = True
    app.run()