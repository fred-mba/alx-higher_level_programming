## Python - Everything is object
- `id`: To get variable identifier (which is the memory address in the CPython implementation)
For example
    x = 42
    var_id = id(x)
    print("Variable identifier of x is: ", var_id")

### Files 103
    julien@ubuntu:/python3$ cat int.py
    a = 1
    b = 1
    julien@ubuntu:/python3$
- Small integers cached are usually -5 to 256(NSMALLPOSINTS + NSMALLNEGINTS). Both 'a' and 'b' are assigned value 1, falls within this range and no new objects are created. In this case 'a' and 'b' share the same id.

### Files 104
    julien@ubuntu:/python3$ cat int.py
    a = 1024
    b = 1024
    del a
    del b
    c = 1024
    julien@ubuntu:/python3$
- In this case, 1024 are outside the range typically cached by Cpython (-5 to 256). Therefore two distinct integer objects will be created.

### File 105
- `NSMALLPOSINTS`: Number of small positive integers that are cached. Typically they are integers from 0 to 257
- `NSMALLNEGINTS`: Number of small negative integers that are cached. Typically they are integers from 0 to -6
- These constants define range in which new objects are created leading to reduced memory overhead
- These caching mechanism aims to optimize frequently used integers in Cpython.

### Files 106
    guillaume@ubuntu:/python3$ cat string.py
    a = "SCHL"
    b = "SCHL"
    del a
    del b
    c = "SCHL"
    guillaume@ubuntu:/python3$
- In the first line `(a = "SCHL")`, a string object is created with the value "SCHL". In CPython string literals are subject to string interning.

- `String interning` is a process where the interpreter stores only one copy of each unique string literal, and subsequent references to the same string literal will reuse the existing object. This optimization helps save memory.

- Since "SCHL" is a string literal, CPython will typically intern it, and a will reference the same string object as b. Therefore, while a string object is technically created, it's important to note that string interning may result in the reuse of an existing object.

- In the second line `(b = "SCHL")`, no new string object is created. This is because, string "SCHL" is subject to string interning.

- When a string literal is encountered, CPython checks if an equivalent string object already exists in the interned string pool. If it does, the existing object is reused. In this case, since "SCHL" was already interned when a was assigned, b will reference the same existing string object, and no new object is created.

-  After the execution of `(del a)`, the string object pointed by a is not immediately deleted. The del statement removes the reference to the object but doesn't necessarily delete the object right away. The object will only be deleted when there are no more references to it.

- In this case, since b still references the same string object after the deletion of a, the string object is not immediately deleted. Only when `(del b)` is executed and there are no more references to the string object will it be eligible for garbage collection.