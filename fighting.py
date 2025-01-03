import cv2
import numpy as np
import mediapipe as mp
from keras.models import load_model
import telepot  # Import telepot library for Telegram integration
import io
import threading

def inFrame(lst):
    if lst[28].visibility > 0.6 and lst[27].visibility > 0.6 and lst[15].visibility > 0.6 and lst[16].visibility > 0.6:
        return True
    return False

def is_punching(landmarks):
    left_shoulder = np.array([landmarks[11].x, landmarks[11].y])
    right_shoulder = np.array([landmarks[12].x, landmarks[12].y])
    left_wrist = np.array([landmarks[15].x, landmarks[15].y])
    right_wrist = np.array([landmarks[16].x, landmarks[16].y])

    left_distance = np.linalg.norm(left_shoulder - left_wrist)
    right_distance = np.linalg.norm(right_shoulder - right_wrist)

    if left_distance < 0.2 or right_distance < 0.2:
        return True
    return False

# Load the trained model
model = load_model("fight_detection_model.h5")
cap = cv2.VideoCapture(0)
holistic = mp.solutions.pose
holis = holistic.Pose()
drawing = mp.solutions.drawing_utils

# Setup the Telegram bot
bot = telepot.Bot('7543448339:AAGk0tcz0ovu3hniOqktEMraaBm75OLjr3o')  # Replace with your bot's token
chat_id = '5223196348'  # Replace with the chat ID

def send_alert_and_image_to_telegram(image, message):
    def send_message():
        is_success, img_bytes = cv2.imencode('.jpg', image)
        if is_success:
            byte_io = io.BytesIO(img_bytes)
            bot.sendPhoto(chat_id, photo=byte_io)
            bot.sendMessage(chat_id, message)

    # Send the alert in a new thread
    threading.Thread(target=send_message).start()

while True:
    _, frm = cap.read()
    frm = cv2.flip(frm, 1)
    frm = cv2.resize(frm, (640, 480))  # Resize to improve processing speed

    res = holis.process(cv2.cvtColor(frm, cv2.COLOR_BGR2RGB))

    lst = []
    if res.pose_landmarks and inFrame(res.pose_landmarks.landmark):
        for i in res.pose_landmarks.landmark:
            lst.append(i.x - res.pose_landmarks.landmark[0].x)
            lst.append(i.y - res.pose_landmarks.landmark[0].y)

        lst = np.array(lst).reshape(1, -1)

        p = model.predict(lst)
        pred = np.argmax(p)

        if is_punching(res.pose_landmarks.landmark):
            print("Fighting Detected!")
            cv2.putText(frm, "Fighting Detected!", (50, 100), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
            send_alert_and_image_to_telegram(frm, "Alert: Fighting Detected at at location https://maps.app.goo.gl/boaF1uByNhmYefd48!")
        else:
            cv2.putText(frm, "No Fighting", (50, 100), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    cv2.imshow("Real-time Detection", frm)

    if cv2.waitKey(1) == 27:  # Press 'Esc' to exit
        cv2.destroyAllWindows()
        cap.release()
        break
