import sys
import pytest
from utils import file_relative_path, run


def test_cat_in_hat():
    actual_output = run(
        sys.executable,
        file_relative_path("../read32.py"),
        "txts/CatInTheHat.txt",
    )

    with open(file_relative_path("../txts/CatInTheHat-soln4.txt")) as f:
        expected_output = "".join(f.readlines())

    assert expected_output == actual_output
