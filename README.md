# 📚 Plagiarism Detection System

A Machine Learning-based Plagiarism Detection System that identifies copied text using Natural Language Processing (NLP). This tool is designed to assist teachers, students, and content creators by automatically flagging plagiarized content.

---

## 🚀 Features
- Detects whether a given text is plagiarized or original.
- Uses TF-IDF vectorization for text representation.
- Supports multiple ML models (Logistic Regression, Naive Bayes, Random Forest, SVM).
- Saves the trained model using Pickle for future predictions.

---

## 🧠 Tech Stack
- **Python**
- **Scikit-learn**
- **Pandas & NumPy**
- **TF-IDF Vectorizer**
- **Pickle**
- **Jupyter Notebook / Python Script**

---

## 📁 Dataset
The dataset contains two columns:
- `source_text`: Original or plagiarized text
- `label`: `1` for plagiarized, `0` for original

---

## ⚙️ Workflow
1. **Data Preprocessing**  
   - Lowercasing, symbol removal, stopword filtering
2. **Data Splitting**  
   - Train-test split (80/20)
3. **Vectorization**  
   - Applied TF-IDF to convert text to numeric form
4. **Model Training**  
   - Trained models: Logistic Regression, Naive Bayes, Random Forest, SVM
   - Best performers: Logistic Regression & Naive Bayes
5. **Model Saving**  
   - Used Pickle to save the trained model

---

## 🖥️ How to Run
1. Clone the repository:
   ```bash
   git clone https://github.com/Ankitaghavate/Plagiarism-Detection-System.git
   cd Plagiarism-Detection-System
