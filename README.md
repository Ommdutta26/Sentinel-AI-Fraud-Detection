# Sentinel-AI Fraud Detection System
🚀 Live Demo: https://sentinel-ai-fraud-detection.onrender.com/
Sentinel-AI is an advanced financial fraud detection system that combines **graph analytics, machine learning, and deep learning** to identify suspicious transactions in financial networks.

The system analyzes **transaction relationships, behavioral patterns, and temporal sequences** to detect fraud with high precision. It uses a **hybrid ensemble model (XGBoost + Neural Network + LSTM)** to achieve robust fraud detection.

---

# Project Overview

Financial fraud is increasingly sophisticated and often involves **hidden transaction networks and behavioral anomalies**.

Sentinel-AI addresses this by combining:

- Graph-based fraud detection
- Behavioral transaction analysis
- Machine learning models
- Deep learning models
- Sequential transaction modeling

The system identifies **high-risk accounts, suspicious transaction flows, and abnormal financial behaviors**.

---

# Key Features

## Graph-Based Fraud Detection

Builds a **transaction network using NetworkX**.

Extracted graph features include:

- PageRank
- Betweenness Centrality
- Node Degree
- Clustering Coefficient

These features help detect **suspicious hubs and fraud rings**.

---

## Behavioral Transaction Analysis

Sentinel-AI captures user behavior using features such as:

- Transaction velocity
- Average transaction amount
- Transaction count
- Amount deviation
- Balance inconsistencies

This helps identify **abnormal spending patterns**.

---

## Machine Learning Model (XGBoost)

An optimized **XGBoost classifier** is used for high-performance fraud prediction.

Hyperparameters are tuned using **Optuna** to maximize **AUPRC (Area Under Precision Recall Curve)**, which is crucial for **imbalanced fraud datasets**.

---

## Neural Network Model

A **Deep Neural Network (DNN)** is trained to capture nonlinear financial patterns.

Architecture:

This model improves fraud detection by learning **complex feature relationships**.

---

## Sequential Fraud Detection (LSTM)

Fraud often occurs in **sequences of transactions**.

An **LSTM model** analyzes **transaction history sequences of users**.

It detects suspicious temporal patterns such as:

- Rapid transaction bursts
- Repeated transfers
- Sudden spikes in transaction amounts

---

# Ensemble Fraud Prediction

Sentinel-AI combines predictions from multiple models.

| Model | Weight |
|------|------|
| XGBoost | 0.5 |
| Neural Network | 0.4 |
| LSTM | 0.1 |

The final fraud probability is calculated using a **weighted ensemble strategy**.

---

# Dataset

The system uses the **PaySim financial transaction dataset**, which simulates real-world mobile money transactions.

Key columns include:

- `step`
- `type`
- `amount`
- `nameOrig`
- `oldbalanceOrg`
- `newbalanceOrig`
- `nameDest`
- `oldbalanceDest`
- `newbalanceDest`
- `isFraud`

---

# Feature Engineering

The project generates **advanced fraud detection features**.

## Graph Features

- `orig_pagerank`
- `dest_pagerank`
- `dest_degree`
- `dest_between`
- `dest_cluster`

## Behavioral Features

- `velocity`
- `tx_count`
- `avg_tx_amount`
- `amount_deviation`

## Balance Consistency Features

- `balance_error`
- `dest_balance_diff`

---

# Handling Imbalanced Data

Fraud datasets are extremely **imbalanced**.

To solve this problem:

**SMOTE (Synthetic Minority Oversampling Technique)** is used to balance the dataset before training.

---

# Model Evaluation

Evaluation metrics used:

- Precision
- Recall
- F1 Score
- AUPRC (Area Under Precision-Recall Curve)

A custom **decision threshold** is selected to ensure **high recall for fraud detection**.

---

# Model Explainability

The system uses **SHAP (SHapley Additive Explanations)** to explain model predictions.

This helps identify:

- Most influential fraud features
- Model decision reasoning
- Transaction risk drivers

---

# Fraud Network Visualization

Fraudulent transactions are visualized using **network graphs** to detect clusters of suspicious accounts.

Examples include:

- Fraud transaction network
- Suspicious account hubs
- Fraud rings

---

# Project Architecture

---

# Fraud Risk Classification

Transactions are classified into three risk levels.

| Probability | Classification |
|-------------|---------------|
| ≥ 75% | High Risk (Fraud) |
| 60% – 85% | Suspicious |
| < 60% | Normal |

---

# Installation

Clone the repository:

```bash
git clone https://github.com/yourusername/Sentinel-AI-Fraud.git
cd Sentinel-AI-Fraud
