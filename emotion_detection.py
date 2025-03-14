import requests
import json

def emotion_detector(text_to_analyze):
    # API URL and headers
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    
    # Prepare input JSON
    input_json = {"raw_document": {"text": text_to_analyze}}
    
    # Make the API call
    try:
        response = requests.post(url, json=input_json, headers=headers, timeout=10)
        response.raise_for_status() 
        
        # Parse the response
        response_json = response.json()
        
        # Get the text attribute and parse it as JSON
        emotions_data = json.loads(response_json.get('text', '{}'))
        
        # Extract the emotion scores
        anger_score = emotions_data.get('emotion', {}).get('anger', 0)
        disgust_score = emotions_data.get('emotion', {}).get('disgust', 0)
        fear_score = emotions_data.get('emotion', {}).get('fear', 0)
        joy_score = emotions_data.get('emotion', {}).get('joy', 0)
        sadness_score = emotions_data.get('emotion', {}).get('sadness', 0)
        
        # Find the dominant emotion (emotion with the highest score)
        emotions = {
            'anger': anger_score,
            'disgust': disgust_score,
            'fear': fear_score,
            'joy': joy_score,
            'sadness': sadness_score
        }
        dominant_emotion = max(emotions.items(), key=lambda x: x[1])[0]
        
        # Return the required output format
        return {
            'anger': anger_score,
            'disgust': disgust_score,
            'fear': fear_score,
            'joy': joy_score,
            'sadness': sadness_score,
            'dominant_emotion': dominant_emotion
        }
    
    except requests.exceptions.RequestException as e:
        print(f"Error during API call: {e}")
        return None

