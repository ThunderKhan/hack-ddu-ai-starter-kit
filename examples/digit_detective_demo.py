"""Run with: python -m examples.digit_detective_demo"""
from src.digit_detective import predict_digit, train_digit_model


def main():
    result = train_digit_model()
    print("Held-out accuracy:", f"{result['accuracy']:.3f}")
    print(result["report"])
    example = result["x_test"][0]
    prediction = predict_digit(result["model"], example)
    print("One example:", prediction, "actual:", int(result["y_test"][0]))
    print("Try changing the model, then report the same evaluation metric.")


if __name__ == "__main__":
    main()
