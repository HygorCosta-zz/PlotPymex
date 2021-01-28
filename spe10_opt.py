""" Plot optimization results from spe10."""
import pandas as pd
from util.plot_opt import PlotOpt

if __name__ == "__main__":
    # Read csv
    hf_df = pd.read_csv("./results/spe10/results_spe_ori.csv", sep='\t')
    # hf_df = pd.read_csv("./results/egg/results_hf.csv", sep='\t')
    # hf_df = pd.read_csv("./results/egg/results_orig_egg2.csv", sep='\t')
    # opt_df = pd.read_csv("./results/egg/results_wav.csv", sep='\t')
    opt_df = pd.read_csv("./results/spe10/results_spe_wav.csv", sep='\t')

    # Crea plot optimization
    plot_opt = PlotOpt(opt_df, hf_df, restore_npv=True)
    plot_opt.opt_history_ori()
