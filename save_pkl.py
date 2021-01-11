""" Create plots for reservoir production."""
import os
from util.simulate import Simulation

if __name__ == "__main__":
    # Create simulation instance
    reservoir = Simulation()

    # Define the control
    # controls = reservoir.nominal
    controls = None

    # Run PyMEX
    results = reservoir(controls)

    # Remove extension
    filename, _ = os.path.splitext(results.tpl)

    # Save Results
    filename = filename + '.pkl'
    save_path = os.path.join(results.run_path, filename)
    results.data.to_pickle(save_path)
    results.data.to_pickle("./results")
