# 🧠 Brain Tumor Detection System
A deep learning–based application that classifies MRI brain images into different tumor categories using **Transfer Learning with VGG16**. The system helps in automated and accurate tumor detection through medical image analysis.



<img width="951" height="371" alt="image" src="https://github.com/user-attachments/assets/d039694b-31c2-484b-8f0b-e61f163aca44" />
<img width="712" height="539" alt="image" src="https://github.com/user-attachments/assets/805758f7-5a87-4a03-86c0-628d57400fa3" />
<img width="987" height="284" alt="image" src="https://github.com/user-attachments/assets/8a6423bd-c19c-43f8-a6e5-e4a870fd699f" />

---

## 🚀 Features

* Classifies MRI brain scans into **four categories**: Glioma, Meningioma, Pituitary Tumor, and No Tumor
* Uses **VGG16 pre-trained CNN model** for high accuracy
* Image preprocessing and data augmentation for better generalization
* Displays **prediction confidence** along with tumor type
* Interactive **Streamlit web interface** for real-time prediction

---

## 🛠️ Technologies Used

* **Python**
* **TensorFlow / Keras**
* **CNN (VGG16 – Transfer Learning)**
* **NumPy & Pandas**
* **Matplotlib & Seaborn**
* **Streamlit**

---

## 📂 Project Structure

```
├── Training/                 # Training MRI images
├── Testing/                  # Testing MRI images
├── model.h5                  # Trained deep learning model
├── app.py                    # Streamlit application
├── detect.py                 # Tumor detection logic
├── brain_tumor.ipynb         # Jupyter Notebook (model training)
├── requirements.txt          # Dependencies
└── README.md                 # Project documentation
```

---

## 🧠 Model Architecture

* Pre-trained **VGG16** model with ImageNet weights
* Top layers removed and customized for medical classification
* Last few layers unfrozen for fine-tuning
* Dense and Dropout layers added to reduce overfitting
* **Softmax activation** for multi-class classification

---

## 📊 Model Performance

* Achieved **~95% accuracy** on test dataset
* Evaluated using:

  * Classification Report
  * Confusion Matrix
  * ROC Curve & AUC Score

---

## 🖥️ How to Run the Project

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/Abhishek10075/MRI-Brain-Tumor-Detection-System.git
cd Brain-Tumor-Detection
```

### 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 3️⃣ Run Streamlit App

```bash
streamlit run app.py
```

---

## 📸 Sample Output

* Upload MRI image
* Model predicts:

  * Tumor Type
  * Confidence Score

---

## 📌 Use Case

* Medical image analysis
* Assisting radiologists in tumor detection
* AI-based healthcare applications

---

## ⚠️ Disclaimer

This project is for **educational and research purposes only** and should not be used as a replacement for professional medical diagnosis.

---

## 👤 Author

**Abhishek Nishad**

If you like this project, ⭐ star the repository on Git
