import matplotlib.pyplot as plt
from tabulate import tabulate

# Define your model evaluation results
models = ['Linear Regression', 'Ridge Regression', 'ElasticNet Regression', 'Polynomial Regression']
r2_scores = [0.4429978856405674, 0.44313023237980076, 0.0745403363393774, 0.3832193922112488]
mae_scores = [0.28514552488606887, 0.28572889500964493, 0.45121638917580764, 0.27885967706821485]
rmse_scores = [0.3675241656199244, 0.3674805001532071, 0.47373582221014765, 0.38674333122661997]

# Create the table data (without the "R²", "MAE", "RMSE" labels)
table_data = []
for i in range(len(models)):
    table_data.append([models[i], r2_scores[i], mae_scores[i], rmse_scores[i]])

# Define table headers
headers = ['Model', 'R²', 'MAE', 'RMSE']

# Create the table string
table = tabulate(table_data, headers=headers, tablefmt='grid')

# Print the table to see if it's correctly formatted
print(table)

# Create the plot (saving the table as an image)
fig, ax = plt.subplots(figsize=(10, 3))  # Set the size of the table
ax.axis('tight')
ax.axis('off')
ax.table(cellText=table_data, colLabels=headers, loc='center')

# Save the table as an image
plt.savefig('results_table.png', dpi=300, bbox_inches='tight')

plt.show()  # Optionally show the table image