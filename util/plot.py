""" Plot simulation production. """
# import pandas as pd
import numpy as np
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

        # Axes style
        sns.axes_style("whitegrid")

    @staticmethod
    def set_size(fig):
        """ Set size and layout."""
        fig.set_size_inches(6, 3)
        plt.tight_layout()

    def plot_cum_oil_prod(self):
        """ Plot cumulative oil production."""
        axes = sns.lineplot(x='time',
                            y='cum_op',
                            data=self.dframe,
                            style='Models',
                            hue='Models')
        axes.set(xlabel='Time (days)',
                 ylabel='Cumulative Oil Production (bbl)')
        self.set_size(plt.gcf())
        plt.show()

    def plot_cum_oil_prod_zoom(self):
        """ Plot cumulative oil production with
        zoom in [7000, 7300] x."""
        fig, ax = plt.subplots()
        axes = sns.lineplot(x='time',
                            y='cum_op',
                            data=self.dframe,
                            style='Models',
                            hue='Models',
                            ax=ax)
        axes.set(xlabel='Time (days)',
                 ylabel='Cumulative Oil Production (bbl)')
        ax2 = plt.axes([0.2, 0.4, .2, .2],
                       position=[0.5, 0.4, 0.2, 0.2],
                       ylim=[41000, 49000])
        axes2 = sns.lineplot(x='time',
                             y='cum_op',
                             data=self.dframe,
                             style='Models',
                             hue='Models',
                             ax=ax2)
        # ADDED: Remove labels.
        axes2.set_ylabel('')
        axes2.set_xlabel('')
        plt.legend([], [], frameon=False)
        axes2.set_title('Zoom')
        axes2.set_xlim([7000, 7300])
        self.set_size(plt.gcf())
        plt.show()

    def plot_oil_rate(self):
        """ Plot Oil rate production."""
        axes = sns.lineplot(x='time',
                            y='prod1_or',
                            data=self.dframe,
                            style='Models',
                            hue='Models')
        axes.set(xlabel='Time (days)',
                 ylabel='Oil rate (bbl / day)')
        self.set_size(plt.gcf())
        plt.show()

    def plot_cum_gas_prod(self):
        """ Plot cumulative gas production."""
        axes = sns.lineplot(x='time',
                            y='cum_gp',
                            data=self.dframe,
                            style='Models',
                            hue='Models')
        axes.set(xlabel='Time (days)',
                 ylabel='Cumulative Gas Production ($ft^3$)')
        self.set_size(plt.gcf())
        plt.show()

    def plot_ave_pressure(self):
        """ Plot average reservoi pressure."""
        axes = sns.lineplot(x='time',
                            y='pres',
                            data=self.dframe,
                            style='Models',
                            hue='Models')
        axes.set(xlabel='Time (days)',
                 ylabel='Average reservoir pressure (psia)')
        self.set_size(plt.gcf())
        plt.show()
