# Challenge 2 — 📨 Campus Message Router

**Difficulty:** Beginner · **Technology:** Python, scikit-learn NLP · **GPU:** Not needed

## Mission

Teach a small classifier to categorize **fictional** student requests: academics, facilities, events, or technical support. The starter uses TF-IDF text features and logistic regression. It includes an uncertainty/needs-review option because not all messages fit neatly into a category.

[Launch the self-contained Colab notebook](https://colab.research.google.com/github/ThunderKhan/hack-ddu-ai-starter-kit/blob/main/notebooks/campus_message_router.ipynb)

## Minimum milestones

- Run the baseline; inspect class-wise precision/recall or model errors.
- Build a new feature or materially change how the classifier works.
- Explain how you evaluated the change fairly.
- Keep all examples fictional. Do **not** paste real student messages, emails, phone numbers, IDs, or private chats.

## Extension ideas

- Design and justify a new set of fictional examples without leaking test data.
- Add an interactive UI for pasting a fictional question and showing prediction + caveat.
- Compare n-gram settings or model types; keep the holdout consistent.
- Analyze mistaken classifications and create a useful uncertainty or fallback UI.
- Demonstrate how short, ambiguous or multi-topic messages cause difficulties.

## How to demo

Show two fictional messages, your innovation, evaluation result, and one known limitation. Explain that confidence scores are **not guaranteed correctness probabilities**.

**Avoid:** submitting the unchanged starter; claiming the classifier is ready to route actual support requests; inserting personal information into code or prompts.
