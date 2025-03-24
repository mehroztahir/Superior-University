import cv2
import numpy as np

def detect_herd(image_path, min_contour_area=500):
    # Load the image
    image = cv2.imread(image_path)
    if image is None:
        print("Error: Could not load image")
        return
    
    # Convert to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # Apply Gaussian blur to reduce noise
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)
    
    # Threshold the image (adjust threshold value as needed)
    _, thresh = cv2.threshold(blurred, 100, 255, cv2.THRESH_BINARY_INV)
    
    # Find contours
    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    # Filter small contours and draw bounding boxes
    herd_count = 0
    for contour in contours:
        if cv2.contourArea(contour) > min_contour_area:
            x, y, w, h = cv2.boundingRect(contour)
            cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)
            herd_count += 1
    
    print(f"Detected {herd_count} animal herds/groups")
    
    # Display the result
    cv2.imshow('Herd Detection', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


detect_herd('image.jpg')