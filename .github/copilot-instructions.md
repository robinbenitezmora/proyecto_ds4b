## Copilot / AI Agent Instructions for this repo

This is a small, single-purpose Data Science pilot that analyzes customer churn
and contains a minimal script and dataset. Keep changes minimal and make
behavior explicit so humans can review quickly.

- **Big picture:** the project is a prototype for predicting/preventing
  customer abandonment. Key files are `README.md`, `scripts/app_abandono.py`,
  the data folder `datos/` (contains `clientes.csv`), and the environment
  specification `entorno.yml`.

- **Run / debug:** the working directory is the repository root. Scripts
  assume relative paths to `datos/clientes.csv`. To create the Python
  environment use the included conda file:

  conda env create -f entorno.yml

  Then run the main script with:

  python scripts/app_abandono.py

- **Why relative paths matter:** `scripts/app_abandono.py` reads
  `datos/clientes.csv` with a plain `pd.read_csv("datos/clientes.csv")`.
  Avoid moving `datos/` without updating all path usages; prefer using
  `pathlib.Path(__file__).resolve().parents[1] / 'datos'` when refactoring.

- **Coding patterns in this repo:**
  - Lightweight, notebook-like scripts (no package layout, no tests).
  - Data loading occurs with Pandas; simple column transforms (see
    `scripts/app_abandono.py` where `pd.qcut` is used to create
    `segmento_valor`).

- **When editing or extending:**
  - Keep data I/O explicit and reproducible (accept `data_dir` or use
    repo-root based resolution). Show example calls in `if __name__ == '__main__'`.
  - Add a small README subsection for any new script explaining inputs/outputs.

- **Common tasks you'll be asked to do:**
  - Add a prediction pipeline (train + save model) and a small CLI to run it.
  - Add unit tests for data transforms (create a `tests/` folder if needed).
  - Create a `requirements.txt` if moving away from conda for CI.

- **Don't assume:** there is no CI, no packaging, and no test harness. Keep
  changes simple and document any new dependencies in `entorno.yml` or a
  new `requirements.txt`.

If anything here is unclear or you want the agent to add a starter test or
packaging scaffold, ask and I will update these instructions.
