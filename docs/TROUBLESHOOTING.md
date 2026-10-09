# Troubleshooting

**Colab doesn't open:** Sign into a Google account, try the direct Colab link from README, or download the notebook from GitHub and use a mentor machine. Colab is a third-party service and availability is not guaranteed.

**Notebook says ModuleNotFoundError: sklearn:** In Colab, if dependencies aren't preinstalled, run a separate code cell with `%pip install scikit-learn numpy matplotlib` and restart/retry. Locally run `python -m pip install -r requirements.txt` inside a virtual environment.

**No internet:** Run `python -m examples.digit_detective_demo` locally after prerequisites were installed in advance. Both toy datasets are local; do not attempt new package installations without connectivity.

**My router predicts the wrong category:** That's expected with a tiny synthetic corpus. Study confusion metrics, add appropriate *fictional* training examples and evaluate fairly.

**Different results every time:** Check random seeds, package versions and train/test split. Don't fit the vectorizer/scaler on test data.

**GitHub says file is too large:** Remove downloaded models, large media, generated caches, and notebook outputs before committing. Never commit .env files or credentials.

**I changed the notebook but can't find it on GitHub:** Colab edits are in your personal copy or session. Download it, push to your team's repository, and confirm the published commit and license.

**A teammate cannot see our submission:** Make your repository public, double-check the link, and confirm official event form access with an organizer. Project publication and official submission are separate steps.

**A project seems to work only with an API key:** Don't hardcode it. Choose a local demo, use an open model/tool with permission, or mock the unavailable dependency clearly without claiming the mock is a real AI result.
