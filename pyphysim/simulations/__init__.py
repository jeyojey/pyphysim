#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Module containing useful classes to implement Monte Carlo simulations.

The main class for Monte Carlo simulations is the :class:`.runner.SimulationRunner`
class, but a few other classes are also implemented to handle simulation
parameters and simulation results.

More specifically, the :mod:`.simulations` module implements the classes:
 - :class:`.runner.SimulationRunner`
 - :class:`.parameters.SimulationParameters`
 - :class:`.results.SimulationResults`
 - :class:`.results.Result`

For a description of how to implement Monte Carlo simulations using the
classes defined in the :mod:`.simulations` module see the section
:ref:`implementing_monte_carlo_simulations`.
"""

# pylint: disable=W0614,W0401
from .parameters import *
from .runner import *
from .results import *
