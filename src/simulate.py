# simulate.py

import numpy as np
from src.model import step
from src.parameters import get_parameters

def simulate_generations(
    generations=10,
    T=30,
    dt=0.1,
    inheritance=0.6
):
    """
    Simulates multiple generations and returns Parkinson incidence.
    """

    incidence = []
    epi_inherited = 0.0

    for g in range(1, generations + 1):

        nicotine_on = g <= 5
        params = get_parameters(nicotine_on)

        # Initial state
        state = np.array([
            0.9,   # S
            0.1,   # E
            0.0,   # I
            0.0,   # R
            0.0,   # Dopamine
            epi_inherited  # Epigenetic memory
        ])

        inc = 0.0

        for _ in range(int(T / dt)):
            state = step(state, params, dt)

            S, E, I, R, D, epi = state
            sigma = params["sigma0"] / (1 + params["alpha"] * D + params["beta_epi"] * epi)
            inc += sigma * E * dt

        incidence.append(inc)

        # Epigenetic inheritance
        epi_inherited = inheritance * state[5]

    return incidence
