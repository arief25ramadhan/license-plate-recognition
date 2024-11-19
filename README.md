# License Plate Recognition with OCR

This project implements a license plate recognition system using OpenCV for image processing and Tesseract OCR for text extraction. It detects license plates from an image and extracts the text from them.

---

## Features

- Detects license plates in images.
- Extracts text from the license plate using Tesseract OCR.
- Includes preprocessing techniques for enhanced accuracy.

---

## Prerequisites

Ensure the following software and libraries are installed:

1. **C++ Compiler** (supporting C++17 or higher).
2. **CMake** (version 3.10 or later).
3. **OpenCV** (version 4.x recommended).
4. **Tesseract OCR**:
   - Linux: `sudo apt-get install tesseract-ocr libtesseract-dev`
   - macOS: `brew install tesseract`
   - Windows: Use the [Tesseract installer](https://github.com/tesseract-ocr/tesseract) or build it from source.

---

## Project Structure

LicensePlateRecognition/ │ ├── src/ │ ├── main.cpp # Main program ├── CMakeLists.txt # Build configuration ├── README.md # Project documentation └── license_plate.jpg # Sample input image

yaml
Copy code

---

## Build and Run Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/LicensePlateRecognition.git
cd LicensePlateRecognition
```
2. Create a Build Directory
```bash
Copy code
mkdir build
cd build
```
3. Configure the Project
```bash
Copy code
cmake ..
```
4. Build the Project
```bash
Copy code
make
```
5. Run the Program
```bash
Copy code
./LicensePlateRecognition
```
Make sure the sample image license_plate.jpg is in the project directory.

How It Works
Preprocessing:

Converts the input image to grayscale.
Applies Gaussian blur to reduce noise.
Uses Canny edge detection to identify edges in the image.
License Plate Detection:

Identifies contours in the processed image.
Filters and approximates contours to detect regions resembling license plates.
OCR with Tesseract:

Crops the detected license plate region.
Processes the cropped image for optimal OCR performance.
Uses Tesseract OCR to extract text.
Dependencies
The project uses the following libraries:

OpenCV - For image processing.
Tesseract OCR - For optical character recognition.
Sample Output
Input Image:













