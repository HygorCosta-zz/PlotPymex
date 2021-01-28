""" Compare results SPE."""
import pandas as pd
from util.plot import PlotPymex

if __name__ == "__main__":
    # Models
    hfid = pd.read_pickle('./results/spe10/old/mxspe010.pkl')
    uni1 = pd.read_pickle('./results/spe10/old/mxspe010_ham_1.pkl')
    uni2 = pd.read_pickle('./results/spe10/old/mxspe010_ham_2.pkl')
    uni3 = pd.read_pickle('./results/spe10/old/mxspe010_ham_3.pkl')
    wav1 = pd.read_pickle('./results/spe10/old/mxspe010_wav_1.pkl')
    wav2 = pd.read_pickle('./results/spe10/old/mxspe010_wav_2.pkl')
    wav3 = pd.read_pickle('./results/spe10/old/mxspe010_wav_3.pkl')
    concatenated = pd.concat([hfid.assign(Models='HF'),
                              uni1.assign(Models='U1'),
                              uni2.assign(Models='U2'),
                              uni3.assign(Models='U3'),
                              wav1.assign(Models='W1'),
                              wav2.assign(Models='W2'),
                              wav3.assign(Models='W3')])

    # # Create a instance of PlotPymex class
    plot = PlotPymex(concatenated)

    # Plot cumulative oil production
    plot.npv_boxplot()
