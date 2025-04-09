import pandas as pd
import matplotlib.pyplot as plt
from pandas.plotting import table

# Data for the table
data = {
    "Model": ["Random Forest (100)", "Gradient Boosting (100)"],
    "Train Accuracy": [1.0000, 0.9625],
    "Test Accuracy": [0.8656, 0.8531],
    "Accuracy Gap": [0.1344, 0.1094],
    "Train F1 Score": [1.0000, 0.9607],
    "Test F1 Score": [0.8461, 0.8385],
    "F1 Gap": [0.1539, 0.1222],
    "Train Precision": [1.0000, 0.9638],
    "Test Precision": [0.8301, 0.8351],
    "Train Recall": [1.0000, 0.9625],
    "Test Recall": [0.8656, 0.8531],
    "Confusion Matrix (Test)": [
        "[[27, 0, 20], [0, 0, 11], [12, 0, 250]]",
        "[[22, 0, 25], [0, 2, 9], [10, 3, 249]]"
    ]
}

# Create DataFrame
df = pd.DataFrame(data)

# Plot the table
fig, ax = plt.subplots(figsize=(14, 6))  # Set the figure size for clarity
ax.axis('off')  # Hide axes
tbl = table(ax, df, loc='center', colWidths=[0.2] * len(df.columns))

# Style the table
tbl.auto_set_font_size(False)  # Disable auto font size
tbl.set_fontsize(12)  # Set font size for better readability
tbl.scale(1.5, 1.5)  # Increase scale to make the table larger and more readable

# Save the table as PNG
plt.savefig("ensemble_models_table_clear.png", bbox_inches="tight", dpi=300)