import TestFramework.src.base as taf


def test_example():
    taf.goToUrl("https://selenium.dev")


if __name__ == "__main__":
    taf.makeTest(test_example)
