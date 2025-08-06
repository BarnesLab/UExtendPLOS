# A Shape-Based Functional Index for Objective Assessment of Pediatric Motor Function

[![Python](https://img.shields.io/badge/python-3.7+-blue.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Jupyter](https://img.shields.io/badge/jupyter-notebook-orange.svg)](https://jupyter.org/)

> Functional data analysis of arm curl and knock movement data using advanced statistical methods.

## 📋 Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Installation](#installation)
- [Quick Start](#quick-start)
- [Data Structure](#data-structure)
- [Usage](#usage)
- [Results](#results)
  
## 🔍 Overview

This repository contains the complete analysis pipeline for our research on functional data analysis of movement patterns. The project focuses on:

- **Movement analysis** across multiple participants
- **Functional data registration** and alignment techniques
- **Statistical modeling** of temporal movement patterns
- **Comparative analysis** between different cohorts and time points

## ✨ Features

- 📊 Complete functional data analysis pipeline
- 📈 Advanced visualization with publication-ready plots  
- 🔬 Statistical modeling using functional regression
- 📱 Jupyter notebook interface for interactive analysis
- 🔄 Reproducible research workflow
- 📋 Support for both arm curl and knock movement data

## 🚀 Installation

### Prerequisites

- Python 3.7 or higher
- Jupyter Notebook or JupyterLab

### Install Dependencies

```bash
# Clone the repository
git clone https://github.com/yourusername/u-extend.git
cd u-extend

# Install required packages
pip install fdasrsf seaborn statsmodels numpy pandas matplotlib scipy
```

### Conda Environment (Recommended)

```bash
# Create a new conda environment
conda create -n uextend python=3.8
conda activate uextend

# Install packages
conda install -c conda-forge fdasrsf seaborn statsmodels numpy pandas matplotlib scipy jupyter
```

## ⚡ Quick Start

1. **Launch Jupyter Notebook**
   ```bash
   jupyter notebook paper_codes.ipynb
   ```

2. **Run the Analysis**
   - Execute all cells to reproduce arm curl results
   - Modify data paths for knock data analysis
   - View generated plots and statistical outputs


### Data Format Details

| File | Description | Format | Example |
|------|-------------|---------|---------|
| `ys_*` | Time series gyroscope measurements | Numeric array | Movement trajectories |
| `pids_*` | Participant identifiers | Numeric array | `[1, 2, 3, 4, ...]` |
| `visits_*` | Visit dates | Datetime array | `['7/30/24', '6/3/24', ...]` |
| `cohorts_*` | Group assignments | String array | `['Control', 'DMD', ...]` |

## 📖 Usage

### Basic Analysis

```python
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from fdasrsf import *

# Load data
ys = np.loadtxt('ys_curl_wodelta.txt')
pids = np.loadtxt('pids_curl_wodelta.txt')
visits = np.loadtxt('visits_curl_wodelta.txt', dtype=str)
cohorts = np.loadtxt('cohorts_new.txt', dtype=str)

# Run analysis pipeline
# [Analysis code follows...]
```

### Reproducing Paper Results

1. **Arm Curl Analysis**: Run `paper_codes.ipynb` as-is
2. **Knock Data Analysis**: 
   - Update file paths to knock data files
   - Follow same analysis pipeline
   - Compare results across movement types

## 📊 Results

The analysis generates:

- **📈 Functional trajectories** showing movement patterns
- **📉 Mean functions** for different groups and visits  
- **🔍 Statistical comparisons** between cohorts and time points
- **📋 Model summaries** with parameter estimates and significance tests
- **🎨 Publication-ready visualizations** using seaborn styling

