import sys
sys.path.append('D:\\ต้น\\python\\oaqjp-final-project-emb-ai')  # ระบุเส้นทางไปยังโฟลเดอร์ oaqjp-final-project-emb-ai

from EmotionDetection import emotion_detector

# ทดสอบข้อความต่างๆ และคาดหวังผลลัพธ์
test_cases = [
    ("I am glad this happened", "joy"),
    ("I am really mad about this", "anger"),
    ("I feel disgusted just hearing about this", "disgust"),
    ("I am so sad about this", "sadness"),
    ("I am really afraid that this will happen", "fear")
]

# ฟังก์ชันทดสอบ
def run_tests():
    all_passed = True
    for text, expected_emotion in test_cases:
        result = emotion_detector(text)
        dominant_emotion = result['dominant_emotion']
        print(f"Result for '{text}': {result}")  # พิมพ์ผลลัพธ์เพื่อการตรวจสอบ
        if dominant_emotion == expected_emotion:
            print(f"PASS: {text} -> {dominant_emotion}")
        else:
            print(f"FAIL: {text} -> {dominant_emotion} (expected {expected_emotion})")
            print(f"Scores: {result}")  # พิมพ์คะแนนของอารมณ์ทั้งหมดเพื่อการตรวจสอบเพิ่มเติม
            all_passed = False
    return all_passed

# เรียกฟังก์ชันทดสอบ
if __name__ == "__main__":
    if run_tests():
        print("All tests passed.")
    else:
        print("Some tests failed.")
