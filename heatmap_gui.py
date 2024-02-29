import json
import tkinter as tk
from tkinter import filedialog
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap

def load_json_data():
    """ Load JSON file """
    file_path = filedialog.askopenfilename(title="Select JSON File", filetypes=[("JSON files", "*.json")])
    if file_path:
        with open(file_path, 'r') as file:
            data = json.load(file)
        return data
    return None

def generate_heatmap():
    """ generate heatmap from JSON data """
    data = load_json_data()
    if data:
        x = [coord['x'] for coord in data]
        y = [coord['y'] for coord in data]

        colors = sns.color_palette("RdBu_r", as_cmap=True)

        sns.histplot(x=x, y=y, cmap=colors, cbar=True)
        plt.xlabel("X Coordinate")
        plt.ylabel("Y Coordinate")
        plt.title("Heat Map of Screen Coordinates")
        plt.show()

def save_heatmap():
    """ save heatmap as PNG file """
    file_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png")])
    if file_path:
        plt.savefig(file_path)

# Create the main application window
app = tk.Tk()
app.title("Heatmap Generator")

# Create buttons
load_button = tk.Button(app, text="Load JSON", command=generate_heatmap)
load_button.pack(pady=10)

save_button = tk.Button(app, text="Save Heatmap", command=save_heatmap)
save_button.pack(pady=10)

# Start the application
app.mainloop()
