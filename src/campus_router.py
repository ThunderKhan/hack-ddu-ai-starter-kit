"""Fictional campus-message classifier starter.

All text examples are fabricated. This educational prototype should NOT be
used for real routing decisions or evaluated as production-ready software.
"""
from __future__ import annotations

import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.pipeline import make_pipeline

# Distinct, invented examples. No real student records or identifiers.
EXAMPLES = {
    "academics": [
        "Where can I find the semester examination timetable?",
        "How do I register for the mathematics course?",
        "My assignment submission deadline is approaching.",
        "Can someone explain the syllabus for machine learning?",
        "How can I request a transcript of my grades?",
        "The professor changed the classroom for tomorrow.",
        "I cannot see my laboratory marks in the grade portal.",
        "When does the next semester registration open?",
        "How should I apply for an academic elective?",
        "Is there a revision session before the physics exam?",
        "Where are the lecture notes for data structures?",
        "What are the prerequisites for the statistics class?",
        "I need guidance choosing my minor subject.",
        "The timetable shows two lectures at the same time.",
        "How do I submit my final year project report?",
        "Who can explain the practical examination format?",
    ],
    "facilities": [
        "The ceiling fan in the library room is not working.",
        "A classroom light needs repair near the entrance.",
        "There is a water leak beside the main corridor.",
        "The campus restroom needs cleaning supplies.",
        "The library reading tables are broken.",
        "Can the drinking water cooler be serviced?",
        "The hostel gate latch is damaged.",
        "The lecture hall projector cable is missing.",
        "Please repair the loose chair in the seminar room.",
        "The corridor window is stuck open.",
        "One of the campus benches has a broken plank.",
        "There is no drinking water near the sports field.",
        "The classroom air conditioner is making noise.",
        "The staircase railing needs inspection.",
        "A corridor light keeps flickering at night.",
        "Where do we report a damaged classroom desk?",
    ],
    "events": [
        "What time will the coding hackathon begin?",
        "Where can I register for the robotics workshop?",
        "Is the campus cultural festival happening this week?",
        "How do students join the debate competition?",
        "What is the venue for the guest lecture?",
        "Can we volunteer at the open source meetup?",
        "When will the sports tournament schedule be announced?",
        "Does the photography club have an upcoming exhibition?",
        "Where is the seminar on startup ideas taking place?",
        "Can our team apply for the innovation challenge?",
        "Is there a student community meetup tomorrow?",
        "Will the music event require advance registration?",
        "How can I attend the research poster session?",
        "Where do I collect my workshop participation pass?",
        "Are tickets available for the university theatre show?",
        "Who is organizing the coding contest this month?",
    ],
    "technical": [
        "My campus WiFi connection keeps disconnecting.",
        "I cannot reset my learning portal password.",
        "The login page displays an authentication error.",
        "Can IT help install the required development software?",
        "The student email system is not loading.",
        "I am unable to access the online course dashboard.",
        "The campus internet connection is very slow.",
        "How do I connect my laptop to the university network?",
        "The portal shows a server error when I upload files.",
        "My account has been locked after several login attempts.",
        "Where can I report a broken website link?",
        "The virtual classroom link says access denied.",
        "My authentication code is not being accepted.",
        "The registration website will not open in my browser.",
        "I need assistance with campus software setup.",
        "The online attendance app crashes on startup.",
    ],
}


def build_dataset() -> tuple[list[str], list[str]]:
    texts, labels = [], []
    for label, messages in EXAMPLES.items():
        texts.extend(messages)
        labels.extend([label] * len(messages))
    return texts, labels


def train_router(random_state: int = 42) -> dict:
    """Train/test split happens before fitting TF-IDF to prevent vocabulary leakage."""
    messages, labels = build_dataset()
    x_train, x_test, y_train, y_test = train_test_split(
        messages, labels, test_size=0.25,
        random_state=random_state, stratify=labels,
    )
    model = make_pipeline(
        TfidfVectorizer(ngram_range=(1, 2), min_df=1, sublinear_tf=True),
        LogisticRegression(max_iter=1500, random_state=random_state),
    )
    model.fit(x_train, y_train)
    predictions = model.predict(x_test)
    return {
        "model": model, "x_train": x_train, "x_test": x_test,
        "y_train": y_train, "y_test": y_test,
        "predictions": predictions,
        "accuracy": float(accuracy_score(y_test, predictions)),
        "report": classification_report(y_test, predictions, zero_division=0),
        "confusion_matrix": confusion_matrix(y_test, predictions, labels=list(EXAMPLES)),
    }


def route_message(model, message: str, threshold: float = 0.50) -> dict:
    """Return model confidence and optionally abstain on an uncertain prediction.

    Probabilities are model scores, not guarantees that the category is correct.
    """
    if not isinstance(message, str) or not message.strip():
        raise ValueError("Enter a nonempty message.")
    if not 0 <= threshold <= 1:
        raise ValueError("threshold must be between 0 and 1.")
    probabilities = model.predict_proba([message])[0]
    best = int(np.argmax(probabilities))
    label = str(model.classes_[best])
    confidence = float(probabilities[best])
    return {
        "category": label if confidence >= threshold else "needs human review",
        "suggested_category": label,
        "confidence": confidence,
        "needs_review": confidence < threshold,
    }
