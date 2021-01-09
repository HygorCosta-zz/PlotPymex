""" Create plots for reservoir production."""
from util.simulate import Simulation
from util.plot import PlotPymex

if __name__ == "__main__":
    # Create simulation instance
    reservoir = Simulation()

    # Define the control
    controls = reservoir.nominal

    # Run PyMEX
    results = reservoir(controls)

    # Create a instance of PlotPymex class
    plot = PlotPymex(results.data)

    # Plot cumulative oil production
    breakpoint()
    plot.plot_cum_oil_prod()
