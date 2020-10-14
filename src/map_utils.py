
import geopandas as gp
import matplotlib.pyplot as plt
import contextily as cx

class CustomMap(): 

    def __init__(self, bounds : list = None, basemap : bool = True):
        self.data_layers : list = []
        self.alpha_layers : list = []
        self.color_layers : list = []
        self.bounds : list = bounds
        self.basemap : bool = basemap
        self.label = None

    def add_layer(self, data, alpha=1.0, color=None): 
        self.data_layers.append(data)
        self.alpha_layers.append(alpha)
        self.color_layers.append(color)

    def draw(self): 
        ax = None
        for layer, alpha, color in zip(self.data_layers, self.alpha_layers, self.color_layers): 
            if ax is None: 
                if color is None: 
                    ax = layer.plot(figsize=(11,9), alpha=alpha)
                else: 
                    ax = layer.plot(figsize=(11,9), alpha=alpha, color=color)
            else: 
                if color is None: 
                    ax = layer.plot(ax=ax, figsize=(11,9), alpha=alpha)
                else: 
                    ax = layer.plot(ax=ax, figsize=(11,9), alpha=alpha, color=color)

        if not self.bounds is None:
            ax.set_xlim([self.bounds[0], self.bounds[1]])
            ax.set_ylim([self.bounds[2], self.bounds[3]])

        if self.basemap: 
            cx.add_basemap(ax=ax)

        if not self.label is None: 
            plt.xlabel(self.label)

        plt.show()

    def set_bounds(self, bounds : list): 
        if len(bounds) == 4 or bounds is None: 
            self.bounds = bounds

    def set_basemap(self, basemap : bool): 
        self.basemap = basemap

    def set_label(self, label):  
        self.label = label

    def clear(self): 
        self.alpha_layers = []
        self.data_layers = []
        self.bounds = None