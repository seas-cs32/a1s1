import sys
import pytest
from utils import file_relative_path, run


def test_provided_example():
    msg = "Down, down, down. Would the fall never come to an end!"
    actual_output = run(sys.executable, file_relative_path("../count32.py"), input=msg)
    assert "40 letter(s)\n" in actual_output
    assert "11 word(s)\n" in actual_output
    assert "2 sentence(s)\n" in actual_output
