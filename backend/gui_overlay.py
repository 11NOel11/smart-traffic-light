def draw_overlay(frame, car_counts, green_index, countdown, boxes=None):
    height, width, _ = frame.shape

    # Draw YOLO boxes
    if boxes:
        for box in boxes:
            x1, y1, x2, y2 = map(int, box.xyxy[0])
            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 255), 2)

    # Rest of your existing GUI overlay (quadrant lines, counts, etc.)
    ...
import cv2

def draw_overlay(frame, car_counts, green_index, countdown):
    height, width, _ = frame.shape

    # Draw borders
    cv2.line(frame, (width//2, 0), (width//2, height), (255, 255, 255), 2)
    cv2.line(frame, (0, height//2), (width, height//2), (255, 255, 255), 2)

    directions = ['Top-Left', 'Top-Right', 'Bottom-Left', 'Bottom-Right']
    for i, count in enumerate(car_counts):
        x = 10 if i % 2 == 0 else width//2 + 10
        y = 30 if i < 2 else height//2 + 30
        color = (0, 255, 0) if i == green_index else (0, 0, 255)
        cv2.putText(frame, f"{directions[i]}: {count} cars", (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.6, color, 2)

    # Countdown timer
    cv2.putText(frame, f"Time Left: {countdown}s", (width//2 - 80, height - 20), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 255), 2)

    return frame
