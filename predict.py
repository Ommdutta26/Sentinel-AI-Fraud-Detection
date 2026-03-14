import joblib
from tensorflow.keras.models import load_model
import pandas as pd
# load models
xgb_model = joblib.load("fraud_xgboost.pkl")
nn_model = load_model("fraud_nn_model.h5")
lstm_model = load_model("fraud_lstm_model.h5")

features = [
    "amount",
    "oldbalanceOrg",
    "newbalanceOrig",
    "dest_degree",
    "dest_pagerank",
    "orig_pagerank",
    "dest_between",
    "dest_cluster",
    "velocity",
    "tx_count",
    "avg_tx_amount",
    "amount_deviation",
    "balance_error",
    "dest_balance_diff",
    "type_CASH_OUT",
    "type_DEBIT",
    "type_PAYMENT",
    "type_TRANSFER"
]


def predict_fraud(
    amount, old_balance, new_balance,
    old_dest_balance, new_dest_balance,
    dest_degree, velocity,
    type_transfer, type_cashout
):

    try:

        # -----------------------------
        # Feature Engineering
        # -----------------------------
        balance_error = old_balance - amount - new_balance
        dest_balance_diff = new_dest_balance - old_dest_balance

        input_dict = {
            "amount": amount,
            "oldbalanceOrg": old_balance,
            "newbalanceOrig": new_balance,
            "dest_degree": dest_degree,
            "dest_pagerank": 0.001,
            "orig_pagerank": 0.001,
            "dest_between": 0.0,
            "dest_cluster": 0.0,
            "velocity": velocity,
            "tx_count": 1,
            "avg_tx_amount": amount,
            "amount_deviation": 0,
            "balance_error": balance_error,
            "dest_balance_diff": dest_balance_diff
        }

        # -----------------------------
        # Transaction Type Encoding
        # -----------------------------
        for col in features:
            if col.startswith("type_"):
                input_dict[col] = 0

        if "type_TRANSFER" in features:
            input_dict["type_TRANSFER"] = int(type_transfer)

        if "type_CASH_OUT" in features:
            input_dict["type_CASH_OUT"] = int(type_cashout)

        # -----------------------------
        # Create Input DataFrame
        # -----------------------------
        input_df = pd.DataFrame([input_dict])

        # Ensure column order matches training
        input_df = input_df.reindex(columns=features, fill_value=0)

        # -----------------------------
        # Model Predictions
        # -----------------------------

        # XGBoost
        xgb_prob = float(xgb_model.predict_proba(input_df)[0][1])

        # Neural Network
        nn_prob = float(nn_model.predict(input_df.values, verbose=0)[0][0])

        # LSTM Sequence Model
        from tensorflow.keras.preprocessing.sequence import pad_sequences
        import numpy as np

        seq = pad_sequences([[amount]], maxlen=10)
        seq = seq.reshape((1, 10, 1))

        lstm_prob = float(lstm_model.predict(seq, verbose=0)[0][0])

        # -----------------------------
        # Weighted Ensemble
        # -----------------------------
        weights = {
            "xgb": 0.5,
            "nn": 0.4,
            "lstm": 0.1
        }

        final_prob = (
            weights["xgb"] * xgb_prob +
            weights["nn"] * nn_prob +
            weights["lstm"] * lstm_prob
        )

        # -----------------------------
        # Decision Logic
        # -----------------------------
        if final_prob >= 0.75:
            status = "🚨 FRAUD DETECTED"
            risk = "HIGH RISK"

        elif final_prob >= 0.60:
            status = "⚠️ SUSPICIOUS"
            risk = "MEDIUM RISK"

        else:
            status = "✅ NORMAL"
            risk = "LOW RISK"

        # -----------------------------
        # Optional Debug Info
        # -----------------------------
        # print("XGB:", xgb_prob)
        # print("NN:", nn_prob)
        # print("LSTM:", lstm_prob)
        # print("FINAL:", final_prob)

        return status, f"{final_prob*100:.2f}%", risk

    except Exception as e:
        return "Error", str(e), "Check console"