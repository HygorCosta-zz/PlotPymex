""" Plot Layers comparation in Egg Model."""
import pandas as pd
from util.plot import PlotPymex
if __name__ == "__main__":
    # Models
    orig = pd.read_pickle('./results/egg/layers/orig.pkl')
    lay_4 = pd.read_pickle('./results/egg/layers/4lay.pkl')
    lay_3 = pd.read_pickle('./results/egg/layers/3lay.pkl')
    lay_2 = pd.read_pickle('./results/egg/layers/2lay.pkl')
    concatenated = pd.concat([orig.assign(Models='HF'),
                              lay_4.assign(Models='4L'),
                              lay_3.assign(Models='3L'),
                              lay_2.assign(Models='2L')])

    # # Create a instance of PlotPymex class
    breakpoint()
    plot = PlotPymex(concatenated)

    # Plot cumulative oil production
    plot.plot_cum_oil_prod_zoom()
