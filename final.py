import cv2
import numpy as np
import pytesseract
import time
import re

pytesseract.pytesseract.tesseract_cmd = '/usr/local/bin/tesseract'

def is_valid_number_plate(text):
    # Define the regex pattern for valid number plate
    pattern = r'^[A-Z]{2} \d{2} [A-Z]{2} \d{4}$'
    return re.match(pattern, text) is not None

def process_frame(frame):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (5, 5), 0)
    edges = cv2.Canny(blur, 100, 200)

    contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for contour in contours:
        area = cv2.contourArea(contour)
        if area > 1000:
            x, y, w, h = cv2.boundingRect(contour)
            aspect_ratio = w / float(h)
            if 2 < aspect_ratio < 5:
                roi = frame[y:y+h, x:x+w]
                
                # Resize the ROI for better OCR results
                roi_resized = cv2.resize(roi, None, fx=2, fy=2, interpolation=cv2.INTER_CUBIC)
                roi_gray = cv2.cvtColor(roi_resized, cv2.COLOR_BGR2GRAY)

                # Apply thresholding for better text extraction
                _, roi_binary = cv2.threshold(roi_gray, 150, 255, cv2.THRESH_BINARY_INV)

                # OCR on the processed ROI
                number_plate_text = pytesseract.image_to_string(roi_binary, config='--psm 7 --oem 3').strip()
                
                if is_valid_number_plate(number_plate_text):
                    return number_plate_text, roi
    return None, None

def main():
    cap = cv2.VideoCapture(0)
    detected_number_plate = None
    start_time = None
    end_time = None

    while True:
        ret, frame = cap.read()
        if not ret:
            print("Failed to grab frame")  # Debug output
            break

        number_plate_text, roi = process_frame(frame)
        

        if number_plate_text and detected_number_plate is None:
            detected_number_plate = number_plate_text
            start_time = time.time()
            print(f"Detected Number Plate: {detected_number_plate} at {time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(start_time))}")

        elif detected_number_plate and number_plate_text is None:
            end_time = time.time()
            print(f"Number Plate {detected_number_plate} went out of range at {time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(end_time))}")

            # Save the detected number plate data to a file with timestamp
            try:
                with open('number_plates.txt', 'a') as f:
                    f.write(f"{detected_number_plate}, Start: {time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(start_time))}, End: {time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(end_time))}\n")
                print("Data saved to file")  # Debug output
            except Exception as e:
                print(f"Error writing to file: {e}")
            detected_number_plate = None  # Reset after saving

        # Show the frame with bounding box
        cv2.imshow('Frame', frame)
        
        if roi is not None:
            cv2.imshow('ROI', roi)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()
