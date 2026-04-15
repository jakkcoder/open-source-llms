# Open-source LLM exploration

Python workspace for experimenting with Hugging Face Transformers, Datasets, and related tooling. Dependencies are managed with [uv](https://github.com/astral-sh/uv).

## Setup

Install [uv](https://docs.astral.sh/uv/getting-started/installation/), then from this directory:

```bash
uv sync
```

Copy `.env.example` to `.env` and set `HF_TOKEN` if you need gated models or higher Hub rate limits.

## Optional: pip and `requirements.txt`

If you prefer plain pip:

```bash
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

Regenerate the file after dependency changes:

```bash
uv export --no-dev --no-hashes -o requirements.txt
```

## Smoke test

```bash
uv run python examples/smoke_test.py
```

## Stack (high level)

- `transformers`, `tokenizers`, `safetensors`
- `datasets`, `accelerate`, `huggingface-hub`
- `torch` (pulled in by the above)
- `rich`, `python-dotenv`

Lockfile: `uv.lock`. Project metadata: `pyproject.toml`.
