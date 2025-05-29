[![Data Science CI Pipeline](https://github.com/thatwonguy/github_actions_cicd_for_ds/actions/workflows/ci_cd.yml/badge.svg)](https://github.com/thatwonguy/github_actions_cicd_for_ds/actions/workflows/ci_cd.yml)

# ⚙️ Data Science CI/CD Pipeline — Proof of Concept

This repository demonstrates a **minimal CI/CD pipeline for a data science project** using **GitHub Actions**, with features including:

- ✅ Automated testing of model training logic
- ✅ Scheduled pipeline execution every 20 minutes
- ✅ Manual workflow trigger support
- ✅ Versioned artifact uploads (model + logs)
- ✅ Auto-cleanup of artifacts after 3 days

---

## 📁 Repository Structure

| Path                    | Purpose                                      |
|-------------------------|----------------------------------------------|
| `src/`                  | Python code for model training (`model.py`)  |
| `tests/`                | Pytest test to validate training             |
| `data/sample.csv`       | Dummy data for testing                       |
| `.github/workflows/ci_cd.yml` | GitHub Actions workflow file               |
| `outputs/` (generated)  | Stores model and log files (uploaded as artifact) |

---

## 🛠 CI/CD Workflow Features

- **Trigger Events**:
  - On every `push` or `pull_request`
  - Every 20 minutes via cron (`*/20 * * * *`)
  - Manually via GitHub UI

- **Actions Performed**:
  - Installs dependencies
  - Creates output directory
  - Runs tests with `pytest` and saves logs
  - Saves trained model as `model.pkl`
  - Uploads model + logs as versioned artifacts
  - Cleans up artifacts automatically after 3 days

---

## 🧪 Run Locally

```bash
pip install -r requirements.txt
pytest tests/
```

**🚀 What This Proves**   
- ✅ Continuous Integration for data science workflows  
- ✅ Lightweight, reproducible test pipeline  
- ✅ Scheduled, trackable model validation  
- ✅ Foundation for full MLOps workflows  

Built for demonstration purposes. Adapt this template for real-world ML deployment, data validation, or retraining workflows.