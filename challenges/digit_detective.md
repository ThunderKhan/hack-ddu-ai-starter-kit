# Challenge 1 — 🔢 Digit Detective

**Difficulty:** Beginner · **Technology:** Python, scikit-learn, optional Matplotlib · **GPU:** Not needed

## Mission

Train a model to classify 8×8 grayscale handwritten digits. Start with scikit-learn's built-in digits dataset, verify held-out accuracy, then **build an original improvement or investigation**. You do not need to collect handwriting or download datasets.

[Launch the self-contained Colab notebook](https://colab.research.google.com/github/ThunderKhan/hack-ddu-ai-starter-kit/blob/main/notebooks/digit_detective.ipynb)

## Minimum milestones

- Run the baseline and explain training vs. test data.
- Keep the test set untouched while tuning models. Use cross-validation or a validation split for experimenting.
- Make and demonstrate an original addition and report what changed.
- Explain at least one failure mode using a misclassified image, class confusion or limitations of the data.

## Choose an extension (examples, not mandatory)

- Compare two classifiers on an equivalent evaluation split; explain whether gains are meaningful.
- Add visualization of incorrect predictions, confidence scores and failure patterns.
- Build a small interface allowing users to pick one of the **existing** 8×8 digit images for prediction.
- Add a reproducibility report (model settings, seed, metrics) and a confusion matrix.
- Experiment with reduced training data and study how accuracy changes.

## What to show judges (60–90 seconds)

1. State the problem.
2. Show the running model or improvement.
3. Show the evaluation and what changed from baseline.
4. Explain one limitation and link your team repository.

**Avoid:** testing repeatedly on the same holdout until it becomes a tuning set; claiming results generalize to all real-world handwriting; submitting the unchanged notebook.
