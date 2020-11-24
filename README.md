# Introduction

This command-line program lets you use python to process text files.

If you already like python's syntax, you might prefer this tool to `awk` or `sed`.


# Parameters

## --before (or -b)

The code to run before processing any text.

## --each-line (or -e)

The code to run on each line. The text of the line is stored in the string `_line` and the zero-based index of the line is stored in the integer `_i`.

Variables declared in `--before` will be available in `--each-line` unless you do something to make them out of scope.

## --after (or -a)

The code to run after the final line has been processed.

Variables declared in `--before` will be available in `--after` unless you do something to make them out of scope.


# Installation

Copy pipepy.py somewhere, make a soft link to it in /usr/local/bin/pipepy, set it to be executable.

Alternatively, copy pipepy.py somewhere, make it executable, and invoke it using "./pipepy.py".

TODO: Make this easier / friendlier / more complete.

# Examples


## Working with numbers

### Multiply each number by 5

```
echo -e "1\n2\n3\n4" | \
pipepy -e "print(int(_line) * 5)"
```

Input:
```
1
2
3
4
```

Output:
```
5
10
15
20
```

### Add numbers together

```
echo -e "1\n2\n3\n4" | \
pipepy --before "a=0" --each-line "a += int(_line)" --after "print(a)"
```

Input:
```
1
2
3
4
```

Output:
```
10
```


## Working with text

### Capitalize each line

```
echo -e "apple\nbanana\npear\nstrawberry\norange\nmango" | \
pipepy -e "print(_line.capitalize())"
```

Input:
```
apple
banana
pear
strawberry
mango
```

Output:
```
Apple
Banana
Pear
Strawberry
Orange
Mango
```

### Add time durations
```
echo -e "00:24:10\n01:05:55\n01:42:34" | \
pipepy \
    --before "from datetime import timedelta; total = timedelta()" \
    --each-line "a = _line.split(':') ; total += timedelta(hours=int(a[0]),minutes=int(a[1]),seconds=int(a[2]))" \
    --after "print(total)"
```


Input:
```
01:05:55
00:24:10
01:42:34
```


Output:
```
3:12:39
```

Arguably, this is too complicated to do as a "one-liner" and should be its own script.

## Using the index variable (`_i`)

### Multiply every third number by 5 and mark them as "modified"

```
echo -e "1\n2\n3\n4\n5\n6\n7\n8\n9\n10" | \
pipepy -e "print(_line) if _i % 3 != 2 else print(int(_line) * 5, '(modified)' )"
```

Input:
```
1
2
3
4
5
6
7
8
9
10
```

Output:
```
1
2
15 (modified)
4
5
30 (modified)
7
8
45 (modified)
10
```

# FAQ

### Couldn't someone learn `awk` or `sed` instead?
Yes

### The name "pipepy" is confusing. There's also "PyPy" and "PyPI".
That's true

### This program runs `exec()` on arbitrary user input. Isn't that a security risk?
No. Anything that you can do with this program, you can already do with `python -c`. It poses no additional security risk.

If you believe I'm wrong about this, please file an issue on the repository.

# TODO
- Defaults to using `/usr/bin/python3`. Is this a reasonable default? Should it be configurable?
- Come up with a better name than pipepy.

## Consider: Remove the need to call print()?

Would it be useful to remove the need to invoke "print()" when using the one-parameter version? Or would this be confusiing?

`pipepy.py "print(_line.capitalize())"` would become `pipepy.py "_line.capitalize()"

Should this be an option instead?


