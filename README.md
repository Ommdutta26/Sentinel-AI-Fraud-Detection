Sentinel-AI Fraud Detection System

Sentinel-AI is an advanced financial fraud detection system that combines graph analytics, machine learning, and deep learning to identify suspicious transactions in financial networks.

The system analyzes transaction relationships, behavioral patterns, and temporal sequences to detect fraud with high precision.
It uses a hybrid ensemble model (XGBoost + Neural Network + LSTM) to achieve robust fraud detection.

Project Overview

Financial fraud is increasingly sophisticated and often involves hidden transaction networks and behavioral anomalies.

Sentinel-AI addresses this by combining:

Graph-based fraud detection

Behavioral transaction analysis

Machine learning models

Deep learning models

Sequential transaction modeling

The system identifies high-risk accounts, suspicious transaction flows, and abnormal financial behaviors.

Key Features
Graph-Based Fraud Detection

Builds a transaction network using NetworkX.

Extracts graph features such as:

PageRank

Betweenness Centrality

Node Degree

Clustering Coefficient

These features help detect suspicious hubs and fraud rings.

Behavioral Transaction Analysis

Sentinel-AI captures user behavior using features like:

Transaction velocity

Average transaction amount

Transaction count

Amount deviation

Balance inconsistencies

This helps identify abnormal spending patterns.

Machine Learning Model (XGBoost)

An optimized XGBoost classifier is used for high-performance fraud prediction.

Hyperparameters are tuned using Optuna to maximize AUPRC (Area Under Precision Recall Curve), which is crucial for imbalanced fraud datasets.

Neural Network Model

A Deep Neural Network (DNN) is trained to capture nonlinear financial patterns.

Architecture:

Input → Dense → BatchNorm → Dropout → Dense → Dense → Output

This model improves fraud detection by learning complex feature relationships.

Sequential Fraud Detection (LSTM)

Fraud often occurs in sequences of transactions.

An LSTM model is used to analyze transaction history sequences of users.

It detects suspicious temporal patterns such as:

Rapid transaction bursts

Repeated transfers

Sudden spikes in transaction amounts

Ensemble Fraud Prediction

Sentinel-AI combines predictions from multiple models:

Model	Weight
XGBoost	0.5
Neural Network	0.3
LSTM	0.2

Final fraud probability is calculated using a weighted ensemble strategy.

Dataset

The system uses the PaySim financial transaction dataset, which simulates real-world mobile money transactions.

Key columns include:

step

type

amount

nameOrig

oldbalanceOrg

newbalanceOrig

nameDest

oldbalanceDest

newbalanceDest

isFraud

Feature Engineering

The project generates advanced fraud detection features.

Graph Features

orig_pagerank

dest_pagerank

dest_degree

dest_between

dest_cluster

Behavioral Features

velocity

tx_count

avg_tx_amount

amount_deviation

Balance Consistency Features

balance_error

dest_balance_diff

Handling Imbalanced Data

Fraud datasets are extremely imbalanced.

To solve this:

SMOTE (Synthetic Minority Oversampling Technique) is used to balance the dataset before training.

Model Evaluation

Metrics used:

Precision

Recall

F1 Score

AUPRC (Area Under Precision-Recall Curve)

A custom decision threshold is selected to ensure high recall for fraud detection.

Model Explainability

The system uses SHAP (SHapley Additive Explanations) to explain model predictions.

This helps identify:

Most influential fraud features

Model decision reasoning

Transaction risk drivers

Fraud Network Visualization

Fraudulent transactions are visualized using Network Graphs to detect clusters of suspicious accounts.

Example visualization:

Fraud transaction network

Suspicious account hubs

Fraud rings

Project Architecture
Dataset
   │
   ├── Data Preprocessing
   │
   ├── Feature Engineering
   │      ├── Graph Features
   │      ├── Behavioral Features
   │      └── Balance Features
   │
   ├── Data Balancing (SMOTE)
   │
   ├── Model Training
   │      ├── XGBoost
   │      ├── Neural Network
   │      └── LSTM
   │
   ├── Ensemble Model
   │
   └── Fraud Prediction System
Fraud Risk Classification

The system categorizes transactions into three risk levels.

Probability	Classification
≥ 85%	High Risk (Fraud)
60% – 85%	Suspicious
< 60%	Normal
Installation

Clone the repository:

git clone https://github.com/yourusername/Sentinel-AI-Fraud.git
cd Sentinel-AI-Fraud

Install dependencies:

pip install -r requirements.txt
Required Libraries
pandas
numpy
networkx
scikit-learn
xgboost
tensorflow
imblearn
optuna
shap
matplotlib
joblib
Running the Project

Run the fraud detection pipeline:

python fraud_detection.py
Model Files

Saved models:

fraud_xgboost.pkl
fraud_nn.keras
lstm_model.keras

These models are used for real-time fraud prediction.

Example Fraud Prediction
status, probability, risk = predict_fraud(
    amount=5000,
    old_balance=10000,
    new_balance=5000,
    old_dest_balance=2000,
    new_dest_balance=7000,
    dest_degree=3,
    velocity=2000,
    type_transfer=1,
    type_cashout=0
)

print(status, probability, risk)

Output Example:

🚨 FRAUD DETECTED 91.23% HIGH RISK
Future Improvements

Graph Neural Networks (GNN) for fraud detection

Real-time streaming fraud detection

Fraud ring detection algorithms

Explainable AI dashboard

API integration for banking systems

Applications

Banking fraud detection

Payment gateway security

Digital wallet protection

Financial compliance systems

Author

Omm Dutta

AI / Machine Learning Developer

If you want, I can also give you a 🔥 much stronger GitHub README (with badges, architecture diagrams, and screenshots) so that this project looks like a top-tier placement project.
