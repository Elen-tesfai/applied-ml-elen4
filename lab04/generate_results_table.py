import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression, Ridge, ElasticNet
from sklearn.preprocessing import PolynomialFeatures
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

# Example function to generate a results table
def generate_results():
    # Here you would load and process your data (e.g., Titanic dataset)
    # This is just a mock-up example
    data = {
        'Model': ['Linear Regression', 'Ridge Regression', 'ElasticNet', 'Polynomial Regression'],
        'R^2': [0.85, 0.83, 0.84, 0.87],
        'MAE': [10.5, 11.2, 10.8, 9.9],
        'RMSE': [12.0, 13.5, 12.3, 11.7],
    }

    # Create DataFrame
    df_results = pd.DataFrame(data)

    # Save the results table to a .png file
    fig, ax = plt.subplots(figsize=(8, 3))
    ax.axis('tight')
    ax.axis('off')
    table = ax.table(cellText=df_results.values, colLabels=df_results.columns, loc='center')
    table.auto_set_font_size(False)
    table.set_fontsize(10)
    table.auto_set_column_width(col=list(range(len(df_results.columns))))

    # Save the table as an image
    plt.savefig('results_table.png', dpi=300, bbox_inches='tight')
    plt.show()

# Run the function to generate the table
if __name__ == "__main__":
    generate_results()