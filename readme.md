# 🧠 TARS Empirical Experiment

This repository contains the full implementation, dataset, and analysis scripts for the **empirical evaluation of TARS** — an AI-powered _proactive code comprehension assistant_.  
The experiment investigates how **proactive assistance** affects developer **efficiency**, **cognitive load**, and **user perception**, compared to a traditional, reactive assistant paradigm.

---

## 📘 Overview

This study was conducted as part of a controlled **in-vitro experiment** involving 18 participants with backgrounds in computer science, software engineering, and data science.  
Participants were divided into two conditions:

- **TARS (Treatment Group):** Developers used the proactive AI assistant.
- **NO_TARS (Control Group):** Developers completed the same tasks without assistance.

Each participant performed identical programming comprehension tasks, followed by post-task questionnaires.

---

## 🎯 Research Objectives

The experiment was designed to address three main **research questions (RQs):**

1. **RQ1:** Does proactive assistance improve developers’ task performance (time and correctness)?
2. **RQ2:** How is TARS perceived by users in terms of utility, ease of use, and cognitive load?
3. **RQ3:** How do developers’ explanations semantically align with reference documentation when using TARS?

---

---

## 🧩 Data Processing Pipeline

Before the statistical analysis, extensive data cleaning and transformation were performed.

### 1. Time Standardization

All task completion times, originally recorded in a mixed `minutes:seconds` format, were converted into **seconds** for consistency.

### 2. Scale Aggregation

Several psychological constructs were measured using multi-item questionnaires.  
Scores were aggregated using the **mean** across items, resulting in unified metrics for each participant:

| Category     | Constructs Aggregated                                                                                          |
| ------------ | -------------------------------------------------------------------------------------------------------------- |
| **NASA-TLX** | Mental Demand, Effort, Frustration, Physical Demand, Temporal Demand, Performance                              |
| **TAM**      | Perceived Usefulness (PU), Perceived Ease of Use (PEU), Attitude Toward Using (ATU), Behavioral Intention (BI) |
| **TOM**      | Theory of Mind (ToM) composite score                                                                           |

---

## 📊 Analysis Workflow

The analytical process consists of **three major phases**:

1. **Descriptive Statistics**

   - Central tendency and dispersion measures (Mean, Median, Std. Dev.)
   - Group comparison between TARS and NO_TARS
   - Preliminary observations on performance and perception

2. **Exploratory Data Analysis**

   - Visual inspection using boxplots and distribution charts
   - Assessment of normality assumptions via **KDE** and **Q-Q plots**
   - Participant demographics and AI-tool adoption visualization

3. **Inferential Statistics**
   - Parametric or non-parametric hypothesis testing
   - Evaluation of RQs based on performance metrics, TAM, and NASA-TLX constructs
   - Verification of statistical significance (p < 0.05)

---

## 🧠 Key Findings

- **Efficiency:** Participants using TARS completed tasks **significantly faster** with **lower variance**.
- **Quality:** The **cosine similarity** between explanations and docstrings remained comparable across groups — speed did not compromise explanation quality.
- **Perception:** TAM results were **strongly positive**, with high PU, PEU, ATU, and BI scores.
- **Cognitive Load:** NASA-TLX metrics indicated **low mental demand, effort, and frustration**.

These findings collectively suggest that **proactive assistance** improves efficiency and user experience without degrading output quality.

---

## 🧮 Statistical Tools and Models

- **Libraries:** `pandas`, `numpy`, `matplotlib`, `scipy`, `seaborn`, `statsmodels`
- **Embedding Model:** [`intfloat/multilingual-e5-base`](https://huggingface.co/intfloat/multilingual-e5-base)
  - Used for cosine similarity computation between participants’ explanations and the ground-truth docstrings.
- **Normalization:** Text preprocessing pipeline included tokenization, stop-word removal, and Porter stemming.

---

## 📈 Visualizations

All figures in the `figure/` folder are generated automatically during analysis:

- **Task Completion Time Boxplot**
- **Cosine Similarity Boxplot**
- **Kernel Density & Q-Q Plots** for each construct (PU, PEU, ATU, MD, F, BI, etc.)
- **AI Tool Usage Charts** showing adoption and frequency trends

---

## 🧪 Reproducibility

To replicate the analysis:

```bash
# 1. Clone the repository
git clone https://github.com/leotodisco/TARS_empirical_experiment
cd TARS_empirical_experiment

# 2. Install dependencies
pip install -r requirements.txt

# 3. Run the analysis
jupyter notebook scripts/01_data_cleaning.ipynb
```
