import cv2
from car_detection import detect_cars
from traffic_logic import decide_signal
from arduino_control import send_signal_to_arduino
from gui_overlay import draw_overlay
import time

# Constants
CAM_INDEX = 0
FRAME_WIDTH, FRAME_HEIGHT = 640, 480
SIGNAL_INTERVAL = 10  # seconds for green light per lane

# Initializations
cap = cv2.VideoCapture(CAM_INDEX)
cap.set(3, FRAME_WIDTH)
cap.set(4, FRAME_HEIGHT)

prev_signal = None
signal_timer = time.time()

print("[INFO] Starting smart traffic light system...")

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Detect cars per quadrant
    car_counts, boxes = detect_cars(frame)
    frame = draw_overlay(frame, car_counts, prev_signal, SIGNAL_INTERVAL - int(current_time - signal_timer), boxes)

    # Decide best quadrant to give green
    current_time = time.time()
    if current_time - signal_timer > SIGNAL_INTERVAL:
        signal = decide_signal(car_counts)
        send_signal_to_arduino(signal)
        prev_signal = signal
        signal_timer = current_time

    # GUI overlay
    frame = draw_overlay(frame, car_counts, prev_signal, SIGNAL_INTERVAL - int(current_time - signal_timer))

    cv2.imshow("Smart Traffic Light", frame)

    if cv2.waitKey(1) == 27:  # ESC to quit
        break

cap.release()
cv2.destroyAllWindows()
