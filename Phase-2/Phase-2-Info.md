SPG×SLB Hackathon 2025 – Seismic Denoising Challenge (Phase 2)
📌 Overview

This repository contains my solution for Phase 2 of the SPG×SLB Hackathon 2025 – Seismic Denoising Challenge, hosted on Kaggle.

The objective of this challenge is to enhance the quality of 2D seismic sections by removing random and coherent noise using AI / ML–based approaches, while preserving geological structures such as horizons, reflectors, and faults.

This work lies at the intersection of geophysics, signal processing, and data-driven modeling, with direct relevance to seismic interpretation and subsurface imaging.

🧠 Problem Statement

Given noisy 2D seismic sections:

Suppress random and coherent noise

Preserve structural continuity

Avoid distortion of true geological signals

The final task is to denoise a target (subject) seismic section and submit:

The denoised seismic section

An amplitude spectrum comparison (original vs denoised)

📂 Dataset Description
Training Data

200 2D seismic sections

Format: .npz

Shape:

(num_xlines, num_time_samples)


Each section represents an inline (iline) slice

Evaluation Data

subject_seismic.npz

This is the seismic section used for final evaluation

Additional Files

sample_submission.csv – template for submission format

🧪 Data Format

Stored as NumPy compressed files (.npz)

Each file contains a single 2D array:

X-axis → Crosslines (xlines)

Y-axis → Time samples

Amplitude values are floating-point seismic amplitudes

🎯 Evaluation Metric

Submissions are evaluated using a combined score based on:

Final Score = x × SSIM + y × PSNR


Where:

SSIM (Structural Similarity Index)
→ Measures preservation of geological structures (faults, horizons)

PSNR (Peak Signal-to-Noise Ratio)
→ Measures overall noise suppression and pixel-level similarity

⚠️ Structural preservation is prioritized over aggressive smoothing.

🛠️ Methodology (High-Level)

(You can expand this section later with model details)

Data normalization and preprocessing

AI / ML-based denoising model

Careful tuning to balance:

Noise suppression

Geological continuity

Post-processing and visualization

Amplitude spectrum analysis for validation

📊 Outputs & Visualizations

The following outputs are generated:

✅ Denoised seismic section (2D image)

📈 Amplitude spectrum comparison
(Original vs Denoised – single plot)

📦 Final denoised data saved in .npz format

📁 Repository Structure
├── data/
│   ├── train/
│   └── subject_seismic.npz
│
├── notebooks/
│   ├── data_exploration.ipynb
│   ├── model_training.ipynb
│   └── inference.ipynb
│
├── results/
│   ├── denoised_seismic.png
│   └── amplitude_spectrum.png
│
├── src/
│   ├── preprocessing.py
│   ├── model.py
│   └── utils.py
│
├── requirements.txt
├── README.md
└── LICENSE

🚀 How to Run
# Clone the repository
git clone https://github.com/<your-username>/seismic-denoising-spgxslb.git
cd seismic-denoising-spgxslb

# Install dependencies
pip install -r requirements.txt

# Run inference
python src/inference.py

🧾 Competition Details

Competition: SPG×SLB Hackathon 2025 – Phase 2

Platform: Kaggle

Host: Vishvendra Veer

Participants: 32

Teams: 8

Submissions: 34

Category: Community Prediction Challenge (Private)

📖 Acronyms

iline – Inline number

xline – Crossline number

SSIM – Structural Similarity Index

PSNR – Peak Signal-to-Noise Ratio

📜 License

This project follows the Kaggle Competition Rules.
Dataset usage is restricted to the terms defined by the competition.

🙌 Acknowledgements

Society of Petroleum Geophysicists (SPG)

SLB (Schlumberger)

Kaggle platform and community

Organizers of SPG×SLB Hackathon 2025
