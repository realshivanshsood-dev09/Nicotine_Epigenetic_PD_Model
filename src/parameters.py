# parameters.py

def get_parameters(nicotine_on=True):
    """
    Returns model parameters.
    Nicotine is ON for first 5 generations, OFF afterward.
    """

    params = {
        # Phenotypic transition
        "beta": 0.02,        # S -> E transition

        # Baseline disease rates
        "sigma0": 0.08,      # Parkinson onset
        "gamma0": 0.05,      # Degeneration rate

        # Protective strength
        "alpha": 2.0,        # Dopamine -> onset suppression
        "beta_epi": 3.0,     # Epigenetics -> onset suppression
        "delta": 1.5,        # Dopamine -> degeneration suppression
        "epsilon": 2.0,      # Epigenetics -> degeneration suppression

        # Dopamine dynamics
        "kN": 1.0,           # Nicotine → dopamine induction
        "kD": 1.2,           # Dopamine decay

        # Epigenetic dynamics
        "kE1": 0.4,          # Nicotine → epigenetic induction
        "kE2": 0.3,          # Dopamine → epigenetic reinforcement
        "kEdecay": 0.05,     # Epigenetic decay

        # Noise
        "noise": 0.02,

        # Nicotine exposure
        "nicotine": 1.0 if nicotine_on else 0.0
    }

    return params
