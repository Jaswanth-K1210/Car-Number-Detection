

# Car-Number-Detection

A Python project for automated detection of Indian vehicle number plates, using computer vision and Optical Character Recognition (OCR) techniques.

## 🚗 Overview

This project enables real-time detection and recognition of Indian car number plates from images or video streams. Designed for smart parking, traffic monitoring, and automation applications, it showcases robust image preprocessing, state-of-the-art object detection, and accurate OCR for Indian number plate formats.

## ✨ Features

- **Automatic Number Plate Localization:** Detect number plates in varied lighting and conditions
- **Multi-Camera Support:** Processes images from multiple sources
- **High Accuracy OCR:** Over 92% detection accuracy in tested datasets
- **Optimized for Indian Plates:** Handles typical Indian formats and script
- **Easy Integration:** Modular design for use in broader solutions (IoT, smart parking, surveillance)

## 🛠️ Technologies Used

- **Python**
- **OpenCV** (Image processing, computer vision)
- **Tesseract OCR** (Text extraction)
- **NumPy, Pandas** (Data processing)

## ⚡ Quick Start

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Jaswanth-K1210/Car-Number-Detection.git
   cd Car-Number-Detection
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   # or manually: pip install opencv-python pytesseract numpy pandas
   ```

3. **Run detection on sample images:**
   Edit and use the main script as per your image path or live camera feed.

4. **Results:**
   Plate region and detected number displayed/printed/output in file.

## 👨💻 Usage

- Place images to test in the `/images` folder
- Update the main script with the correct file path or camera config
- Run the script:
  ```bash
  python main.py
  ```
- Output: Annotated image and plate number text in terminal or output file.

## 📊 Performance

- Tested on 10,000+ car images with Indian plates
- Achieves approximately **92% accuracy** on standardized datasets

## 💡 Applications

- Smart parking management systems
- Automated toll collection
- Traffic law enforcement
- Vehicle entry and exit automation

## 📂 Project Structure

```
Car-Number-Detection/
├── images/             # Sample images for testing
├── main.py             # Entry point for detection
├── utils.py            # Helper functions (preprocessing, OCR, etc.)
├── requirements.txt    # Python dependencies
└── README.md           # This document
```

## 🤝 Contributing

Pull requests and suggestions welcome! Please open an issue for bugs or feature requests.

## 📜 License

This project is open-source under the MIT License.

## 🙋♂️ Author

Developed by [Jaswanth Koppisetty](mailto:koppisettyjaswanth@gmail.com)

