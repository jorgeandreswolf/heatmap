import json
import tkinter as tk
from tkinter import filedialog
import seaborn as sns
import matplotlib.pyplot as plt

def load_json_data():
    file_path = filedialog.askopenfilename(title="Select JSON File", filetypes=[("JSON files", "*.json")])
    if file_path:
        with open(file_path, 'r') as file:
            data = json.load(file)
        return data
    return None

def generate_contour_plot():
    data = load_json_data()
    if data:
        x = [coord['x'] for coord in data]
        y = [coord['y'] for coord in data]

        sns.kdeplot(x=x, y=y, fill=True, cmap="Blues", common_norm=False)
        plt.xlabel("X Coordinate")
        plt.ylabel("Y Coordinate")
        plt.title("Contour Plot of Screen Coordinates")
        plt.show()

def save_contour_plot():
    file_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png")])
    if file_path:
        plt.savefig(file_path)

# Create the main application window
app = tk.Tk()
app.title("Contour Plot Generator")

# Create buttons
load_button = tk.Button(app, text="Load JSON", command=generate_contour_plot)
load_button.pack(pady=10)

save_button = tk.Button(app, text="Save Contour Plot", command=save_contour_plot)
save_button.pack(pady=10)

# Start the application
app.mainloop()
