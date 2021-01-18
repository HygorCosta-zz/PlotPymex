""" Create plots for reservoir production."""
import os
from util.simulate import Simulation

if __name__ == "__main__":
    # Create simulation instance
    RESERVOIR_CONFIG = './PyMEX/reservoir_config_ml.yaml'
    reservoir = Simulation(RESERVOIR_CONFIG, restore_file=False)

    # Define the control
    # CONTROLS = reservoir.nominal
    CONTROLS = None

    # Run PyMEX
    results = reservoir(CONTROLS)

    # Remove extension
    filename, _ = os.path.splitext(results.tpl)

    # Save Results
    if reservoir.res_param['wells_resul']:
        filename = filename + '_wells'
    filename = filename + '.pkl'
    save_path = os.path.join(results.run_path, filename)
    results.prod.to_pickle(save_path)
