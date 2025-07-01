# traffic_controller.py

from utils import HIGH_DENSITY_THRESHOLD, MEDIUM_DENSITY_THRESHOLD

def decide_signal(vehicle_count):
    if vehicle_count > HIGH_DENSITY_THRESHOLD:
        return "G", 15
    elif vehicle_count > MEDIUM_DENSITY_THRESHOLD:
        return "G", 10
    else:
        return "G", 5
