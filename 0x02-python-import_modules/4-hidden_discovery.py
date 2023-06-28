#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4

    all_dir = [name for name in dir(hidden_4) if not name.startswith("__")]

    for name in all_dir:
        print(name)
