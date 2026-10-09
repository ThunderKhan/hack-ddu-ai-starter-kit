import unittest
from src.campus_router import EXAMPLES, build_dataset, route_message, train_router


class RouterTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.result = train_router()

    def test_balanced_fictional_examples(self):
        messages, labels = build_dataset()
        self.assertEqual(len(messages), 64)
        self.assertEqual(len(messages), len(set(messages)))
        self.assertEqual(set(labels), set(EXAMPLES))
        self.assertEqual({label: labels.count(label) for label in EXAMPLES},
                         {label: 16 for label in EXAMPLES})

    def test_holdout_is_reproducible(self):
        again = train_router()
        self.assertEqual(self.result["y_test"], again["y_test"])
        self.assertEqual(list(self.result["predictions"]), list(again["predictions"]))
        self.assertGreaterEqual(self.result["accuracy"], 0)
        self.assertLessEqual(self.result["accuracy"], 1)
        self.assertFalse(set(self.result["x_train"]) & set(self.result["x_test"]))

    def test_abstention(self):
        model = self.result["model"]
        prediction = route_message(model, "Campus WiFi login is broken", threshold=1.0)
        self.assertTrue(prediction["needs_review"])
        self.assertEqual(prediction["category"], "needs human review")
        self.assertIn(prediction["suggested_category"], EXAMPLES)

    def test_input_validation(self):
        model = self.result["model"]
        with self.assertRaises(ValueError):
            route_message(model, "   ")
        with self.assertRaises(ValueError):
            route_message(model, "Hello", threshold=-0.1)
        with self.assertRaises(ValueError):
            route_message(model, "Hello", threshold=1.5)


if __name__ == "__main__":
    unittest.main()
