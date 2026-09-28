import cv2

from image_processing import (
    preprocess_image,
    detect_edges,
    detect_objects
)


# -----------------------------------
# 1. Read Image
# -----------------------------------

image = cv2.imread("images/objects.jpg")

if image is None:
    print("Error: Image not found.")
    print("Place your image at: images/objects.jpg")
    raise SystemExit(1)


# -----------------------------------
# 2. Preprocess Image
# -----------------------------------

gray, blurred = preprocess_image(image)


# -----------------------------------
# 3. Detect Edges
# -----------------------------------

edges = detect_edges(blurred)


# -----------------------------------
# 4. Detect Objects
# -----------------------------------

result, object_count = detect_objects(
    edges,
    image.copy()
)


# -----------------------------------
# 5. Display Results
# -----------------------------------

cv2.imshow("Original Image", image)
cv2.imshow("Grayscale", gray)
cv2.imshow("Edges", edges)
cv2.imshow("Detected Objects", result)

print("--------------------------------")
print("Edge Detection & Shape Analysis")
print("--------------------------------")
print("Number of detected objects:", object_count)


# -----------------------------------
# 6. Save Result
# -----------------------------------

cv2.imwrite(
    "output/detected_objects.jpg",
    result
)

print("Result saved to output/detected_objects.jpg")


# -----------------------------------
# 7. Close Windows
# -----------------------------------

cv2.waitKey(0)
cv2.destroyAllWindows()
