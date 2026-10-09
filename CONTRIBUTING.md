# Contributing to the Track A starter kit

This repository hosts **educational examples** used by the DDUGU organizers; participants should create their **own team repositories** for their hackathon entries.

To improve the shared starter kit:

1. Open a focused issue describing the actual problem.
2. Fork and create a branch, then make the smallest practical fix.
3. Run tests with `python -m unittest discover -s tests -v` and `python scripts/validate_notebooks.py`.
4. Do not add personal student data, credentials, large datasets or generated output cells.
5. Open a PR with an explanation, reproducible steps and appropriate license attribution.

The notebook examples intentionally duplicate the self-contained implementation from src/ to remain runnable in Colab without cloning. When changing a model, **update both the Python module and corresponding notebook**. Keep notebook outputs cleared before committing.

Code reviews require evidence of correctness and respect for fellow contributors. Please follow [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md).
