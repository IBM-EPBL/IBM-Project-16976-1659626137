from keras_preprocessing import image
import numpy as np
from keras.models import load_model
import json
# from ibm_watson import VisualRecognitionV3
# from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import requests


cnn_model = load_model('trained_cnn_model.h5')


def predict_alpha(pos):
  res = {0:'A', 1:'B', 2:'C', 3:'D', 4:'E', 5:'F', 6:'G', 7:'H', 8:'I'}
  return res[pos]

def predict(img_src):
  img = image.load_img(img_src, target_size=(128,128), color_mode='grayscale')
  arr = image.img_to_array(img)
  arr = np.expand_dims(arr, axis=0)
  # API_KEY = "uK6_2BkDeaVcCaMnVSMABbOrpSde4G6uMNgSkXkA55e9"
  # token_response = requests.post('https://iam.cloud.ibm.com/identity/token', data={"apikey":
  # API_KEY, "grant_type": 'urn:ibm:params:oauth:grant-type:apikey'})
  # mltoken = token_response.json()["access_token"]
  # header = {'Content-Type': 'application/json', 'Authorization': 'Bearer ' + mltoken}
  # payload_scoring = {"input_data": [{"values": arr.tolist()}]}
  # response_scoring = requests.post('https://us-south.ml.cloud.ibm.com/ml/v4/deployments/d45d9ae4-908b-4d66-9427-e0a6a07468e9/predictions?version=2022-11-16', json=payload_scoring,
  # headers=header)
  # print(type(response_scoring))
  # print(response_scoring.json())
  # print("Scoring response")
  # res  = response_scoring.json()
  # idx = res["predictions"][0]["values"][0][1]
  prediction = np.argmax(cnn_model.predict(arr))
  return predict_alpha(prediction)