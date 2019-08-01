from flask import Blueprint,request,jsonify
import pickle
import numpy as np
import pandas as pd
import gensim
from sklearn.feature_extraction.text import TfidfVectorizer
from gensim.parsing.preprocessing import strip_numeric 
from gensim.parsing.preprocessing import strip_non_alphanum
from gensim.parsing.preprocessing import strip_punctuation
from gensim.parsing.preprocessing import strip_punctuation2
from gensim.parsing.preprocessing import strip_multiple_whitespaces
from gensim.parsing.preprocessing import strip_tags
from gensim.parsing.preprocessing import stem_text
from gensim.parsing.preprocessing import preprocess_string
model=pickle.load(open('t2','rb'))
v=pickle.load(open("pink","rb"))
ratings=[0,1]

filters=[
    strip_numeric,strip_punctuation,strip_tags,
    strip_punctuation2,stem_text
]

def clean(string):
     words=preprocess_string(string,filters)
     return " ".join(word.lower() for word in words)



#rresult=[]
model_predict =Blueprint('model_predict',__name__)
@model_predict.route('/predict',methods=['POST'])

def predict_value():
    content = request.get_json()
    predstring = content["input"]
    print("hello")
    print("hello")
    ps=clean(predstring)
    #rk=tokenize(gf)
    x=v.transform(ps)
    r=model.predict(x) 
    print("hello")
    print("PREDICTIONS :")
    print(r)
    return jsonify(
    {
      "review" : str(r[0])
    }             
            
)