import unittest
import numpy as np
from src.digit_detective import predict_digit, train_digit_model


class DigitTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.result = train_digit_model()

    def test_shapes_and_stratification(self):
        result = self.result
        self.assertEqual(result["x_train"].shape[1], 64)
        self.assertEqual(result["x_test"].shape[1], 64)
        self.assertEqual(len(result["x_train"]) + len(result["x_test"]), 1797)
        self.assertEqual(set(result["y_train"]), set(range(10)))
        self.assertEqual(set(result["y_test"]), set(range(10)))

    def test_deterministic_baseline(self):
        again = train_digit_model()
        np.testing.assert_array_equal(self.result["predictions"], again["predictions"])
        self.assertGreater(self.result["accuracy"], 0.75)

    def test_prediction_confidence(self):
        value = predict_digit(self.result["model"], self.result["x_test"][0])
        self.assertIn(value["digit"], range(10))
        self.assertGreaterEqual(value["confidence"], 0)
        self.assertLessEqual(value["confidence"], 1)
        self.assertAlmostEqual(sum(value["probabilities"]), 1, places=5)

    def test_invalid_image_rejected(self):
        with self.assertRaises(ValueError):
            predict_digit(self.result["model"], [0] * 63)
        with self.assertRaises(ValueError):
            predict_digit(self.result["model"], [float("nan")] * 64)
        with self.assertRaises(ValueError):
            predict_digit(self.result["model"], [17] * 64)


if __name__ == "__main__":
    unittest.main()
