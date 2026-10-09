# Getting started — 10-minute participant guide

## Option A: Google Colab (recommended for beginners)

1. Open the [Digit Detective notebook](../notebooks/digit_detective.ipynb) or [Campus Message Router notebook](../notebooks/campus_message_router.ipynb) on GitHub.
2. Click **Open in Colab** if shown, or use the direct links below.
3. Sign in to Colab and select a CPU runtime. No GPU or paid API key is needed.
4. Run cells sequentially, starting from the top. Your first run may take a moment to import libraries.
5. Save your **own copy** to Drive or download a notebook; changes in a shared or GitHub-viewed notebook are not automatically committed to GitHub.
6. For submission, create your **own** public GitHub repository and upload code/notebook, README and license.

- [Digit Detective — launch Colab](https://colab.research.google.com/github/ThunderKhan/hack-ddu-ai-starter-kit/blob/main/notebooks/digit_detective.ipynb)
- [Campus Message Router — launch Colab](https://colab.research.google.com/github/ThunderKhan/hack-ddu-ai-starter-kit/blob/main/notebooks/campus_message_router.ipynb)

**Colab limitations:** A network connection and Google account are required. Free runtime access and available resources are not guaranteed. If you cannot access Colab, ask a mentor for a local starter copy.

## Option B: Local Python (no cloud needed after installing dependencies)

Requires Python 3.10+ and a terminal in the repository root.

~~~bash
python -m venv .venv
# Activate environment as appropriate for your system
python -m pip install -r requirements.txt
python -m examples.digit_detective_demo
python -m examples.campus_router_demo
~~~

If pip installation fails, use a mentor machine or an existing working Colab runtime rather than spending the entire sprint troubleshooting.

## Teams, originality and evaluation

- Solo is welcome; teams of 2–4 make collaboration simpler.
- Start with the baseline, then change one thing you can demonstrate and evaluate.
- Record a baseline metric and a metric **after the change**; negative results can be discussed honestly.
- Never collect or commit real student data, private messages, tokens or passwords.
- Open a public repository owned by your team and follow [the submission guide](SUBMISSION_GUIDE.md).
