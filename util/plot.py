""" Plot simulation production. """
# import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.legend import _get_legend_handles_labels


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
                 ylabel='Cumulative Oil Production ($m^3$)')
        ax2 = plt.axes([0.2, 0.4, .2, .2],
                       position=[0.6, 0.3, 0.2, 0.2],
                       ylim=[470000, 520000])
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
        axes2.set_xlim([3000, 3600])
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

    def plot_cum_gas_prod_zoom(self):
        """ Plot cumulative gas production."""
        fig, ax = plt.subplots()
        axes = sns.lineplot(x='time',
                            y='cum_gp',
                            data=self.dframe,
                            style='Models',
                            hue='Models',
                            ax=ax)
        axes.set(xlabel='Time (days)',
                 ylabel='Cumulative Gas Production ($ft^3$)')
        fig.tight_layout()
        ax2 = plt.axes([0.2, 0.4, .2, .2],
                       position=[0.8, 0.4, 0.2, 0.2],
                       ylim=[1.45e6, 1.55e6])
        axes2 = sns.lineplot(x='time',
                             y='cum_gp',
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

    def plot_cum_wat_prod_zoom(self):
        """ Plot cumulative gas production."""
        axes = sns.lineplot(x='time',
                            y='cum_wp',
                            data=self.dframe,
                            style='Models',
                            hue='Models')
        axes.set(xlabel='Time (days)',
                 ylabel='Cumulative Water Production ($m^3$)')
        ax2 = plt.axes([0.2, 0.4, .2, .2],
                       position=[0.7, 0.25, 0.2, 0.2],
                       ylim=[1.12e6, 1.24e6])
        axes2 = sns.lineplot(x='time',
                             y='cum_wp',
                             data=self.dframe,
                             style='Models',
                             hue='Models',
                             ax=ax2)
        ax2.set_title('Zoom')
        ax2.set_xlim([3400, 3600])
        # ADDED: Remove labels.
        axes2.set_ylabel('')
        axes2.set_xlabel('')
        plt.legend([], [], frameon=False)
        self.set_size(plt.gcf())
        plt.show()

    def cum_op_all_wells(self):
        """ Plot the cumulative wells production
        for each well."""
        fig, axes = plt.subplots(2, 2, sharex=True, sharey=True)

        # Prod 1
        breakpoint()
        ax1 = sns.lineplot(ax=axes[0, 0], x='time', y='cum_op_p1',
                           data=self.dframe, style='Models',
                           hue='Models')
        axes[0, 0].set_title('PROD1')
        ax1.get_legend().remove()

        # Prod 2
        ax2 = sns.lineplot(ax=axes[0, 1], x='time', y='cum_op_p2',
                           data=self.dframe, style='Models',
                           hue='Models')
        axes[0, 1].set_title('PROD2')
        ax2.get_legend().remove()

        # Prod 3
        ax3 = sns.lineplot(ax=axes[1, 0], x='time', y='cum_op_p3',
                           data=self.dframe, style='Models',
                           hue='Models')
        axes[1, 0].set_title('PROD3')
        ax3.get_legend().remove()

        # Prod 4
        ax4 = sns.lineplot(ax=axes[1, 1], x='time', y='cum_op_p4',
                           data=self.dframe, style='Models',
                           hue='Models')
        axes[1, 1].set_title('PROD4')
        ax4.get_legend().remove()

        for iax in axes.flat:
            iax.set(xlabel='Time (days)',
                    ylabel='Cumulative Oil Production ($m^3$)')
        plt.tight_layout()
        fig.subplots_adjust(bottom=0.18)
        fig.legend(labels=['HF', 'U1', 'U2', 'U3',
                           'W1', 'W2', 'W3'], loc="lower center",
                   ncol=4, fontsize='small')
        plt.show()
