from flask import Flask as f, render_template, request

app = f("__main__")

def isvul(data):
    isvul = False
    file = open("dict.txt", "r")
    while True:
        line = file.readline()

        if not line:
            break
        if (line.strip() == data):
            isvul = True
            break

    return isvul

@app.route("/")
def index():
    return render_template("index.html")

@app.route('/', methods=['GET','POST'])
def parse_request():
    data = request.form.get('pass')
    if(isvul(data)):
        return "<h1>The password '"+data+"' is vulnareble to brute force attacks as it is in the dictionary 😶</h1><h2><a href='.'> Try another one</a></h2>"
    else:
        return "<h1>Yohoo! Your password '"+data+"' is safe to use! 😁</h1><h2><a href='.'> Try another one</a></h2>"


app.run(host = "0.0.0.0", port="80", debug=True)