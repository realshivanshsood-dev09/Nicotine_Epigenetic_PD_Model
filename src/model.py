# model.py

import numpy as np

def step(state, params, dt):
    """
    Single Euler–Maruyama step of the model.
    """

    S, E, I, R, D, epi = state

    # Unpack parameters
    beta = params["beta"]
    sigma0 = params["sigma0"]
    gamma0 = params["gamma0"]

    alpha = params["alpha"]
    beta_epi = params["beta_epi"]
    delta = params["delta"]
    epsilon = params["epsilon"]

    kN = params["kN"]
    kD = params["kD"]

    kE1 = params["kE1"]
    kE2 = params["kE2"]
    kEdecay = params["kEdecay"]

    nicotine = params["nicotine"]
    noise = params["noise"]

    # Dopamine dynamics (fast, noisy)
    dD = (kN * nicotine - kD * D) * dt
    dD += noise * np.random.randn() * np.sqrt(dt)

    # Epigenetic dynamics (slow, persistent)
    dEpi = (kE1 * nicotine + kE2 * D - kEdecay * epi) * dt

    # Protective disease rates
    sigma = sigma0 / (1 + alpha * D + beta_epi * epi)
    gamma = gamma0 / (1 + delta * D + epsilon * epi)

    # Phenotypic transitions
    dS = -beta * S * dt
    dE = (beta * S - sigma * E) * dt
    dI = (sigma * E - gamma * I) * dt
    dR = gamma * I * dt

    return np.array([
        S + dS,
        E + dE,
        I + dI,
        R + dR,
        D + dD,
        epi + dEpi
    ])
