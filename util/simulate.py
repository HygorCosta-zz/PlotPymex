""" Simulate reservoi class. """
import yaml
import numpy as np
from PyMEX.utilits.ManiParam import PyMEX


class Simulation:

    """ Reservoir parameters for simulation."""

    def __init__(self):
        """ Reservoir parameters."""
        self.res_param = self.reservoir_parameters()
        self.nominal = self.x_nominal()
        self.num_simulations = 0
        self.template = self.res_param['template'][0]

    @staticmethod
    def reservoir_parameters():
        """ Return the reservoir configuration."""
        with open('./PyMEX/reservoir_config_ml_spe10.yaml') as file:
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

    def __call__(self, controls):
        """High fidelity model."""
        if not isinstance(controls, np.ndarray):
            controls = np.array(controls)
        model = PyMEX(controls, self.template, self.res_param)
        return model
