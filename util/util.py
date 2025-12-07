from os import path
from datetime import timedelta

def get_input(filename):
    with open(path.join(r"inputs/", filename)) as f:
        return f.read().strip("\n")

def parse_input(filename):
    return get_input(filename).split("\n")

def log_result(exercise, result, runtime):
    print(f"{exercise}: {result}.\nRuntime: {runtime:5f}s")
    return
