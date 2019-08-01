
from flask import Flask
import router1
ml=Flask('ml')

ml.register_blueprint(router1.model_predict)

ml.run(host="0.0.0.0",port=5005,debug=True)
