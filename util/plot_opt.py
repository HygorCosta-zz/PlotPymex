""" Plot optimization results."""
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib
from util.simulate import Simulation


class PlotOpt:

    """Plot Optimization Results."""

    def __init__(self, mult_df, hf_df=None, restore_npv=True):
        """

        Parameters
        ----------
        opt_frame: pandas dataframe


        """
        self.data = mult_df
        self.high = hf_df
        self.restore_npv = restore_npv
        self.x_level = []
        self.time = []
        self.nfe = []
        self.groupby_level()
        if not restore_npv:
            self.npv_level = self.evaluate_x_level()

    @staticmethod
    def set_style_2():
        """ Set style 2"""
        plt.style.use(['seaborn-white', 'seaborn-paper'])
        matplotlib.rc("font", family="Times New Roman")

    def set_style(self):
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
    def stringtoarray(str_row):
        """ Change string in numpy array. """
        row = np.fromstring(str_row[1:-1], sep=' ')
        return row

    def groupby_level(self):
        """ Select the first design variable position
        in each level of the optimization."""
        arr = np.empty((0, 6), int)
        breakpoint()
        first = self.data.groupby('opt_level').first()['x_c']
        self.time = self.data.groupby('opt_level').last()['time-spend']
        self.nfe = self.data.groupby('opt_level').last()['nfev-hf']
        for row in first:
            np_first = self.stringtoarray(row)
            arr = np.vstack((arr, np_first))
        last = self.data['x_s'].iloc[-1][1:-1]
        last = np.fromstring(last, sep=' ')
        self.x_level = np.vstack((arr, last))

    def group_xcenter(self):
        """ Get all x center values."""
        arr = np.empty((0, 6), int)
        xct = self.data['x_c']
        for row in xct:
            row = self.stringtoarray(row)
            arr = np.vstack((arr, row))
        return arr

    def group_xstar(self):
        """ Get all x center values."""
        arr = np.empty((0, 6), int)
        xct = self.data['x_c']
        for row in xct:
            row = self.stringtoarray(row)
            arr = np.vstack((arr, row))
        return arr

    def evaluate_x_level(self):
        """ Evaluate the high fidelity values of the
        x level positions."""
        if self.restore_npv:
            npv = -1 * np.load('npv_level_spe10_wav.npy')
        else:
            # Create simulation instance
            controls = self.group_xcenter()
            breakpoint()
            reservoir_config = './PyMEX/reservoir_config_ml.yaml'
            reservoir = Simulation(reservoir_config)
            # High Fidelity template
            reservoir.res_param['run_folder'] = False
            reservoir.template = reservoir.res_param['original']
            npv = reservoir.npv(controls, pool_size=4)
            np.save('npv_wav.npy', npv)
            breakpoint()
        return npv

    def plot_multilevel_sea_spe10(self):
        """ Plot multilevel seaborn scheme."""
        fig, ax = plt.subplots()
        sns.lineplot(x=self.data.index,
                     y=-1 * self.data['fob_c'],
                     data=self.data, style='opt_level',
                     hue='opt_level',
                     palette="tab10",
                     markers=True,
                     ax=ax, legend=False)
        index = [0, 19, 29, 34]
        npv_level = [1.7147, 1.8178, 1.8147, 1.8148]
        sns.scatterplot(x=index, y=npv_level, marker='D',
                        color='black', ax=ax)
        plt.legend(title='Models', labels=["W3", "W2", "W1", "HF"])
        plt.ylabel(r"NPV ($1 \times 10^{-6}$)")
        plt.xlabel('Iterations')
        self.set_style_2()
        fig.set_size_inches(6, 3)
        plt.tight_layout()
        plt.savefig('ml_opt_spe10.eps', format='eps')

    def plot_multilevel_sea_egg(self):
        """ Plot multilevel seaborn scheme."""
        fig, ax = plt.subplots()
        sns.lineplot(x=self.data.index,
                     y=-1 * self.data['fob_c'],
                     data=self.data, style='opt_level',
                     hue='opt_level',
                     palette="tab10",
                     markers=True,
                     ax=ax, legend=False)
        index = [0, 19, 29, 34]
        npv_level = [33.8814, 46.2205, 47.9874, 48.3924]
        sns.scatterplot(x=index, y=npv_level, marker='D',
                        color='black', ax=ax)
        plt.legend(title='Models', labels=["W3", "W2", "W1", "HF"])
        plt.ylabel(r"NPV ($1 \times 10^{-6}$)")
        plt.xlabel('Iterations')
        self.set_style_2()
        fig.set_size_inches(6, 3)
        plt.tight_layout()
        plt.savefig('ml_opt_egg.eps', format='eps')

    def plot_multilevel_npv(self):
        """ Plot multilevel optimization iterations."""
        npv_level = self.npv_level
        fob_c = -1 * self.data.fob_c.values
        plt.plot(np.arange(20), fob_c[:20], label="W3", marker='s')
        plt.plot(np.arange(20, 30), fob_c[20:30], label="W2", marker='*')
        plt.plot(np.arange(30, 35), fob_c[30:35], label="W1", marker='d')
        plt.plot([0, 19, 29, 34], npv_level, 'kx', label='HF points')
        plt.ylabel(r"NPV ($1 \times 10^{-6}$)")
        plt.xlabel('Iterations')
        plt.legend(title="Models")
        plt.tight_layout()
        plt.show()

    def plot_time_npv(self):
        """ Plot time comparation between hf optimization and
        multilevel optimization."""
        npv_level = self.npv_level
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
        plt.legend(title="Models")
        plt.tight_layout()
        plt.show()

    def plot_controls(self):
        """ Plot control for each cycle. """
        fig, ax = plt.subplots()
        times = [0, 2433, 4687, 7300]
        rate_max = 500
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
        self.set_style_2()
        fig.set_size_inches(6, 3)
        plt.tight_layout()
        plt.savefig('spe10_controls.eps', format='eps')

    def plt_heatmap_controls(self):
        """ Plot heatmap controls."""
        fig, ax = plt.subplots()
        reservoir_config = './PyMEX/reservoir_config_ml.yaml'
        reservoir = Simulation(reservoir_config)
        ncycle = reservoir.res_param['nb_cycles']
        nprod = reservoir.res_param['nb_prod']
        ninj = reservoir.res_param['nb_inj']
        nwells = nprod + ninj
        cycles = ['1st', '2nd', '3rd']
        x_star = self.x_level[-1].reshape((ncycle, nwells)).T
        prod_name = [f"PROD{i+1}" for i in range(nprod)]
        inj_name = [f"INJECT{i+1}" for i in range(ninj)]
        wells_names = prod_name + inj_name
        dataf = pd.DataFrame(data=x_star)
        dataf.columns = cycles
        dataf.index = wells_names
        sns.heatmap(dataf, ax=ax)
        plt.ylabel("Wells")
        plt.xlabel("Control Cycles")
        self.set_style_2()
        fig.set_size_inches(6, 3)
        plt.tight_layout()
        plt.savefig('control_heatmap.eps', format='eps')

    def opt_history(self):
        """ Plot optimization history of low fidelity and
        high fidelity. """
        breakpoint()
        fig, ax = plt.subplots()
        wav_data = np.load('npv_egg_orig_wav.npy')
        plt.plot(-1 * wav_data, marker='o')
        plt.plot(-1 * self.high['fob_c'], marker='+')
        plt.legend(title='Models', labels=["ML-WAV", "SL-HF"])
        plt.ylabel(r"NPV ($1 \times 10^{-6}$)")
        plt.xlabel('Iterations')
        self.set_style_2()
        fig.set_size_inches(6, 3)
        plt.tight_layout()
        plt.savefig('opt_hist_egg.eps', format='eps')

    def opt_history_ori(self):
        """ Plot optimization history of low fidelity and
        high fidelity. """
        fig, ax = plt.subplots()
        wav_data = np.load('npv_level_spe10_wav2.npy')
        breakpoint()
        high_data = -1 * self.high['fob_c'].values
        plt.plot(-1 * wav_data, marker='o')
        plt.plot(high_data, marker='+')
        plt.legend(title='Models', labels=["WAV", "HF"])
        plt.ylabel(r"NPV ($1 \times 10^{-6}$)")
        plt.xlabel('Iterations')
        self.set_style_2()
        fig.set_size_inches(6, 3)
        plt.tight_layout()
        plt.savefig('tr_upd_spe10.eps', format='eps')
