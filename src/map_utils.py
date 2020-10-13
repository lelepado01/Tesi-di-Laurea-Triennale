
import geopandas as gp
import matplotlib.pyplot as plt
import contextily as cx

class CustomMap(): 

    def __init__(self, bounds : list = None, basemap : bool = True):
        self.data_layers : list = []
        self.alpha_layers : list = []
        self.bounds : list = bounds
        self.basemap : bool = basemap

    def add_layer(self, data, alpha=1.0): 
        self.data_layers.append(data)
        self.alpha_layers.append(alpha)

    def draw(self): 
        ax = None
        for layer, alpha in zip(self.data_layers, self.alpha_layers): 
            if ax is None: 
                ax = layer.plot(figsize=(11,9), alpha=alpha)
            else: 
                ax = layer.plot(ax=ax, figsize=(11,9), alpha=alpha)

        if not self.bounds is None:
            ax.set_xlim([bounds[0], bounds[1]])
            ax.set_ylim([bounds[2], bounds[3]])

        if self.basemap: 
            cx.add_basemap(ax=ax)

        plt.show()

    def set_bounds(self, bounds : list): 
        if len(bounds) == 4 or bounds is None: 
            self.bounds = bounds

    def set_basemap(self, basemap : bool): 
        self.basemap = basemap

    def clear(self): 
        self.alpha_layers = []
        self.data_layers = []
        self.bounds = None