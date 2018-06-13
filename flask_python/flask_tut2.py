from flask import Flask, request

#Its the root path
app =Flask(__name__)

@app.route("/")
def index():
    return 'Method used: %s'% request.method

@app.route("/bacon",methods=['Get','POST'])
def bacon():
    if request.method == 'POST':
         return "You are using POST"
    else:
        return 'You are using GET'

if __name__ == "__main__":
    app.run(debug=True)