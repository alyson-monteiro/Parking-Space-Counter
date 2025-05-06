# Parking Space Detector with OpenCV

This project uses computer vision techniques to detect available and occupied parking spaces in a parking lot using video footage. It employs OpenCV for image processing, adaptive thresholding, and simple contour analysis — without relying on machine learning.

## 🔍 Features

- Manual ROI selection of parking spots
- Adaptive thresholding for lighting variation handling
- Morphological operations to reduce noise
- Real-time visualization of available and occupied spots
- Dynamic parking count display

## 📁 Project Structure

- `determineSpaces.py`: Script to select and save parking space positions.
- `countSpaces.py`: Main script to process video and count available spots.
- `spaces.pkl`: File storing the coordinates of each parking space.
- `estacionamento.png`: Static image used for ROI selection.
- `videoEstacionamento.mp4`: Sample video of the parking lot.

## 🛠️ Requirements

- Python 3.8+
- OpenCV
- NumPy
- Pickle

## ▶️ How to Run

Install dependencies with:

pip install opencv-python numpy Pickle

python determineSpaces.py #if you want to mark parking spaces manually (Use the mouse to draw each spot and press Enter after each one.)

python countSpaces.py

## 📷 Video

https://github.com/user-attachments/assets/09f654b7-ab05-48a6-901c-5866e6401a60

## 🧠 Concepts Used

* Grayscale conversion
* Adaptive thresholding
* Median blur & dilation
* ROI (Region of Interest) handling
* Pixel-based classification (counting non-zero pixels)

## 📄 License

This project is open-source and available under the MIT License.
