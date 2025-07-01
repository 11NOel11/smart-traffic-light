import serial

# Arduino port will vary
arduino = serial.Serial('COM3', 9600, timeout=1)

def send_signal_to_arduino(signal_index):
    try:
        # Send 0, 1, 2, or 3 for respective quadrant
        arduino.write(f"{signal_index}\n".encode())
    except Exception as e:
        print("Error sending to Arduino:", e)
