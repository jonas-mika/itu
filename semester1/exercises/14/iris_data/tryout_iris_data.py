import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats

iris_classes = ["Iris Setosa", "Iris Versicolour", "Iris Virginica"]
attributes = ["Sepal Length", "Sepal Width", "Petal Lenght", "Petal Width"]

# load the iris dataset using the default loadtxt method within numpy, no delimiter needed, because the datset is delimited with whitespaces
def load_data(filepath : str):
    return np.loadtxt(filepath)

def plot_bar(data):
    unique_classes, counts = np.unique(data[:,-1], return_counts=True)

    # create a figure
    fig = plt.figure(figsize=(16,9))
    axes = fig.add_axes([0.1,0.1,0.8,0.8])

    # plot the bar
    axes.bar(unique_classes, counts, fc="blue", alpha=0.3)

    # label
    title ="Frequency of Classes of Iris Flower" 
    axes.set_title(title, fontweight="bold"); axes.set_xlabel("Classes of Iris Flower"); axes.set_ylabel("Frequency")
    axes.set_xticks(unique_classes)
    axes.set_xticklabels([name for name in iris_classes])

    return fig

def plot_histograms(data):
    # create a figure with subplots
    fig, axes = plt.subplots(nrows=3, ncols=4, figsize=(40,20))
    fig.subplots_adjust(bottom = 0.1, top = 0.9, wspace = 0.2, hspace = 0.3)

    for x in range(3):
        mask = data[:,-1] == x
        for i in range(4):
            axes[x][i].hist(data[:,i][mask], color="blue", density=True, alpha=0.3, edgecolor="k", linewidth=0.5)

            # find mu and sigma for each attribute
            mu, sigma = stats.norm.fit(data[:,i][mask])

            # plot the normal distribution fit 
            xmin, xmax = axes[x][i].get_xlim()
            z = np.linspace(xmin, xmax, 100)
            p = stats.norm.pdf(z, mu, sigma)
            axes[x][i].plot(z, p,"k", linewidth=1);
            
            # labeling the plots
            axes[x][i].set_title("{} of {}".format(attributes[i], iris_classes[x]), fontweight="bold", fontsize=8);
            #axes[x][i].set_yticks([i*10 for i in range(3)])
            if x == 2:
                axes[x][i].set_xlabel("{} (cm)".format(attributes[i]))
            if i == 0:
                axes[x][i].set_ylabel("Frequency")

    return fig 

def main():
    filepath = "/Users/jonassenghaas/python/itu/semester 1/assignments/assignment5/iris.data"
    data = load_data(filepath)

    # split the array into two arrays
    attributes = data[:,:4] # two-dimensional array with the attributes being the columns
    flower_class = data[:,-1] # one-dimensional array containing the class of the flower

    figure_counts = plot_bar(data)
    # plt.show(figure_counts)
    figure_counts.savefig("output_plots/Frequency of Classes of Iris Flower.pdf")

    histograms = plot_histograms(data)
    # plt.show(histograms)

    histograms.savefig("output_plots/Attribute Histograms of Iris Classes.pdf")

if __name__ == "__main__":
    print("Plotting...")
    main()