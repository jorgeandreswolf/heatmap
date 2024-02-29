import json
import seaborn as sns
import matplotlib.pyplot as plt

# Load coordinates from the JSON file
with open('coordinates.json', 'r') as file:
    screen_coordinates = json.load(file)

# Extract x and y coordinates
x = [coord['x'] for coord in screen_coordinates]
y = [coord['y'] for coord in screen_coordinates]

colors = sns.color_palette("RdBu_r", as_cmap=True)

# Create a heatmap with the custom color palette
sns.histplot(x=x, y=y, cmap=colors, cbar=True)

# Add labels and title
plt.xlabel("X Coordinate")
plt.ylabel("Y Coordinate")
plt.title("Heat Map of Screen Coordinates")

# Show the plot
plt.show()
