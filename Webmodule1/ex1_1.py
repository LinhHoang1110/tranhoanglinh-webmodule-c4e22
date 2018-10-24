from flask import Flask
app = Flask(__name__)

@app.route("/bmi/<int:weight>/<int:height>")
def bmi(weight,height):
    height = height/100
    bmi = weight/(height*height)
    if bmi < 16:
      return "your bmi: "+str(bmi)+" that mean: "+"Severely underweight"
    elif 16<= bmi <18.5:
      return "your bmi: "+str(bmi)+" that mean: "+"Underweight"  
    elif 18.5 <= bmi < 25:
      return "your bmi: "+str(bmi)+" that mean: "+"Normal"
    elif 25 <= bmi < 30:
      return "your bmi: "+str(bmi)+" that mean: "+"Overweight"  
    else:
      return "your bmi: "+str(bmi)+" that mean: "+"Obese"  

if __name__ == '__main__':
  app.run(debug=True)