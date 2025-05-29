[![Data Science CI Pipeline](https://github.com/thatwonguy/github_actions_cicd_for_ds/actions/workflows/ci_cd.yml/badge.svg)](https://github.com/thatwonguy/github_actions_cicd_for_ds/actions/workflows/ci_cd.yml)
## CI/CD Proof of Concept for Data Science using github_actions
Minimal GitHub directory structure and content that demonstrates a CI/CD pipeline for a Data Science team using GitHub Actions, covering basic testing, validation, and automation.

This repo demonstrates a minimal CI/CD pipeline for a data science project using GitHub Actions.

## Structure
- `src/`: Python source code (e.g. model training)
- `tests/`: Pytest test cases
- `data/`: Sample input CSV for testing
- `.github/workflows/ci.yml`: GitHub Actions pipeline for CI

## Run Locally
```bash
pip install -r requirements.txt
pytest tests/
```

---

This structure and code will:

✅ Install dependencies  
✅ Run tests automatically on push/pull request  
✅ Prove CI/CD functionality for model training pipelines  