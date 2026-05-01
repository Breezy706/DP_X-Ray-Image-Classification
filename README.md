# 🩻 X-ray Image Classification using Deep Learning

**Deep Learning Project by @breezy_yrn**

---

## 📌 Project Overview

This project focuses on **medical image classification** using chest X-ray images to detect whether a patient is **NORMAL** or has **PNEUMONIA**.

Using **Deep Learning (Convolutional Neural Networks)** and **Transfer Learning**, the system analyzes grayscale X-ray images and predicts the presence of pneumonia, helping in early diagnosis and decision-making.

---

## 🎯 Objective

* Classify chest X-ray images into:

  * NORMAL
  * PNEUMONIA
* Build and train a CNN model from scratch
* Apply transfer learning using a pre-trained model (VGG16)
* Evaluate performance using accuracy metrics

---

## 📊 Dataset

The dataset contains labeled chest X-ray images divided into:

* Training set
* Validation set
* Test set

📎 **Dataset Link:**
👉 https://drive.google.com/drive/folders/1d0CElm_eNFVXVhDvdpnGpgSsabivg90H?usp=drive_link

---

## 🧠 Models Used

### 1️⃣ Custom CNN Model

* 3 Convolutional Layers (64, 128, 256 filters)
* MaxPooling & Dropout
* Fully Connected Dense Layers
* Sigmoid activation for binary classification

### 2️⃣ Transfer Learning (VGG16)

* Pre-trained VGG16 model (ImageNet)
* Frozen base layers
* Custom dense layers added for classification

---

## ⚙️ Technologies Used

* Python 🐍
* TensorFlow / Keras
* OpenCV
* NumPy
* Matplotlib

---

## 🚀 How to Run the Project

1. Clone the repository

```bash
git clone https://github.com/Breezy706
```

2. Navigate to the project folder

```bash
cd your-repo-name
```

3. Install dependencies

```bash
pip install -r requirements.txt
```

4. Run the Python script or Jupyter Notebook

---

## 📈 Model Performance

### ✅ Custom CNN

* Training Accuracy: ~97%
* Validation Accuracy: up to 100% (small validation set)
* Test Accuracy: ~72%

### ✅ Transfer Learning (VGG16)

* Training Accuracy: ~96%
* Validation Accuracy: ~93%
* Test Accuracy: ~89.5%

---

## 🧪 Prediction Example

The model can:

* Load a new X-ray image
* Convert it to grayscale
* Resize to 100×100
* Predict class (NORMAL / PNEUMONIA)

---

## 📊 Key Features

* Image preprocessing (grayscale + resizing)
* Dataset shuffling and splitting
* CNN model training
* Transfer learning implementation
* Model saving & loading
* Real-time prediction on new images

---

## 📂 Project Structure

```
├── dataset/
│   ├── train/
│   ├── val/
│   └── test/
├── models/
├── notebooks/
├── README.md
└── requirements.txt
```

---

## 🌍 Applications

* Medical diagnosis support systems
* AI-assisted radiology
* Healthcare automation
* Early pneumonia detection

---

## 🔗 Project Links

📎 **GitHub Repository:**
👉 https://github.com/Breezy706

📎 **Dataset:**
👉 https://drive.google.com/drive/folders/1d0CElm_eNFVXVhDvdpnGpgSsabivg90H?usp=drive_link

---

## 🔮 Future Improvements

* Increase dataset size for better generalization
* Deploy as a web application (Streamlit)
* Improve model accuracy using advanced architectures
* Add multi-class disease detection

---

## 👨‍💻 Author

**@breezy_yrn (BREEZY_360)**

📎 GitHub: https://github.com/Breezy706

---

## 📜 License

This project is for educational and research purposes.

---

⭐ *If you like this project, give it a star on GitHub!*
