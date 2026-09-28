import cv2


# -----------------------------------
# Preprocessing
# -----------------------------------

def preprocess_image(image):
    """
    Convert an image to grayscale and
    reduce noise using Gaussian blur.
    """

    # Convert BGR image to grayscale
    gray = cv2.cvtColor(
        image,
        cv2.COLOR_BGR2GRAY
    )

    # Reduce image noise
    blurred = cv2.GaussianBlur(
        gray,
        (5, 5),
        0
    )

    return gray, blurred


# -----------------------------------
# Edge Detection
# -----------------------------------

def detect_edges(image):
    """
    Detect image edges using Canny and
    clean/connect edges using morphology.
    """

    edges = cv2.Canny(
        image,
        50,
        150
    )

    # Morphological closing
    kernel = cv2.getStructuringElement(
        cv2.MORPH_RECT,
        (3, 3)
    )

    edges = cv2.morphologyEx(
        edges,
        cv2.MORPH_CLOSE,
        kernel,
        iterations=2
    )

    return edges


# -----------------------------------
# Object / Shape Detection
# -----------------------------------

def detect_objects(edges, original):
    """
    Find contours, filter small noise,
    calculate area, detect basic shapes,
    and draw bounding boxes.
    """

    contours, _ = cv2.findContours(
        edges,
        cv2.RETR_EXTERNAL,
        cv2.CHAIN_APPROX_SIMPLE
    )

    object_count = 0
    min_area = 500

    for contour in contours:

        # Calculate object area
        area = cv2.contourArea(contour)

        # Ignore very small objects/noise
        if area < min_area:
            continue

        object_count += 1

        # Calculate perimeter
        perimeter = cv2.arcLength(
            contour,
            True
        )

        # Approximate contour
        approx = cv2.approxPolyDP(
            contour,
            0.04 * perimeter,
            True
        )

        # Detect basic shape
        vertices = len(approx)

        if vertices == 3:
            shape = "Triangle"

        elif vertices == 4:
            x, y, w, h = cv2.boundingRect(approx)

            if h != 0:
                ratio = float(w) / h
            else:
                ratio = 0

            if 0.90 <= ratio <= 1.10:
                shape = "Square"
            else:
                shape = "Rectangle"

        elif vertices > 4:
            shape = "Circle"

        else:
            shape = "Unknown"

        # Bounding rectangle
        x, y, w, h = cv2.boundingRect(
            contour
        )

        # Draw contour
        cv2.drawContours(
            original,
            [contour],
            -1,
            (255, 0, 0),
            2
        )

        # Draw bounding box
        cv2.rectangle(
            original,
            (x, y),
            (x + w, y + h),
            (0, 255, 0),
            2
        )

        # Display object number, shape and area
        text = (
            f"Object {object_count}: "
            f"{shape} | Area: {int(area)}"
        )

        cv2.putText(
            original,
            text,
            (x, max(y - 10, 20)),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.5,
            (0, 255, 0),
            2
        )

    return original, object_count
