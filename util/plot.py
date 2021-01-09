""" Plot simulation production. """
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


class PlotPymex:

    """Docstring for PlotPymex. """

    def __init__(self, dataframe):
        """Create fancy plot productions for the dataframe

        Parameters
        ----------
        dataframe: pandas.DataFrame instance
            Include cumulative production, injection,
            wells rates and pressure.

        """
        self.dframe = dataframe
        self.set_style()

    @staticmethod
    def set_style():
        """ Set seaborn style."""
        # This sets reasonable defaults for font size for
        # a figure that will go in a paper
        sns.set_context("paper")

        # Set the font to be serif, rather than sans
        sns.set(font='serif')

        # Make the background white, and specify the
        # specific font family
        sns.set_style("white", {
            "font.family": "serif",
            "font.serif": ["Times", "Palatino", "serif"]
        })

    @staticmethod
    def set_size(fig):
        """ Set size and layout."""
        fig.set_size_inches(6, 3)
        plt.tight_layout()

    def plot_cum_oil_prod(self):
        """ Plot cumulative oil production."""
        breakpoint()
        axes = sns.lineplot(x='time', y='cum_op',
                            data=self.dframe)
        axes.set(xlabel='Time (days)',
                 ylabel='Cumulative Oil Production (bbl)')
        self.set_size(plt.gcf())
        plt.show()
