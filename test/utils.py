import os
import subprocess


def file_relative_path(rel_path: str) -> str:
    return os.path.join(os.path.dirname(__file__), rel_path)


def run(*args, **kwargs):
    computed_out = subprocess.run(args, capture_output=True, text=True, **kwargs)
    return computed_out.stdout
