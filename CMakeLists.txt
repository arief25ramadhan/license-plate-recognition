cmake_minimum_required(VERSION 3.10)
project(LicensePlateRecognition)

# Specify C++ standard
set(CMAKE_CXX_STANDARD 17)

# Find OpenCV
find_package(OpenCV REQUIRED)
include_directories(${OpenCV_INCLUDE_DIRS})

# Find Tesseract
find_package(Tesseract REQUIRED)
include_directories(${Tesseract_INCLUDE_DIRS})

# Add executable
add_executable(LicensePlateRecognition src/main.cpp)

# Link libraries
target_link_libraries(LicensePlateRecognition ${OpenCV_LIBS} ${Tesseract_LIBRARIES})