# 🚀 Hack DDU — Open-Source AI Starter Kit

**Track A · Hacktoberfest Hack Day Gorakhpur × DDUGU · Saturday, 10 October 2026**

A runnable starter kit for beginner-friendly AI projects at the Institute of Engineering & Technology, Deen Dayal Upadhyaya Gorakhpur University. Learn, experiment, build an original extension, and demonstrate what you made.

**This is a starter kit, not a submission repository.** Each team builds and submits its own project. Merely rerunning a notebook is learning, not an original competition entry.

## Start here — run in your browser

| Challenge | Starter | Difficulty | No paid API? |
| --- | --- | --- | --- |
| 🔢 Digit Detective | [Open notebook in Colab](https://colab.research.google.com/github/ThunderKhan/hack-ddu-ai-starter-kit/blob/main/notebooks/digit_detective.ipynb) | Beginner | Yes |
| 📨 Campus Message Router | [Open notebook in Colab](https://colab.research.google.com/github/ThunderKhan/hack-ddu-ai-starter-kit/blob/main/notebooks/campus_message_router.ipynb) | Beginner | Yes |
| 💡 Open Innovation | [Read the challenge](challenges/open_innovation.md) | Any level | Depends on your choice |

Colab requires an internet connection and Google account. Both examples use small local datasets and **scikit-learn**, without secret keys or paid inference services. The digit example uses a built-in dataset; all message examples are fictional. Models are demonstration baselines and not production-ready.

## The three challenge briefs

1. [Digit Detective](challenges/digit_detective.md): recognize digits, evaluate results, and improve the baseline.
2. [Campus Message Router](challenges/campus_message_router.md): classify fictional student messages, investigate mistakes, and build responsible uncertainty handling.
3. [Open Innovation](challenges/open_innovation.md): bring your own open-source AI idea and prove the use of AI.

## First 10 minutes

1. Form a team (suggested: 2–4; solo allowed) and open one starter notebook.
2. Run all cells and read the baseline metrics. Ask a mentor if an error occurs.
3. Choose one **meaningful extension**, identify who does what, and begin implementing.
4. Keep evaluation reproducible, record failed attempts and explain limitations.
5. Create a **new public GitHub repository owned by your team**, including a README and an appropriate open-source license.
6. Use the [submission guide](docs/SUBMISSION_GUIDE.md) and official event submission flow.

Please check the [getting-started guide](docs/GETTING_STARTED.md) before the event. See the [schedule](docs/SCHEDULE.md), [judging rubric](docs/JUDGING_RUBRIC.md), and [FAQ](docs/FAQ.md).

## Local setup (optional)

Requires Python 3.10+ (3.11 recommended). You do **not** need a GPU.

~~~bash
git clone https://github.com/ThunderKhan/hack-ddu-ai-starter-kit.git
cd hack-ddu-ai-starter-kit
python -m venv .venv
# Windows PowerShell: .venv\Scripts\Activate.ps1
# macOS/Linux: source .venv/bin/activate
python -m pip install -r requirements.txt
python -m examples.digit_detective_demo
python -m examples.campus_router_demo
python -m unittest discover -s tests -v
python scripts/validate_notebooks.py
~~~

Running from the repository root is important for module imports. Notebooks are self-contained and can also be opened using local Jupyter if installed.

## What makes a valid project?

- A clear problem and a working demo
- Meaningful use of open-source AI code or an appropriately licensed open-weight model
- **An original contribution beyond the unchanged starter**
- A public GitHub repository containing source code, a suitable license, reproducible instructions, and a short limitations note
- Team members credited; evidence of testing and what changed

Official Hack Day category eligibility and prize winners are determined by the **current MLH organizer guidance**, not this repository. A classical ML library demo is not automatically eligible for every official AI prize. Ask an organizer to verify your chosen project's eligibility.

## For organizers and mentors

- [Mentor playbook](docs/MENTOR_GUIDE.md) — setup checks, troubleshooting, judging flow, offline fallback
- [Judging scorecard](templates/judging_scorecard.csv) — local 100-point rubric
- [Team README template](templates/TEAM_README_TEMPLATE.md) — copy into each team's own repo
- [Submission instructions](docs/SUBMISSION_GUIDE.md) — demonstration and official submission checklist

**Important:** Track A project submissions are separate from Track B's [Open Source AI Compass](https://github.com/ThunderKhan/open-source-ai-compass) issue contributions.

## Community and licensing

Educational starter code licensed under [MIT](LICENSE). Dataset/tool authors retain their own rights and licenses. Students must honor each library, model and dataset license used in their own projects. Follow [CONTRIBUTING.md](CONTRIBUTING.md) and our [Code of Conduct](CODE_OF_CONDUCT.md).

Official registration: https://events.mlh.com/events/15114-hacktoberfest-hack-day-gorakhpur-x-ddugu

Event website: https://hacktoberfest-ddugu.vercel.app/

Built for learning. Not affiliated with scikit-learn, Google Colab or third-party model providers.
