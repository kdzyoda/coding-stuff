import matplotlib.pyplot as plt # type: ignore
import matplotlib.patches as patches # type: ignore

# Create a figure and axis
fig, ax = plt.subplots()

# Set the aspect of the plot to be equal
ax.set_aspect('equal')

# Draw the cell membrane
cell = patches.Circle((0.5, 0.5), 0.4, edgecolor='black', facecolor='none')
ax.add_patch(cell)

# Draw the metaphase plate (an imaginary line)
metaphase_plate = patches.Rectangle((0.4, 0.1), 0.2, 0.8, edgecolor='black', linestyle='dashed', facecolor='none')
ax.add_patch(metaphase_plate)

# Draw chromosomes aligned at the metaphase plate
chromosomes = [
    patches.Ellipse((0.5, 0.15), 0.05, 0.1, edgecolor='blue', facecolor='blue'),
    patches.Ellipse((0.5, 0.3), 0.05, 0.1, edgecolor='blue', facecolor='blue'),
    patches.Ellipse((0.5, 0.45), 0.05, 0.1, edgecolor='blue', facecolor='blue'),
    patches.Ellipse((0.5, 0.6), 0.05, 0.1, edgecolor='blue', facecolor='blue'),
    patches.Ellipse((0.5, 0.75), 0.05, 0.1, edgecolor='blue', facecolor='blue')
]
for chromosome in chromosomes:
    ax.add_patch(chromosome)

# Draw spindle fibers
spindle_fibers = [
    patches.FancyArrowPatch((0.1, 0.15), (0.45, 0.15), color='red', arrowstyle='->'),
    patches.FancyArrowPatch((0.1, 0.3), (0.45, 0.3), color='red', arrowstyle='->'),
    patches.FancyArrowPatch((0.1, 0.45), (0.45, 0.45), color='red', arrowstyle='->'),
    patches.FancyArrowPatch((0.1, 0.6), (0.45, 0.6), color='red', arrowstyle='->'),
    patches.FancyArrowPatch((0.1, 0.75), (0.45, 0.75), color='red', arrowstyle='->'),
    patches.FancyArrowPatch((0.9, 0.15), (0.55, 0.15), color='red', arrowstyle='->'),
    patches.FancyArrowPatch((0.9, 0.3), (0.55, 0.3), color='red', arrowstyle='->'),
    patches.FancyArrowPatch((0.9, 0.45), (0.55, 0.45), color='red', arrowstyle='->'),
    patches.FancyArrowPatch((0.9, 0.6), (0.55, 0.6), color='red', arrowstyle='->'),
    patches.FancyArrowPatch((0.9, 0.75), (0.55, 0.75), color='red', arrowstyle='->')
]
for spindle in spindle_fibers:
    ax.add_patch(spindle)

# Add labels
ax.text(0.2, 0.9, 'Spindle Pole', color='red', fontsize=12)
ax.text(0.75, 0.9, 'Spindle Pole', color='red', fontsize=12)
ax.text(0.35, 0.05, 'Metaphase Plate', color='black', fontsize=12, ha='center')

# Remove the axes
ax.axis('off')

# Display the plot
plt.title('Metaphase Illustration')
plt.show()
