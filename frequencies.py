"""Frequencies function."""

def frequencies(items):
    frequencies = {}
    for value in items:
        string_value = str(value)
        if not string_value in frequencies:
            frequencies[string_value] = 1
        else:
            frequencies[string_value] += 1

    return frequencies
