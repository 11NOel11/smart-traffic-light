from ultralytics import YOLO
import cv2

# Load YOLOv8 Small model
model = YOLO('yolov8s.pt')  # <--- Updated here

# COCO classes relevant for traffic detection
CAR_CLASSES = ['car', 'truck', 'bus', 'motorcycle']

def detect_cars(frame):
    height, width, _ = frame.shape

    # Run YOLOv8 inference
    results = model.predict(source=frame, imgsz=640, conf=0.4, device=0, verbose=False)[0]

    boxes = results.boxes
    cls = boxes.cls.tolist()
    xyxy = boxes.xyxy.tolist()

    # Define 4 quadrants
    quadrants = [
        [0, 0, width // 2, height // 2],        # Top-Left
        [width // 2, 0, width, height // 2],    # Top-Right
        [0, height // 2, width // 2, height],   # Bottom-Left
        [width // 2, height // 2, width, height]  # Bottom-Right
    ]

    car_counts = [0, 0, 0, 0]
    for i, class_id in enumerate(cls):
        name = model.names[int(class_id)]
        if name not in CAR_CLASSES:
            continue

        x1, y1, x2, y2 = xyxy[i]
        cx, cy = int((x1 + x2) / 2), int((y1 + y2) / 2)

        for idx, (qx1, qy1, qx2, qy2) in enumerate(quadrants):
            if qx1 <= cx <= qx2 and qy1 <= cy <= qy2:
                car_counts[idx] += 1
                break

    return car_counts, boxes
