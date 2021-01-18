""" Compare results."""
import pandas as pd
from util.plot import PlotPymex

if __name__ == "__main__":
    # Models
    hfid = pd.read_pickle('./results/egg/layers/Egg_orig_wells.pkl')
    uni1 = pd.read_pickle('./results/egg/ari/Egg_ari_1_wells.pkl')
    uni2 = pd.read_pickle('./results/egg/ari/Egg_ari_2_wells.pkl')
    uni3 = pd.read_pickle('./results/egg/ari/Egg_ari_3_wells.pkl')
    wav1 = pd.read_pickle('./results/egg/wav/Egg_wav_1_wells.pkl')
    wav2 = pd.read_pickle('./results/egg/wav/Egg_wav_2_wells.pkl')
    wav3 = pd.read_pickle('./results/egg/wav/Egg_wav_3_wells.pkl')
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
    plot.cum_op_all_wells()
