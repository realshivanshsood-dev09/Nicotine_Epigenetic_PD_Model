# Nicotine_Epigenetic_PD_Model
A multigenerational state-transition model studying nicotine-induced epigenetic neuroprotection and delayed Parkinson’s incidence in α-synuclein Drosophila.

## Overview
This repository implements a mechanistic, multigenerational state-transition model to study how nicotine-induced epigenetic programming modulates Parkinson’s disease incidence in *Drosophila melanogaster* genetically predisposed via α-synuclein expression.

The model is designed to investigate whether neuroprotective epigenetic effects induced by nicotine persist after exposure withdrawal, and how Parkinsonian incidence rebounds across generations once nicotine is removed.

---

## Biological Motivation
Epidemiological and experimental studies suggest that nicotine exerts protective effects in Parkinson’s disease, partly through dopaminergic modulation. However, whether nicotine induces persistent epigenetic changes that alter long-term disease susceptibility remains poorly understood.

This model explicitly separates:
- **Acute dopaminergic protection** (fast, reversible)
- **Epigenetic neuroprotection** (slow, persistent, partially heritable)

allowing analysis of delayed disease rebound following nicotine withdrawal.

---

## Model Structure

### Phenotypic States (Irreversible)
- **S** — Pre-symptomatic α-synuclein flies  
- **E** — Compensated (nicotine-protected, no phenotype)  
- **I** — Parkinsonian phenotype  
- **R** — Severe neurodegeneration / non-viable  

### Regulatory States
- **D** — Dopaminergic protective tone (fast dynamics)
- **Epi** — Epigenetic protective memory (slow dynamics)

---

## Nicotine Exposure Protocol
Nicotine exposure is modeled as a generation-dependent input:
- **Generations 1–5:** Nicotine ON  
- **Generations ≥6:** Nicotine OFF (withdrawal phase)

Epigenetic protection accumulates during exposure and decays gradually after withdrawal, while dopaminergic effects disappear rapidly.

---

## Key Model Features
- Irreversible phenotypic progression
- Epigenetic memory with partial intergenerational inheritance
- Explicit nicotine withdrawal dynamics
- Quantitative definition of Parkinson’s incidence
- Stochasticity to capture biological variability

---

## Model Output
Parkinson’s incidence is defined as the cumulative transition from the compensated state to the Parkinsonian state within each generation. The model predicts:
- Reduced incidence during nicotine exposure
- Persistent suppression after withdrawal
- Delayed rebound as epigenetic protection decays

---

## Running the Simulation

```bash
pip install -r requirements.txt
python scripts/run_simulation.py
