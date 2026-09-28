# AI Image Enhancement Toolkit

## Program 3: Edge Detection & Shape Analysis System

An intermediate-level Digital Image Processing project built with Python and OpenCV.

The program processes an image through the following pipeline:

**Image → Grayscale → Gaussian Blur → Canny Edge Detection → Morphological Processing → Contours → Shape Detection → Bounding Boxes → Area Calculation → Object Count**

## Features

- Read an input image
- Convert image to grayscale
- Remove noise using Gaussian Blur
- Detect edges using Canny
- Apply morphological processing
- Detect contours
- Filter small/noise objects
- Calculate object area
- Detect basic shapes
- Draw bounding boxes
- Display object number
- Display detected shape
- Display object area
- Count detected objects
- Save the processed result

## Technologies

- Python
- OpenCV
- VS Code
- Git
- GitHub

## Project Structure

```text
AI_Image_Enhancement_Toolkit/
│
├── main.py
├── image_processing.py
├── README.md
├── requirements.txt
├── .gitignore
│
├── images/
│   └── objects.jpg
│
└── output/
    └── detected_objects.jpg
```

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/YOUR-USERNAME/AI-Image-Enhancement-Toolkit.git
cd AI-Image-Enhancement-Toolkit
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

Or:

```bash
pip install opencv-python
```

## Input Image

Place your image here:

```text
images/objects.jpg
```

The program expects the file name:

```text
objects.jpg
```

You can replace it with your own image, but if you use another filename, update the path in `main.py`.

## Run the Program

```bash
python main.py
```

If your system uses `py` instead:

```bash
py main.py
```

## Processing Pipeline

```text
Input Image
     ↓
Grayscale Conversion
     ↓
Gaussian Blur
     ↓
Canny Edge Detection
     ↓
Morphological Closing
     ↓
Contour Detection
     ↓
Small Noise Removal
     ↓
Shape Detection
     ↓
Bounding Box
     ↓
Area Calculation
     ↓
Object Count
     ↓
Output Image
```

## Example Output

The program displays:

```text
--------------------------------
Edge Detection & Shape Analysis
--------------------------------
Number of detected objects: 4
Result saved to output/detected_objects.jpg
```

The output image contains bounding boxes and labels such as:

```text
Object 1: Rectangle | Area: 12450
Object 2: Circle | Area: 15670
Object 3: Triangle | Area: 8320
```

## Important Parameter

The program ignores contours smaller than:

```python
min_area = 500
```

If small objects are not detected, reduce this value.

For example:

```python
min_area = 200
```

If too much noise is detected, increase it:

```python
min_area = 1000
```

## Learning Objectives

This project demonstrates:

1. Image acquisition
2. Image enhancement
3. Noise reduction
4. Edge detection
5. Morphological image processing
6. Contour extraction
7. Shape analysis
8. Object measurement
9. Object counting
10. Modular Python programming

## Author

Computer Engineering Student

## License

This project is intended for educational and academic use.
