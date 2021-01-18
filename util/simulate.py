""" Simulate reservoi class. """
import yaml
import numpy as np
from PyMEX.utilits.ManiParam import PyMEX
# import multiprocessing as mp


class Simulation:

    """ Reservoir parameters for simulation."""

    def __init__(self, reservoir_config, restore_file=False):
        """ Reservoir parameters."""
        self.reservoir_config = reservoir_config
        self.restore_file = restore_file
        self.res_param = self.reservoir_parameters()
        self.nominal = self.x_nominal()
        self.num_simulations = 0
        self.template = self.res_param['template'][0]

    def reservoir_parameters(self):
        """ Return the reservoir configuration."""
        with open(self.reservoir_config) as file:
            res_param = yaml.load(file, Loader=yaml.FullLoader)
        return res_param

    def x_nominal(self):
        """ Determine the nominal controls for the wells. """

        def _prod_nom(res_param):
            """ Producer norm max plat."""
            plat_prod = res_param["max_plat_prod"]
            prod_rate = res_param["max_rate_prod"]
            nb_prod = res_param["nb_prod"]
            prod_total = prod_rate * nb_prod
            x_prod = plat_prod / prod_total
            if x_prod > 1:
                x_prod = 1
            return x_prod

        def _inj_nom(res_param):
            """ Producer norm max plat."""
            plat_inj = res_param["max_plat_inj"]
            inj_rate = res_param["max_rate_inj"]
            nb_inj = res_param["nb_inj"]
            inj_total = inj_rate * nb_inj
            x_inj = plat_inj / inj_total
            if x_inj > 1:
                x_inj = 1
            return x_inj

        nb_prod = self.res_param["nb_prod"]
        nb_inj = self.res_param["nb_inj"]
        if self.res_param['max_plat_prod']:
            nom_prod = _prod_nom(self.res_param)
            nom_inj = _inj_nom(self.res_param)
        else:
            nom_prod = np.ones(nb_prod)
            nom_inj = np.ones(nb_inj)
        rate_cycle = np.repeat([nom_prod, nom_inj], [nb_prod, nb_inj])
        return np.tile(rate_cycle, self.res_param["nb_cycles"])

    def run_parallel(self, control):
        """ Run PyMEX with Pool."""
        model = PyMEX(control,
                      self.template,
                      self.restore_file,
                      self.res_param)
        return model.npv

    def npv(self, controls, pool_size):
        """ Net present value of controls. """
        with mp.Pool(pool_size) as proc:
            npv = proc.map(self.run_parallel, controls)
        return np.array(npv)

    def restore_prod(self, restore_file):
        """ Restore results."""
        model = PyMEX(None,
                      self.template,
                      self.restore_file,
                      self.res_param)
        return model

    def __call__(self, controls):
        """High fidelity model."""
        if not isinstance(controls, np.ndarray):
            controls = np.array(controls)
        model = PyMEX(controls,
                      self.template,
                      self.restore_file,
                      self.res_param)
        return model
