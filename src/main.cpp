#include <opencv2/opencv.hpp>
#include <tesseract/baseapi.h>
#include <iostream>

using namespace cv;
using namespace std;

int main() {
    // Load the image
    Mat image = imread("license_plate.jpg");
    if (image.empty()) {
        cerr << "Error: Image not loaded." << endl;
        return -1;
    }

    // Convert to grayscale
    Mat gray;
    cvtColor(image, gray, COLOR_BGR2GRAY);

    // Apply Gaussian blur to reduce noise
    GaussianBlur(gray, gray, Size(5, 5), 0);

    // Edge detection using Canny
    Mat edges;
    Canny(gray, edges, 50, 200);

    // Find contours
    vector<vector<Point>> contours;
    findContours(edges, contours, RETR_TREE, CHAIN_APPROX_SIMPLE);

    // Approximate contours and find the plate
    Rect licensePlateRect;
    for (const auto& contour : contours) {
        double area = contourArea(contour);
        if (area < 500 || area > 10000) continue; // Filter contours by area

        // Approximate contour to polygon
        vector<Point> approx;
        approxPolyDP(contour, approx, 0.02 * arcLength(contour, true), true);

        // Look for rectangles
        if (approx.size() == 4) {
            licensePlateRect = boundingRect(approx);
            break;
        }
    }

    if (licensePlateRect.area() > 0) {
        // Crop the license plate area
        Mat licensePlate = image(licensePlateRect);

        // Preprocess for OCR
        Mat ocrReady;
        cvtColor(licensePlate, ocrReady, COLOR_BGR2GRAY);
        threshold(ocrReady, ocrReady, 0, 255, THRESH_BINARY | THRESH_OTSU);

        // Initialize Tesseract
        tesseract::TessBaseAPI tess;
        if (tess.Init(NULL, "eng", tesseract::OEM_LSTM_ONLY)) {
            cerr << "Error: Could not initialize Tesseract." << endl;
            return -1;
        }

        // Set image for OCR
        tess.SetImage(ocrReady.data, ocrReady.cols, ocrReady.rows, 1, ocrReady.step);

        // Get OCR result
        string text = tess.GetUTF8Text();
        cout << "License Plate Text: " << text << endl;
    } else {
        cerr << "License plate not found." << endl;
    }

    return 0;
}