# run_simulation.py

from src.simulate import simulate_generations
from src.utils import save_results

if __name__ == "__main__":

    incidence = simulate_generations(
        generations=10,
        T=30,
        dt=0.1
    )

    save_results(incidence, "outputs/incidence_results.csv")

    print("Simulation complete.")
    print("Incidence per generation:")
    for g, inc in enumerate(incidence, start=1):
        print(f"Generation {g}: {inc:.4f}")
