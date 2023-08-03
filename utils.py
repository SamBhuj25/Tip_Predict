
import pickle
import json
import numpy as np
import warnings
warnings.filterwarnings("ignore")

class Tips_Pred():
    
    def __init__(self,total_bill,gender,smoker,time,size,day):
        self.total_bill = total_bill
        self.gender = gender
        self.smoker = smoker
        self.time = time
        self.size = size
        self.day = "day_" + day
        
    def load_data(self):
        with open("model.pkl","rb") as k:
            self.model = pickle.load(k)
        
        with open("proj_data.json","r") as l:
            self.json_data = json.load(l)

        
    def pred_tips(self):
        self.load_data()
             
        day_index = self.json_data["col"].index(self.day)
        
        test_array = np.zeros([1,len(self.json_data["col"])],dtype=int)
        
        test_array[0][0] = self.total_bill
        test_array[0][1] = self.json_data["gender"][self.gender]
        test_array[0][2] = self.json_data["smoker"][self.smoker]
        test_array[0][3] = self.json_data["time"][self.time]
        test_array[0][4] = self.size
        test_array[0,day_index] = 1
        
        pred_tip = self.model.predict(test_array)    
        return pred_tip[0]
    
# obj = Tips_Pred(500,"Male","Yes","Lunch",5,"Sun")
# obj.pred_tips()
    
