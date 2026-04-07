from ultralytics import YOLO
import cv2
from twilio.rest import Client

from lighting import decide_brightness, predictive_lighting
from weather_module import get_weather_light
from dashboard import update_dashboard

model = YOLO("yolov8n.pt")


def detect_objects():

    cap = cv2.VideoCapture(0)

    sms_sent = False

    while True:

        ret, frame = cap.read()

        if not ret:
            break

        results = model(frame)

        vehicle_count = 0
        pedestrian = False
        accident = False

        for r in results:
            for box in r.boxes:

                cls = int(box.cls)

                if cls == 0:
                    pedestrian = True

                if cls in [2,3,5,7]:
                    vehicle_count += 1

        weather, color, brightness_weather, brightness_time = get_weather_light()

        ai_brightness = decide_brightness(vehicle_count, pedestrian, weather)

        pole1, pole2, pole3 = predictive_lighting(vehicle_count)

        print("Vehicles:", vehicle_count)
        print("Pedestrian:", pedestrian)
        print("Weather:", weather)
        print("AI Brightness:", ai_brightness)
        print("Pole1:", pole1, "Pole2:", pole2, "Pole3:", pole3)

        if vehicle_count >= 2:
            accident = True

        if accident:

            print("🚨 ACCIDENT DETECTED")

            if not sms_sent:

                account_sid = "AC06d64cfd98861bd9a080205cd905b43e"
                auth_token = "3521cc929d5e05d92594f6ffbbc44490"

                client = Client(account_sid, auth_token)

                # Location coordinates
                latitude = 13.0827
                longitude = 80.2707

                location_link = f"https://maps.google.com/?q={latitude},{longitude}"

                message = client.messages.create(
                    body=f"🚨 SMART STREET LIGHT SYSTEM\nAccident detected on road.\n\nLive Location:\n{location_link}",
                    from_="+12604002962",
                    to="+919677699624"
                )

                print("SMS sent successfully!")
                print("Message SID:", message.sid)

                sms_sent = True

        annotated_frame = results[0].plot()

        cv2.imshow("Smart Street Detection", annotated_frame)

        update_dashboard(
            vehicle_count,
            pedestrian,
            weather,
            ai_brightness,
            pole1,
            pole2,
            pole3,
            accident
        )

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()