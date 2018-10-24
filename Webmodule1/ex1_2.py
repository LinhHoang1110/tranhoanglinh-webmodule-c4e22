from flask import Flask, render_template
app = Flask(__name__)

@app.route("/bmi/<int:weight>/<int:height>")
def bmi(weight,height):
    height = height/100
    bmi = weight/(height*height)
    return render_template("ex1_2.html",bmi=bmi)

        
 

if __name__ == '__main__':
  app.run(debug=True)