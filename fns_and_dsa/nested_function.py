#!/usr/bin/env python3

"""A nested function showing the use of LEGB Function rule"""

# LEGB Function rule in action
def outer_func():
    """Enclosing function or global scope"""
    outer_var = 10
    def inner_func():
        """Nested function, local to enclosing function"""
        nonlocal outer_var
        outer_var += 5
        print(f'{outer_var}')
    
    inner_func()
    print(f"Modified value of outer_var={outer_var} from inner function")

outer_func()
