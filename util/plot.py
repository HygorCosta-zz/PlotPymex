""" Plot simulation production. """
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib
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

    @staticmethod
    def set_style_2():
        """ Set style 2"""
        plt.style.use(['seaborn-white', 'seaborn-paper'])
        matplotlib.rc("font", family="Times New Roman")

    @staticmethod
    def set_size(fig):
        """ Set size and layout."""
        plt.tight_layout()

    def plot_perm_2d(self):
        """ Plot 2D permeability."""
        fig, ax = plt.subplots()
        perm = np.load('spe10_fperm.npy')
        sns.heatmap(perm, xticklabels=False, yticklabels=False)
        self.set_style_2()
        fig.set_size_inches(6, 3)
        plt.tight_layout()
        plt.savefig('spe10_fine_perm.eps', format='eps')

    def npv_boxplot(self):
        """ Plot npv boxplot."""
        fig, ax = plt.subplots()
        npv = -1 * np.load('npv.npy')
        w3 = pd.DataFrame({'npv': npv[:, 0], 'Models': 'W3'})
        w2 = pd.DataFrame({'npv': npv[:, 1], 'Models': 'W2'})
        w1 = pd.DataFrame({'npv': npv[:, 2], 'Models': 'W1'})
        hf = pd.DataFrame({'npv': npv[:, 3], 'Models': 'HF'})
        df = pd.concat([w3, w2, w1, hf]).reset_index(drop=True)
        ax = sns.boxplot(x="Models", y="npv", data=df, showfliers=False)
        ax.set(xlabel='Models', ylabel=r'NPV ($1 \times 10^{-6}}$)')
        self.set_style_2()
        fig.set_size_inches(6, 3)
        plt.tight_layout()
        plt.savefig('npv_boxplt_spe10.eps', format='eps')

   # def plot_cum_oil_prod(self):
   #      """ Plot cumulative oil production."""
   #      fig, ax = plt.subplots()
   #      axes = sns.lineplot(x='time',
   #                          y='cum_op',
   #                          data=self.dframe,
   #                          style='Models',
   #                          hue='Models')
   #      axes.set(xlabel='Time (days)',
   #               ylabel='Cumulative Oil Production (bbl)')
   #      self.set_style_2()
   #      fig.set_size_inches(6, 3)
   #      plt.tight_layout()
   #      plt.savefig('spe10_unif_cop.eps', format='eps')

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
                       position=[0.75, 0.3, 0.2, 0.2],
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
        self.set_style_2()
        fig.set_size_inches(6, 3)
        plt.tight_layout()
        plt.savefig('egg_cum_oil_models.eps', format='eps')

    def plot_cum_oil_prod_zoom_spe(self):
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
                       ylim=[4000, 50000])
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
        self.set_style_2()
        fig.set_size_inches(6, 3)
        plt.tight_layout()
        plt.savefig('spe10_cum_oil_models.eps', format='eps')

    def plot_oil_rate(self):
        """ Plot Oil rate production."""
        fig, ax = plt.subplots()
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
        fig, ax = plt.subplots()
        axes = sns.lineplot(x='time',
                            y='cum_gp',
                            data=self.dframe,
                            style='Models',
                            hue='Models')
        axes.set(xlabel='Time (days)',
                 ylabel='Cumulative Gas Production ($ft^3$)')
        self.set_style_2()
        fig.set_size_inches(6, 3)
        plt.tight_layout()
        plt.savefig('spe10_cum_gas_models.eps', format='eps')

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
                       position=[0.75, 0.3, 0.2, 0.2],
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
        self.set_style_2()
        fig.set_size_inches(6, 3)
        plt.tight_layout()
        plt.savefig('spe10_cum_gas_models_2.eps', format='eps')

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
        fig, ax = plt.subplots()
        axes = sns.lineplot(x='time',
                            y='cum_wp',
                            data=self.dframe,
                            style='Models',
                            hue='Models',
                            ax=ax)
        axes.set(xlabel='Time (days)',
                 ylabel='Cumulative Water Production ($m^3$)')
        ax2 = plt.axes([0.2, 0.4, .2, .2],
                       position=[0.75, 0.3, 0.2, 0.2],
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
        self.set_style_2()
        fig.set_size_inches(6, 3)
        plt.tight_layout()
        plt.savefig('egg_cum_water_layers.eps', format='eps')

    def cum_op_all_wells(self):
        """ Plot the cumulative wells production
        for each well."""
        fig, axes = plt.subplots(2, 2, sharex=True, sharey=True)

        # Prod 1
        ax1 = sns.lineplot(ax=axes[0, 0], x='time', y='cum_op_p1',
                           data=self.dframe, style='Models',
                           hue='Models')
        axes[0, 0].set_title('PROD1')
        ax1.get_legend().remove()

        # Prod 2
        ax2 = sns.lineplot(ax=axes[0, 1], x='time', y='cum_op_p2', data=self.dframe, style='Models',
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

    def oil_rate_all_wells(self):
        """ Plot the oil rate wells production
        for each well."""
        fig, axes = plt.subplots(2, 2, sharex=True, sharey=True)

        # Prod 1
        ax1 = sns.lineplot(ax=axes[0, 0], x='time', y='cum_or_p1',
                           data=self.dframe, style='Models',
                           hue='Models')
        axes[0, 0].set_title('PROD1')
        ax1.get_legend().remove()

        # Prod 2
        ax2 = sns.lineplot(ax=axes[0, 1], x='time', y='cum_or_p2',
                           data=self.dframe, style='Models',
                           hue='Models')
        axes[0, 1].set_title('PROD2')
        ax2.get_legend().remove()

        # Prod 3
        ax3 = sns.lineplot(ax=axes[1, 0], x='time', y='cum_or_p3',
                           data=self.dframe, style='Models',
                           hue='Models')
        axes[1, 0].set_title('PROD3')
        ax3.get_legend().remove()

        # Prod 4
        ax4 = sns.lineplot(ax=axes[1, 1], x='time', y='cum_or_p4',
                           data=self.dframe, style='Models',
                           hue='Models')
        axes[1, 1].set_title('PROD4')
        ax4.get_legend().remove()

        for iax in axes.flat:
            iax.set(xlabel='Time (days)',
                    ylabel='Oil Rate ($m^3 / day$)')
        plt.tight_layout()
        fig.subplots_adjust(bottom=0.18)
        fig.legend(labels=['HF', 'U1', 'U2', 'U3',
                           'W1', 'W2', 'W3'], loc="lower center",
                   ncol=4, fontsize='small')
        plt.show()
