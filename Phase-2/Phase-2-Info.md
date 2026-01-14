# 🌊 SPG×SLB Hackathon 2025 – Seismic Denoising Challenge

<div align="center">

![Banner](https://img.shields.io/badge/🏆_Phase_2-Completed-gold?style=for-the-badge)
![Competition](https://img.shields.io/badge/Kaggle-20BEFF?style=for-the-badge&logo=kaggle&logoColor=white)
![AI/ML](https://img.shields.io/badge/AI/ML-Geophysics-purple?style=for-the-badge)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)

### *Transforming Noisy Seismic Data into Crystal-Clear Subsurface Insights*

**Using Deep Learning to Preserve Geological Truth While Eliminating Noise**

---

[![View on Kaggle](https://img.shields.io/badge/View_Competition-Kaggle-20BEFF?style=flat&logo=kaggle)](https://www.kaggle.com)
[![GitHub stars](https://img.shields.io/github/stars/yourusername/seismic-denoising?style=social)](https://github.com/yourusername/seismic-denoising)
[![License](https://img.shields.io/badge/License-Competition_Rules-red?style=flat)](LICENSE)

</div>

---

## 🎯 Mission Statement

> **Challenge:** Transform noisy 2D seismic sections into pristine geological images that reveal the Earth's subsurface secrets.

In this intense **SPG×SLB Hackathon 2025**, I developed an AI-powered solution that doesn't just remove noise—it intelligently preserves every fault line, horizon, and reflector that geophysicists depend on for accurate subsurface interpretation.

### 🎪 The Challenge Arena

```
┌─────────────────────────────────────────────────────────┐
│  🎯 32 Participants  │  👥 8 Teams  │  📊 34 Submissions │
└─────────────────────────────────────────────────────────┘
```

---

## 🧠 The Problem: Signal vs. Noise

### What I Solved

Seismic data is inherently noisy. Random interference and coherent noise patterns obscure critical geological features. My mission was to:

<table>
<tr>
<td width="33%" align="center">

### 🎯 **Suppress Noise**
Eliminate random & coherent noise patterns without compromise

</td>
<td width="33%" align="center">

### 🏔️ **Preserve Structure**
Maintain geological continuity—every fault, horizon, and reflector

</td>
<td width="33%" align="center">

### ✨ **Enhance Clarity**
Deliver interpretable data that geophysicists can trust

</td>
</tr>
</table>

### 📦 My Deliverables

- ✅ **Denoised Seismic Section** – Production-ready geological image
- 📈 **Amplitude Spectrum Analysis** – Frequency domain validation
- 🎯 **Optimized SSIM+PSNR Scores** – Quantified quality metrics

---

## 📊 Dataset Deep Dive

### 🗄️ Training Arsenal

I worked with a comprehensive dataset designed to challenge even the most sophisticated denoising algorithms:

<div align="center">

| 📦 Component | 📋 Specification |
|:-------------|:-----------------|
| **Volume** | 200 2D seismic sections |
| **Format** | `.npz` (NumPy compressed arrays) |
| **Dimensions** | `(num_xlines, num_time_samples)` |
| **Data Type** | Float32 seismic amplitudes |
| **Slice Type** | Inline (iline) geological cross-sections |

</div>

### 🎯 Evaluation Target

**Subject File:** `subject_seismic.npz`  
The ultimate test—a blind seismic section where my model's true performance would be measured.

### 📐 Data Architecture

```
Seismic Data Cube Structure:
│
├── 📍 X-Axis (Horizontal) ──→ Crosslines (xlines)
│                                Spatial positioning
│
└── ⏱️ Y-Axis (Vertical) ──→ Time Samples
                                Two-way travel time (TWT)

💾 Storage: NumPy .npz format
🔢 Values: Seismic amplitude measurements
```

---

## 🏆 Scoring System: The Double-Edged Sword

My model was evaluated using a sophisticated **dual-metric system** that balanced two competing objectives:

<div align="center">

### 🎯 Competition Formula

```
🏅 Final Score = α × SSIM + β × PSNR
```

</div>

<table>
<tr>
<td width="50%">

### 📊 **SSIM** – Structure Guardian
**Structural Similarity Index**

- 🎯 **Purpose:** Preserve geological features
- 🏔️ **Protects:** Faults, horizons, reflectors
- 💎 **Philosophy:** Structural truth > pixel perfection
- ⚖️ **Weight:** α (High priority)

</td>
<td width="50%">

### 📡 **PSNR** – Noise Warrior
**Peak Signal-to-Noise Ratio**

- 🎯 **Purpose:** Quantify noise suppression
- 🔍 **Measures:** Pixel-level reconstruction quality
- 🧹 **Philosophy:** Clean data, clear insights
- ⚖️ **Weight:** β (Supporting metric)

</td>
</tr>
</table>

> **⚠️ Critical Insight:** The competition prioritized **structural preservation** over aggressive smoothing. A geologist needs to trust every fault line—blurring them for higher PSNR would be a pyrrhic victory.

---

## 🛠️ My Technical Approach

### 🔬 The Pipeline

I engineered a sophisticated processing pipeline that balances computational efficiency with geological accuracy:

```
┌──────────────┐    ┌──────────────┐    ┌──────────────┐    ┌──────────────┐    ┌──────────────┐
│   📥 Data    │ ─→ │ 🔧 Preproc   │ ─→ │ 🧠 AI Model  │ ─→ │ ✨ Postproc  │ ─→ │ ✅ Validated │
│  Ingestion   │    │ & Normalize  │    │  Denoising   │    │ & Refinement │    │    Output    │
└──────────────┘    └──────────────┘    └──────────────┘    └──────────────┘    └──────────────┘
       │                    │                    │                    │                    │
       └─ Load .npz         └─ Standardize       └─ Neural Net        └─ Polish           └─ Validate
          Validate shape        Scale values         Architecture         Edge handling        SSIM/PSNR
          Check quality         Handle outliers      Noise removal        Spectrum check       Export
```

### 🎯 Key Innovation Areas

<details>
<summary><b>🔧 1. Advanced Preprocessing</b></summary>

- **Normalization Strategy:** Custom scaling to preserve geological amplitude relationships
- **Quality Gating:** Automated detection of data anomalies
- **Validation Checks:** Ensuring data integrity before model input

</details>

<details>
<summary><b>🧠 2. AI/ML Architecture</b></summary>

- **Model Design:** Neural network optimized for seismic data characteristics
- **Training Strategy:** Balanced approach to noise reduction and structure preservation
- **Loss Function:** Custom hybrid loss combining SSIM and PSNR objectives

</details>

<details>
<summary><b>⚡ 3. Optimization & Tuning</b></summary>

- **Hyperparameter Search:** Grid search across architecture configurations
- **Cross-Validation:** Ensuring generalization across diverse seismic patterns
- **A/B Testing:** Comparing multiple model variants on validation set

</details>

<details>
<summary><b>✨ 4. Post-Processing & Validation</b></summary>

- **Edge Preservation:** Special handling for geological boundaries
- **Spectrum Analysis:** Frequency domain verification of noise removal
- **Visual QC:** Expert review of denoised sections

</details>

---

## 📁 Repository Architecture

```
🗂️ seismic-denoising-spgxslb/
│
├── 📂 data/
│   ├── 📂 train/                         # 200 training seismic sections
│   │   ├── section_001.npz
│   │   ├── section_002.npz
│   │   └── ...
│   ├── 📄 subject_seismic.npz            # Competition evaluation target
│   └── 📄 sample_submission.csv          # Submission format template
│
├── 📂 notebooks/
│   ├── 📓 01_data_exploration.ipynb      # EDA & visualization
│   ├── 📓 02_model_development.ipynb     # Architecture experiments
│   ├── 📓 03_training_pipeline.ipynb     # Model training loops
│   └── 📓 04_inference_submission.ipynb  # Final predictions
│
├── 📂 results/
│   ├── 🖼️ denoised_seismic.png           # Primary output visualization
│   ├── 📊 amplitude_spectrum.png         # Frequency analysis plot
│   ├── 📈 training_curves.png            # Loss & metrics over time
│   └── 💾 final_submission.npz           # Competition submission file
│
├── 📂 src/
│   ├── 🔧 preprocessing.py               # Data preparation utilities
│   ├── 🧠 model.py                       # Neural network architecture
│   ├── 🎯 training.py                    # Training loops & optimization
│   ├── 🔍 evaluation.py                  # Metrics calculation
│   └── 🛠️ utils.py                       # Helper functions
│
├── 📄 requirements.txt                    # Python dependencies
├── 📄 README.md                           # This file
├── 📄 LICENSE                             # Competition rules compliance
└── 📄 .gitignore                          # Git exclusions
```

---

## 🚀 Reproduction Guide

### ⚙️ Environment Setup

```bash
# 1️⃣ Clone my competition solution
git clone https://github.com/yourusername/seismic-denoising-spgxslb.git
cd seismic-denoising-spgxslb

# 2️⃣ Create isolated Python environment
python -m venv venv

# Activate (choose your OS):
source venv/bin/activate        # 🐧 Linux/Mac
venv\Scripts\activate           # 🪟 Windows

# 3️⃣ Install all dependencies
pip install -r requirements.txt
```

### 🎯 Running My Solution

```bash
# Execute the complete denoising pipeline
python src/inference.py

# Or explore interactively via Jupyter
jupyter notebook notebooks/04_inference_submission.ipynb
```

### 📦 Expected Outputs

After running the pipeline, you'll find:

```
results/
├── ✅ denoised_seismic.npz              # Final submission-ready data
├── 🖼️ denoised_seismic.png              # Visual comparison plot
├── 📊 amplitude_spectrum.png           # Frequency domain analysis
└── 📈 metrics_report.json              # SSIM, PSNR, and other scores
```

---

## 📈 Results & Visualizations

### 🎨 What My Solution Produces

<table>
<tr>
<td width="50%" align="center">

### 🖼️ **Denoised Seismic Section**
Crystal-clear geological image with:
- ✨ Suppressed random noise
- 🏔️ Preserved fault structures
- 📏 Maintained horizon continuity

</td>
<td width="50%" align="center">

### 📊 **Amplitude Spectrum**
Frequency domain comparison showing:
- 🔊 Original noisy spectrum
- 🎯 Denoised clean spectrum
- 📉 Noise reduction across frequencies

</td>
</tr>
</table>

### 🏆 Performance Metrics

My final submission achieved competitive scores on:

- **SSIM Score:** Structure preservation metric
- **PSNR Score:** Noise suppression metric
- **Combined Score:** Weighted competition metric

*Note: Exact scores withheld pending final competition results*

---

## 🎓 Key Learnings & Insights

### 💡 Technical Discoveries

1. **Geological Domain Knowledge Matters:** Understanding fault mechanics and seismic reflection patterns was crucial for model design
2. **SSIM vs PSNR Tradeoff:** Found the sweet spot between structure preservation and noise reduction
3. **Preprocessing is Half the Battle:** Quality data normalization dramatically improved model convergence

### 🚀 What Worked Best

- **Hybrid Loss Functions:** Combining multiple objectives led to better generalization
- **Progressive Denoising:** Multi-stage approach outperformed single-pass methods
- **Frequency Domain Analysis:** Validating in both time and frequency domains caught edge cases

---

## 📖 Terminology Glossary

<div align="center">

| 🏷️ Term | 📚 Definition | 🎯 Context |
|:--------|:-------------|:----------|
| **iline** | Inline number | Seismic survey line running in primary direction |
| **xline** | Crossline number | Lines perpendicular to inline direction |
| **SSIM** | Structural Similarity Index | Perceptual quality metric (0-1 scale) |
| **PSNR** | Peak Signal-to-Noise Ratio | Reconstruction quality (dB scale) |
| **TWT** | Two-Way Travel Time | Seismic wave travel time (milliseconds) |
| **SPG** | Society of Petroleum Geophysicists | Professional organization |
| **SLB** | Schlumberger | Global oilfield services company |

</div>

---

## 🏅 Competition Stats

<div align="center">

### 📊 By The Numbers

| Metric | Value |
|:-------|:------|
| **🏆 Competition** | SPG×SLB Hackathon 2025 – Phase 2 |
| **🌐 Platform** | Kaggle Community Challenge |
| **👤 Organizer** | Vishvendra Veer |
| **👥 Total Participants** | 32 data scientists |
| **🤝 Teams Formed** | 8 collaborative teams |
| **📊 Total Submissions** | 34 solution attempts |
| **🏷️ Category** | Private Prediction Competition |
| **📅 Duration** | [Competition dates] |
| **🎯 My Rank** | [Your final rank] |

</div>

---

## 📜 License & Usage

This project strictly adheres to **Kaggle Competition Rules**. 

- ✅ Dataset usage governed by competition terms
- ⚠️ Commercial use may be restricted
- 📋 Code shared under [specify license]
- 🤝 Attribution required for derivative works

For detailed terms, see [LICENSE](LICENSE) file.

---

## 🙏 Acknowledgements

This journey wouldn't have been possible without:

<table>
<tr>
<td width="33%" align="center">

### 🛢️ **Industry Partners**
**SPG** – Society of Petroleum Geophysicists  
Domain expertise and challenge design

**SLB** (Schlumberger)  
Real-world datasets and industry insights

</td>
<td width="33%" align="center">

### 🌐 **Platform & Community**
**Kaggle**  
Competition infrastructure

**Open Source Community**  
Libraries: NumPy, PyTorch, scikit-image

</td>
<td width="33%" align="center">

### 👥 **People**
**Vishvendra Veer**  
Competition organizer

**Fellow Participants**  
Inspiration and friendly competition

</td>
</tr>
</table>

---

## 🔗 Connect & Collaborate

<div align="center">

[![Portfolio](https://img.shields.io/badge/Portfolio-000000?style=for-the-badge&logo=About.me&logoColor=white)](https://yourportfolio.com)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://linkedin.com/in/yourprofile)
[![Kaggle](https://img.shields.io/badge/Kaggle-20BEFF?style=for-the-badge&logo=kaggle&logoColor=white)](https://kaggle.com/yourprofile)
[![GitHub](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)](https://github.com/yourusername)

### 💬 Questions or Collaboration Ideas?

Feel free to open an issue or reach out directly. I'm always excited to discuss geophysics, AI/ML, and signal processing!

---

### ⭐ Found This Useful?

If this repository helped your research or learning journey, consider giving it a star! It helps others discover the work.

---

**Built with** 🧠 **intelligence**, ❤️ **passion**, and ☕ **caffeine**

*Transforming seismic noise into geological insights, one tensor at a time*

[⬆️ Back to Top](#-spgslb-hackathon-2025--seismic-denoising-challenge)

</div>
