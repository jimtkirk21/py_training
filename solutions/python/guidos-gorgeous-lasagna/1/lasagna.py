"""Functions used in preparing Guido's gorgeous lasagna.

Learn about Guido, the creator of the Python language:
https://en.wikipedia.org/wiki/Guido_van_Rossum

This is a module docstring, used to describe the functionality
of a module and its functions and/or classes.
"""
EXPECTED_BAKE_TIME = 40
PREPARATION_TIME = 2

def bake_time_remaining(time_in_oven):
    """Return the remaining bake time (in minutes) given the elapsed bake time."""
    remainig = EXPECTED_BAKE_TIME - time_in_oven
    return remainig

def preparation_time_in_minutes(number_of_layers):
    """Return the preparation time (in minutes) given the number of layers."""
    prep_time = PREPARATION_TIME * number_of_layers
    return prep_time

def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    """Return the total elapsed time (in minutes) given layers and bake time."""
    elapsed_bake_time = bake_time_remaining (elapsed_bake_time)
    elapsed_time = bake_time_remaining (elapsed_bake_time) + preparation_time_in_minutes(number_of_layers)
    return elapsed_time