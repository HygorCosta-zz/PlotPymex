""" Plot optimization results."""
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from util.simulate import Simulation


class PlotOpt:

    """Plot Optimization Results."""

    def __init__(self, mult_df, hf_df, restore_npv=True):
        """

        Parameters
        ----------
        opt_frame: pandas dataframe


        """
        self.data = mult_df
        self.high = hf_df
        self.restore_npv = restore_npv
        self.x_level = self.groupby_level()
        self.npv_level = self.evaluate_x_level()
        breakpoint()
        self.set_style()

    @staticmethod
    def stringtoarray(str_row):
        """ Change string in numpy array. """
        row = np.fromstring(str_row[1:-1], sep=' ')
        return row

    def groupby_level(self):
        """ Select the first design variable position
        in each level of the optimization."""
        first = self.data.groupby('opt_level').first()['x_c']
        arr = np.empty((0, 6), int)
        last = self.data['x_s'].iloc[-1][1:-1]
        last = np.fromstring(last, sep=' ')
        arr = np.vstack((arr, last))
        return arr

    def evaluate_x_level(self):
        """ Evaluate the high fidelity values of the
        x level positions."""
        if self.restore_npv:
            npv = -1 * np.load('npv_level.npy')
        else:
            reservoir = Simulation()
            # High Fidelity template
            reservoir.res_param['run_folder'] = False
            reservoir.template = 'mxspe10.tpl'
            breakpoint()
            # npv = reservoir(self.x_level[0])
            npv = reservoir.npv(self.x_level, pool_size=4)
            np.save('npv_level.npy', npv)
        return npv

    @ staticmethod
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
            "font.serif": ["Times", "Palatino", "serif"]})

        # Axes style
        sns.axes_style("whitegrid")

    @ staticmethod
    def set_size(fig):
        """ Set size and layout."""
        fig.set_size_inches(6, 3)
        plt.tight_layout()

    def plot_multilevel_npv(self):
        """ Plot multilevel optimization iterations."""
        breakpoint()
        npv_level = self.npv_level
        fob_c = -1 * self.data.fob_c.values
        plt.plot(np.arange(20), fob_c[:20], label="W3", marker='s')
        plt.plot(np.arange(20, 29), fob_c[20:29], label="W2", marker='*')
        plt.plot(np.arange(29, 34), fob_c[29:34], label="W1", marker='d')
        plt.plot([0, 19, 28, 33], npv_level, 'kx', label='HF points')
        plt.ylabel(r"NPV ($1 \times 10^{-6}$)")
        plt.xlabel('Iterations')
        self.set_size(plt.gcf())
        plt.legend(title="Models")
        plt.show()

    def plot_time_npv(self):
        """ Plot time comparation between hf optimization and
        multilevel optimization."""
        npv_level = self.npv_level
        breakpoint()
        fob_c = -1 * self.data.fob_c.values
        fob_hf = -1 * self.high.fob_c.values
        time_lf = self.data['time-spend'].values
        time_hf = self.high['time-spend'].values
        # plt.plot(time_lf[:20], fob_c[:20], label="W3", marker='s')
        # plt.plot(time_lf[20:29], fob_c[20:29], label="W2", marker='*')
        # plt.plot(time_lf[29:34], fob_c[29:34], label="W1", marker='d')
        plt.plot(time_lf[[0, 19, 28, 33]], npv_level, 'k--x', label='HF-ML')
        plt.plot(time_hf, fob_hf, label="HF-SL", marker='h')
        plt.ylabel(r"NPV ($1 \times 10^{-6}$)")
        plt.xlabel('CPU time (seconds)')
        self.set_size(plt.gcf())
        plt.legend(title="Models")
        plt.show()

    def plot_controls(self):
        """ Plot control for each cycle. """
        times = [0, 2433, 4687, 7300]
        rate_max = 500
        breakpoint()
        clf = self.stringtoarray(self.data['x_s'].iloc[-1])
        prod_lf = clf[::2] * rate_max
        inj_lf = clf[1::2] * rate_max
        chf = self.stringtoarray(self.data['x_c'].iloc[-1])
        prod_hf = chf[::2] * rate_max
        inj_hf = chf[1::2] * rate_max

        # Plot steps
        plt.step(times, prod_lf[[0, 0, 1, 2]], 'ko-', label='ML-PROD')
        plt.step(times, inj_lf[[0, 0, 1, 2]], 'ko--', label='ML-INJ')
        plt.step(times, prod_hf[[0, 0, 1, 2]], 'bd-', label='HF-PRO')
        plt.step(times, inj_hf[[0, 0, 1, 2]], 'bd--', label='HF-INJ')
        plt.grid(axis='x', color='0.95')
        plt.ylabel(r"Maximum Gas Rate (ft$^3$)")
        plt.xlabel('Time (days)')
        plt.legend(title='Model-Well')
        plt.xlim = (0, 7300)
        plt.show()
