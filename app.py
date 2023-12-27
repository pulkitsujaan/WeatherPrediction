import tkinter as tk
from tkinter import ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import numpy as np  # Assume this is the library used for generating predictions

import pandas as pd

weather = pd.read_csv('weather.csv', index_col="DATE")


# Global variables to store selected values
selected_date = None
selected_month = None
selected_year = None

# Function to generate mock predictions for demonstration
def generate_predictions(date, month, year):
    date_str = f"{year}-{month:02d}-{date:02d}"
    # Convert the date string to datetime or use it directly in your prediction logic
    predictions = np.random.rand() * 100  # Replace with your actual prediction logic
    return date_str, predictions

# Function to update the graph based on user input
def update_graph():
    global selected_date, selected_month, selected_year
    
    date = int(date_var.get())
    month = int(month_var.get())
    year = int(year_var.get())

    selected_date = date
    selected_month = month
    selected_year = year

    date_str, predictions = generate_predictions(date, month, year)

    ax.clear()
    ax.plot([date_str], [predictions], marker='o', label='Predictions')  # Plot a single point for simplicity
    ax.set_xlabel('Date')
    ax.set_ylabel('Predicted Values')
    ax.legend()

    canvas.draw()

# GUI setup
app = tk.Tk()
app.title('Weather Prediction Model')

# Date input as dropdowns
date_label = ttk.Label(app, text='Date:')
date_var = tk.StringVar()
date_dropdown = ttk.Combobox(app, textvariable=date_var, values=list(range(1, 32)))
date_dropdown.set('1')  # Set default value

month_label = ttk.Label(app, text='Month:')
month_var = tk.StringVar()
month_dropdown = ttk.Combobox(app, textvariable=month_var, values=list(range(1, 13)))
month_dropdown.set('1')  # Set default value

year_label = ttk.Label(app, text='Year:')
year_var = tk.StringVar()
year_dropdown = ttk.Combobox(app, textvariable=year_var, values=list(range(1970, 2024)))
year_dropdown.set('1970')  # Set default value

# Graph setup
fig = Figure(figsize=(5, 4), dpi=100)
ax = fig.add_subplot(1, 1, 1)
canvas = FigureCanvasTkAgg(fig, master=app)
canvas_widget = canvas.get_tk_widget()

# Submit button
submit_button = ttk.Button(app, text='Submit', command=update_graph)

# Layout
date_label.grid(row=0, column=0, padx=10, pady=10)
date_dropdown.grid(row=0, column=1, padx=10, pady=10)

month_label.grid(row=1, column=0, padx=10, pady=10)
month_dropdown.grid(row=1, column=1, padx=10, pady=10)

year_label.grid(row=2, column=0, padx=10, pady=10)
year_dropdown.grid(row=2, column=1, padx=10, pady=10)

canvas_widget.grid(row=3, column=0, columnspan=2, padx=10, pady=10)
submit_button.grid(row=4, column=0, columnspan=2, pady=10)

# Run the GUI
app.mainloop()

# Now you can access the selected values in the global variables selected_date, selected_month, and selected_year.
print("Selected Date:", selected_date)
print("Selected Month:", selected_month)
print("Selected Year:", selected_year)
