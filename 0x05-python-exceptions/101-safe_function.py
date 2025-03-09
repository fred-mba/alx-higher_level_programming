#!/usr/bin/python3

def safe_function(fct, *args):
    # Executes function safely, handling exception
    # Returns None if something happens during the function
    try:
        return fct(*args)
    except Exception as ex:
        print(f'Exception: {ex}')
        return None
