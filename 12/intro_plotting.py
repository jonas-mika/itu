import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 2, 100)

# Note that even in the OO-style, we use `.pyplot.figure` to create the figure.
fig = plt.figure(figsize=(16, 9), dpi=300)  # Create a figure as Object Figure
ax = fig.add_axes([0.1, 0.1, 0.8, 0.8])
ax.plot(x, x, label='linear')  # Plot some data on the axes.
ax.plot(x, x**2, label='quadratic')  # Plot more data on the axes...
ax.plot(x, x**3, label='cubic')  # ... and some more.
ax.set_xlabel('x label')  # Add an x-label to the axes.
ax.set_ylabel('y label')  # Add a y-label to the axes.
ax.set_title("Simple Plot")  # Add a title to the axes.
ax.legend()  # Add a legend.

fig.savefig("test_plot.pdf")
print("Done!")