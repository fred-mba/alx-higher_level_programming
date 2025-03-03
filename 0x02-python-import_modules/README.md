## Python - import & modules
### Learning Objectives
- How to import functions from another file
- How to use imported functions
- How to create a [module](https://docs.python.org/3/tutorial/modules.html)
- How to use the built-in function dir()
- How to prevent code in your script from being executed when imported
- How to use [command line arguments](https://docs.python.org/3/tutorial/stdlib.html#command-line-arguments) with your Python programs

- `2-args.py file`:

    if arg_num > 0:
        for i, argv in enumerate(sys.argv[1:], start=1):
            print(f"{i}: {argv}")

    This code snippet is the same as:

    if arg_num > 0:
        for i in range(1, len(sys.argv)):
            print(f"{i}: {sys.argv[i]}")
