#model oluşturulduktan sonra API yi oluşturuyoruz.

from fastapi import FastAPI
import pandas as pd
import pickle                        #eğittiğimiz modeli çıktı almak için 
from pydantic import BaseModel       #veriyi istediğimiz standartta alabilmek için kullandığımız kütüphane

app=FastAPI()   #bir app, değişken oluşturuyoruz.

@app.get("/")

def home():
    return {"Modele hoşgeldiniz."}

#uvicorn main:app --reload

#Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age


class model_schema(BaseModel):    #basemodel den kalıttığımız class'ımız.
    CreditScore:int
    Geography:str
    Gender:str
    Age  :int
    Tenure:int
    Balance:int
    NumOfProducts:int
    HasCrCard:int
    IsActiveMember:int
    EstimatedSalary:float


@app.post("/predict/model")     #post:api ye veri göndermek için kullanılır.
def model(predict_values:model_schema):
    load_model=pickle.load(open('xgboost.pkl','rb'))
    df = pd.DataFrame([predict_values.dict()])
    
    print("-------------------")
    print(df["Geography"])  # doğru erişim
    df["Geography"] = df["Geography"].apply(lambda x: {'france': 1, 'germany': 2, 'spain': 3}[x])
    df['Gender'] = df['Gender'].apply(lambda x: {'female': 1, 'male': 2}[x])
    
    #df=pd.DataFrame([predict_values.dict().values()],columns=predict_values.dict().keys())   #gelen veri dict yapısında olduğu için dict() dedik. Dict den verileri almak içinde values kullanmamız gerekir(key leri almamış oluruz.). Columns kısmında key leri alıyoruz.
    print(df)
    predict=load_model.predict(df)
    print('sonuc:',predict,'veri tipi:',type(predict))
    return {"predict":int(predict)}