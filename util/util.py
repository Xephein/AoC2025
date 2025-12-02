from os import path

def get_input(filename):
    with open(path.join(r"inputs/", filename)) as f:
        return f.read().strip("\n")

def parse_input(filename):
    return get_input(filename).split("\n")
