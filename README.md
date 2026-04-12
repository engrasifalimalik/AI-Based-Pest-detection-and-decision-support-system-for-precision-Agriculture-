# AI-Based Pest Detection and decsion support system for precision Agriculture #

##  Abstract ##

Early detection of crop pests is critical for ensuring food security and sustainable agricultural practices. This project proposes an AI-driven system that integrates deep learning-based pest classification with a rule-based decision support mechanism to assist farmers in timely and effective pest management.

The system leverages convolutional neural networks and transfer learning to classify pest images and provides actionable recommendations based on detected pest types.

---

## Problem Statement ##

Traditional pest detection methods rely on manual inspection, which is time-consuming, error-prone, and not scalable.

This project addresses:
- Automated pest detection  
- Real-time decision support  
- AI integration in smart farming  

---

## Methodology ##

## 1. Data Analysis ##
- Class distribution analysis  
- Image preprocessing  
- Data normalization  

## 2. Model Development ##

## Baseline Models: ##
- Logistic Regression  
- Support Vector Machine  
- Random Forest  

## Deep Learning: ##
- Custom CNN  
- Transfer Learning (MobileNetV2)  

## 3. Evaluation Metrics ##

- Accuracy  
- Precision  
- Recall  
- F1 Score  

## 4. Decision Support System ##

A rule-based system maps detected pests to recommended actions for crop protection.

---

## Experimental Results ##

- Deep learning models outperform traditional ML models  
- Transfer learning improves generalization  
- Class imbalance impacts performance  

---

## Decision Support Output ##

Example:

Detected Pest: Aphids  
Confidence: 92%  
Suggested Action: Use neem oil spray and introduce biological predators  

---

## Research Contributions ##

- Integration of AI with agricultural decision-making  
- Comparative analysis of ML vs DL models  
- Prototype for smart farming applications  

---

## Future Work ##

- Integration with IoT-based smart irrigation systems  
- Real-time mobile deployment  
- Multi-modal data integration (weather + soil data)  
- Use of Vision Transformers  

---

## Technologies ##

- Python  
- TensorFlow / Keras  
- Scikit-learn  
- OpenCV  

---

## Limitations ##

- Dataset size is limited  
- Class imbalance affects performance  
- Model may not generalize to unseen field conditions  

## Citation ##
If you use this work, please cite:

Ali, A. (2026). AI-Based Pest Detection and Decision Support System for Precision Agriculture.

## Project folders structure ##
---
AI_based_pest_detection_and_decision_decision_support_system_for_Agriculture/
│
├── data/
│   ├── train/
│   ├── test/
│
├── notebooks/
│   └── eda_visualization.ipynb
│
├── src/
│   ├── preprocessing.py
│   ├── train.py
│   ├── evaluate.py
│   └── predict.py
|   └── decision_support.py
│
├── models/
│   └── pest_model.h5
│
├── results/
│   ├── experiment_results.csv
│   ├── accuracy_plot.png
│   ├── confusion_matrix.png
│
├── README.md
└── requirements.txt

## Installation ##
pip install -r requirements.txt

## 👨‍💻 Author
Asif Ali
