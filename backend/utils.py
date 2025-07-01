# config.py

# YOLOv8 model
YOLO_MODEL_PATH = "yolov8n.pt"

# Webcam index (0 is usually front camera)
CAMERA_INDEX = 0

# Arduino serial port
ARDUINO_PORT = "COM3"     # Change if needed
BAUD_RATE = 9600

# COCO vehicle class IDs
VEHICLE_CLASSES = [2, 3, 5, 7]

# Traffic count thresholds
HIGH_DENSITY_THRESHOLD = 10
MEDIUM_DENSITY_THRESHOLD = 5
