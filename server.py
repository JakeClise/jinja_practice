from flask import Flask, render_template
app = Flask(__name__)

@app.route('/hello/<string:name>/<int:num>')
def hello_name(name, num):
    return render_template("hello.html", name=name, num=num)
    


if __name__ == ("__main__"):
    app.run(debug=True)