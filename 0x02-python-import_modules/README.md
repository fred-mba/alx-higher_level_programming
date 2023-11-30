### Python - import & modules

- `2-args.py file`:

    if arg_num > 0:
        for i, argv in enumerate(sys.argv[1:], start=1):
            print(f"{i}: {argv}")

    This code snippet is the same as:

    if arg_num > 0:
        for i in range(1, len(sys.argv)):
            print(f"{i}: {sys.argv[i]}")
