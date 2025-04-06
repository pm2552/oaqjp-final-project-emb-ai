import requests
import json

def emotion_detector(text_to_analyze):
    print("I'm IN")
    URL = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    input_json = { "raw_document": { "text": text_to_analyze } }
    print("Sending request")
    response = requests.post(URL, json = input_json, headers=header)
 
    if response.status_code == 200:
        return response.text
    else:
        return response


