""" Plot optimization results from spe10."""
import pandas as pd
from util.plot_opt import PlotOpt

if __name__ == "__main__":
    # Read csv
    opt_df = pd.read_csv("./results/results_ml.csv", sep='\t')
    hf_df = pd.read_csv("./results/results_hf.csv", sep='\t')

    # Crea plot optimization
    plot_opt = PlotOpt(opt_df, hf_df, restore_npv=True)
    plot_opt.plot_controls()
