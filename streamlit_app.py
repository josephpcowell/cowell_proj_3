'''
This .py is the structure for the Streamlit app associated with
the corresponding project on predicting fraudulent credit card transactions.
'''

# IMPORTS
import streamlit as st

# Import the usual suspects
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
import pickle

# Import functions to aid in modeling
from collections import Counter
from sklearn import metrics
from sklearn.metrics import precision_recall_curve, recall_score

# Start of the app layout

st.write(
    """# Predicting Fraud for Mastercard ![](https://icons-for-free.com/iconfiles/png/128/card+ecommerce+logo+master+mastercard+shopping+icon-1320193177496345842.png)
"""
)

st.write(
    """
## Model: XG Boost
The model behind the scenes consists of Mastercard transaction data.
Move the 'Probability Threshold' slider to tailor the model and see
how it performs. This app will help it's user decide how the model
works and find the perfect threshold for it's final purpose.

"""
)


# Load the prediction probabilities
with open("data/X_prob.npy", "rb") as f:
    X_probabilities = np.load(f)

# Create slider to tailor threshold
thresh = st.slider("Probability Threshold", 0.0, 1.0, 0.13)

# Create the predictions based on the threshold
y_pred = X_probabilities[:, 1] > thresh

# Import the test target
with open("data/y_test.npy", "rb") as f:
    y_test = np.load(f)

# Create data for the curve
precision, recall, thresholds = precision_recall_curve(
    y_test, X_probabilities[:, 1]
)
pr_auc = metrics.auc(recall, precision)

conf_mat = pd.DataFrame(metrics.confusion_matrix(y_test, y_pred))


# Plot 1: Precision & Recall

plt.rcParams["font.family"] = "DIN Alternate"
fig1, ax = plt.subplots()
ax.grid(False)
ax.set_facecolor("1")
ax.spines["bottom"].set_color("0")
ax.spines["left"].set_color("0")
plt.title("Precision & Recall for the Final Model", fontweight="bold")
plt.plot(thresholds, precision[:-1], "--", label="Precision", color="#0563C1")
plt.plot(thresholds, recall[:-1], "--", label="Recall", color="#954F72")
plt.xlabel("Threshold", fontweight="bold")
plt.legend(loc="lower left")
plt.ylim([0, 1])
ax.axvline(x=thresh, ymin=0, ymax=1, color="#A57931")
st.pyplot(fig1)


precision2, recall2, thresholds2 = precision_recall_curve(y_test, y_pred)

fraud_recall = recall_score(y_test, y_pred)
nfraud_recall = recall_score(y_test, y_pred, pos_label=0)

st.write(
    """
**Fraudulent Transaction Recall:** {:.2%}  
**Falsely Predicted Valid Transactions:** {:.2%}

With the visual representation of the model's metric and threshold,
combined with the metrics shared above, deciding on the perfect 
model will help the user understand exactly how the model will perform.

""".format(
        fraud_recall, (1 - nfraud_recall)
    )
)

st.write(
    """
____
## Extra Visuals
To further highlight the metrics described above,
look at the heatmap before to see
insight into the data, as well as the model's predictions.

"""
)


# Plot 2: Confusion Matrix

conf_mat = pd.DataFrame(metrics.confusion_matrix(y_test, y_pred))
fig2, ax = plt.subplots()
sns.set(font_scale=1.4)
sns.heatmap(
    conf_mat,
    annot=True,
    fmt=".0f",
    annot_kws={"size": 14},
    xticklabels=["Not Fraud", "Fraud"],
    yticklabels=["Not Fraud", "Fraud"],
    cmap="gray_r",
)
plt.yticks(rotation=0)
plt.xlabel("Predicted", fontweight="bold")
plt.ylabel("Actual", rotation=0, y=0.92, fontweight="bold")
plt.title("Model Predictions on Test Data", fontweight="bold", size=20)
st.pyplot(fig2)

st.write(
    """
_____
Check out the full repository
[here](https://github.com/josephpcowell/cowell_proj_3)
"""
)
