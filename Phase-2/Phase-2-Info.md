# SPG×SLB Hackathon 2025 – Seismic Denoising Challenge

<div align="center">

![Phase 2](https://img.shields.io/badge/Phase-2-blue?style=for-the-badge)
![Competition](https://img.shields.io/badge/Platform-Kaggle-20BEFF?style=for-the-badge&logo=kaggle&logoColor=white)
![Status](https://img.shields.io/badge/Status-Complete-success?style=for-the-badge)

**AI-Powered Seismic Data Enhancement for Subsurface Imaging**

[Competition Link](https://www.kaggle.com) • [Documentation](#-documentation) • [Results](#-outputs--visualizations)

</div>

---

## 🎯 Overview

This repository presents a comprehensive solution for **Phase 2** of the SPG×SLB Hackathon 2025 Seismic Denoising Challenge. The project focuses on enhancing 2D seismic sections through advanced AI/ML techniques, effectively removing random and coherent noise while maintaining critical geological structures.

**Core Objectives:**
- Suppress random and coherent seismic noise
- Preserve structural continuity of geological features
- Maintain fidelity of horizons, reflectors, and fault patterns
- Achieve optimal balance between noise reduction and signal preservation

This work bridges **geophysics**, **signal processing**, and **data-driven modeling**, delivering practical solutions for seismic interpretation and subsurface imaging applications.

---

## 🧠 Problem Statement

### Challenge Requirements

Given noisy 2D seismic sections, the model must:

1. **Noise Suppression** – Eliminate both random and coherent noise patterns
2. **Structural Preservation** – Maintain geological continuity and features
3. **Signal Fidelity** – Prevent distortion of authentic geological signals

### Deliverables

- Denoised seismic section (2D array)
- Amplitude spectrum comparison (original vs. denoised)
- Performance metrics demonstrating structural preservation

---

## 📂 Dataset Architecture

### Training Dataset

| Attribute | Description |
|-----------|-------------|
| **Volume** | 200 2D seismic sections |
| **Format** | `.npz` (NumPy compressed) |
| **Shape** | `(num_xlines, num_time_samples)` |
| **Type** | Inline (iline) slices |
| **Values** | Floating-point seismic amplitudes |

### Evaluation Dataset

- **File:** `subject_seismic.npz`
- **Purpose:** Final model evaluation target

### Supporting Files

- `sample_submission.csv` – Submission format template

### Data Structure

```
Axis Configuration:
├── X-axis → Crosslines (xlines)
└── Y-axis → Time samples

Storage: NumPy compressed format (.npz)
Content: Single 2D array per file
```

---

## 📊 Evaluation Metrics

The solution is evaluated using a **composite scoring system**:

```
Final Score = α × SSIM + β × PSNR
```

### Metric Breakdown

| Metric | Purpose | Weight |
|--------|---------|--------|
| **SSIM** | Structural Similarity Index<br>Measures preservation of geological structures | α |
| **PSNR** | Peak Signal-to-Noise Ratio<br>Quantifies noise suppression quality | β |

> **Note:** Structural preservation takes precedence over aggressive noise smoothing to maintain geological interpretability.

---

## 🛠️ Methodology

### Processing Pipeline

```
Data Ingestion → Normalization → AI/ML Denoising → Post-processing → Validation
```

**Key Components:**

1. **Preprocessing**
   - Data normalization and standardization
   - Quality assessment and validation

2. **Model Architecture**
   - AI/ML-based denoising framework
   - Optimized for geological feature preservation

3. **Optimization Strategy**
   - Balance between noise suppression and structural continuity
   - Hyperparameter tuning for SSIM-PSNR optimization

4. **Validation**
   - Amplitude spectrum analysis
   - Visual and quantitative quality assessment

---

## 📁 Repository Structure

```
seismic-denoising-spgxslb/
│
├── 📂 data/
│   ├── train/                    # Training seismic sections
│   └── subject_seismic.npz       # Evaluation target
│
├── 📂 notebooks/
│   ├── data_exploration.ipynb    # EDA and visualization
│   ├── model_training.ipynb      # Model development
│   └── inference.ipynb           # Prediction pipeline
│
├── 📂 results/
│   ├── denoised_seismic.png      # Output visualization
│   └── amplitude_spectrum.png    # Frequency analysis
│
├── 📂 src/
│   ├── preprocessing.py          # Data preparation utilities
│   ├── model.py                  # Model architectu
