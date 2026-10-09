"""Run with: python -m examples.campus_router_demo"""
from src.campus_router import route_message, train_router


def main():
    result = train_router()
    print("Held-out accuracy:", f"{result['accuracy']:.3f}")
    print(result["report"])
    for example in ["Where is the coding club workshop?", "My WiFi login failed", "Could you help?"]:
        print(repr(example), "=>", route_message(result["model"], example))
    print("This is a teaching demo, not a real campus routing system.")


if __name__ == "__main__":
    main()
