# ✋ Hand Distance Measurement using MediaPipe

## 📌 Overview

This project is a **Computer Vision application** that measures the real-world distance (in centimeters) between fingers using a webcam.

It leverages **MediaPipe Hand Tracking** to detect hand landmarks and calculates distance using a reference measurement.

---

## 🚀 Features

* Real-time hand tracking using webcam
* Measures distance in **centimeters (cm)**
* Supports:

  * 🖐️ One-hand mode (thumb ↔ index finger)
  * 🤝 Two-hand mode (thumb ↔ thumb)
* Fast and lightweight
* Interactive UI with key controls

---

## 🧠 How It Works

1. MediaPipe detects **21 hand landmarks**
2. The **little finger length** is used as a reference (approx. 5 cm)
3. Pixel distance is calculated between landmarks
4. Converted into real-world distance using scaling:

   * `pixels → centimeters`
5. Displays the measured distance in real time

---

## 🎮 Controls

* Press **1** → One-hand measurement
* Press **2** → Two-hand measurement
* Press **Q** → Quit application

---

## ⚙️ Tech Stack

* Python
* OpenCV
* MediaPipe
* Math (distance calculation)

---

## 📦 Installation

Clone the repository:

```bash
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## ▶️ How to Run

```bash
python app.py
```

---

## 📸 Demo



Example:

```bash
![Demo](images/demo.png)
```

---

## ⚠️ Limitations

* Accuracy depends on camera angle and lighting
* Assumes average Little finger length (~5 cm)
* Not suitable for precise industrial measurements

---

## 🔮 Future Improvements

* Dynamic calibration for better accuracy
* Object measurement (not just fingers)
* GUI improvements
* Distance measurement using depth estimation

---

## 🙌 Acknowledgements

* MediaPipe for hand tracking
* OpenCV for image processing

---
