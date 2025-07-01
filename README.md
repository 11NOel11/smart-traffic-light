# smart-traffic-light
AI-powered smart traffic light system using Python + YOLOv8 + Arduino. Detects vehicle density via webcam and dynamically controls LEDs for a toy traffic model.
# 🚦 AI-Powered Smart Traffic Light System (Toy Model)

This project uses computer vision (YOLOv8) and Arduino to simulate a smart traffic light system. A webcam detects toy cars in a small road model, and based on traffic density, Python sends red/green light commands to an Arduino that controls LEDs.

---

## 💻 Features

- Real-time vehicle detection using webcam + YOLOv8
- Dynamic green/red signal control based on car count
- Live visualization of detection + traffic count
- Arduino-controlled LEDs (Red & Green) via serial

---

## 📦 Requirements

- Python 3.8+
- Arduino UNO + USB cable
- LEDs (Red & Green) + 220Ω resistors
- Webcam
- `ultralytics`, `opencv-python`, `pyserial`

Install dependencies:

```bash
cd backend
pip install -r requirements.txt
```
## 📥 Download YOLOv8n Model
Download the pretrained model file from:
```
https://github.com/ultralytics/assets/releases/download/v0.0.0/yolov8n.pt
```
Then, place yolov8n.pt in the backend/ folder.

---

## 🛠️ Arduino Setup
Upload the Arduino code from:

arduino/traffic_light.ino



