import requests
import json

# ใช้ API key ที่คุณได้รับ
api_key = 'f26106de4fmshfffe0fcc2882233p11ed5cjsnd7361ebb869e'
url = 'https://twinword-emotion-analysis-v1.p.rapidapi.com/analyze/'
headers = {
    'x-rapidapi-host': 'twinword-emotion-analysis-v1.p.rapidapi.com',
    'x-rapidapi-key': api_key,
    'content-type': 'application/x-www-form-urlencoded'
}

def emotion_detector(text_to_analyze):
    if not text_to_analyze:
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }

    data = {
        'text': text_to_analyze
    }

    # ทดสอบการเชื่อมต่อกับ Twinword API
    try:
        response = requests.post(url, headers=headers, data=data)
        if response.status_code != 200:
            return {
                'anger': None,
                'disgust': None,
                'fear': None,
                'joy': None,
                'sadness': None,
                'dominant_emotion': None
            }
        response_json = response.json()
    except requests.exceptions.RequestException as e:
        return {"Error": str(e)}
    
    # แปลงผลลัพธ์เป็น dictionary
    emotion_scores = response_json.get('emotion_scores', {})
    
    # หาอารมณ์ที่มีคะแนนสูงสุด
    dominant_emotion = max(emotion_scores, key=emotion_scores.get, default=None)
    
    # คืนค่าผลลัพธ์ในรูปแบบที่กำหนด
    return {
        'anger': emotion_scores.get('anger', 0),
        'disgust': emotion_scores.get('disgust', 0),
        'fear': emotion_scores.get('fear', 0),
        'joy': emotion_scores.get('joy', 0),
        'sadness': emotion_scores.get('sadness', 0),
        'dominant_emotion': dominant_emotion
    }
    