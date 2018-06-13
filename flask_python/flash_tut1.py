from flask import Flask

#Its the root path
app =Flask(__name__)

#its the homepage
# @ signifies a decorator - way to wrap a function and modifying its behavior
@app.route("/")

def index():
    return 'This is the homapage'

@app.route("/tuna")
def tuna():
    return '<h2>tuna is good</h2>'

@app.route("/profile/<username>")
def profile(username):
    return "<h2>Hey there %s<h2/>"% username


@app.route("/age/<int:age_number>")
def age(age_number):
    return "<h2>Your Age is %s<h2/>"% age_number

if __name__ == "__main__":
    app.run(debug=True)