from flask import Flask, render_template


app = Flask(__name__)
user = {
    "huy":{
        "name": "Nguyen Quang huy",
        "age": 29
    },
    "tuananh":{
        "name": "Huynh Tuan Anh",
        "age":22
    }
}


@app.route("/user/<username>")
def profile(username):
    if username in user.keys():
        return render_template("ex2.html", user = user[username])
    else: 
        return "User not found"    

   

    

if __name__ == '__main__':
  app.run(debug=True)