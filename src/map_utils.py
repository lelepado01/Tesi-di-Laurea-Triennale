
import matplotlib.pyplot as plt
import contextily as cx

# Helper class for printing multi-layer geopandas maps
class CustomMap(): 

    # used to get the initial map object, any layer can be modified after creation
    def __init__(self, bounds : list = None, basemap : bool = True):
        self.data_layers : list = []
        self.alpha_layers : list = []
        self.color_layers : list = []
        self.bounds : list = bounds
        self.basemap : bool = basemap
        self.label = None

    # The method adds a layer to the map, currently there is no way of changing the order of layers 
    # The first layer is also the first displayed
    def add_layer(self, data, alpha=1.0, color=None): 
        self.data_layers.append(data)
        self.alpha_layers.append(alpha)
        self.color_layers.append(color)

    # The method draws the map
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

    # The method allows to set new boundaries of the map
    def set_bounds(self, bounds : list): 
        if len(bounds) == 4 or bounds is None: 
            self.bounds = bounds

    # The method allows to set a new basemap    
    def set_basemap(self, basemap : bool): 
        self.basemap = basemap

    # The method allows to set a new label
    def set_label(self, label):  
        self.label = label

    # The method clears all the layers in the map
    def clear(self): 
        self.alpha_layers = []
        self.data_layers = []
        self.bounds = None