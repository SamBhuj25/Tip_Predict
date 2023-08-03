from flask import Flask, request, jsonify,render_template
from utils import Tips_Pred
import config

app = Flask(__name__)

@app.route("/")
def home():

    return render_template("index.html")

@app.route("/predict_tip",methods = ["GET","POST"])
def predict_charges():
    try:

        if request.method == "POST":
            data = request.form
            
            total_bill = eval(data['total_bill'])
            gender = data['gender']
            smoker = data['smoker']
            time = data['time']
            size = data['total_persons']
            day = data["day"]

            obj = Tips_Pred(total_bill,gender,smoker,time,size,day)
            pred = obj.pred_tips().round()
            return jsonify({"Result": f"Predicted tip is {pred}- Rs"})
        
        elif request.method == "GET":

            data = request.args.get

            try :
                total_bill = eval(data('total_bill'))
                if total_bill >= 50 :

                    gender = data('gender')
                    smoker = data('smoker')
                    time = data('time')
                    day = data("day")
                else :
                    return render_template("index.html", B = "Min Bill Amount Must be More than 50 .. !!")
                
            except:
                    pass
            
            try :
                size = int(data('total_persons'))
                if type(size) == int and size >= 1:
                    obj = Tips_Pred(total_bill,gender,smoker,time,size,day)
                    tip = obj.pred_tips().round()

                    return render_template("index.html", result = tip)
                else:
                    return render_template("index.html", A = "Enter Valid No. Persons.. !!")
            except :
                return render_template("index.html", F = "Please Fill All / Valid  Details.. !!")
     
    except:
        return render_template("index.html", F = "Please Fill All / Valid  Details.. !!")

if __name__ == "__main__":
    app.run(host=config.HOST_NO ,port=config.PORT_NO,debug=False)
