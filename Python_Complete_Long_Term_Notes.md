# Python Complete Long-Term Notes
*Your Personal Python Handbook — Fundamentals → Advanced → DSA → Data/AI Ecosystem*

---

## How to use this document

- This is the **deep reference**. For fast lookup, use the companion **[PYTHON_QUICK_REFERENCE.md](./PYTHON_QUICK_REFERENCE.md)**.
- Each topic uses: What it is → Why it matters → Syntax → Examples → Methods table → Rules → Common mistakes → Practical use → Complexity (where relevant) → Remember. Small topics skip sections that don't apply.
- Search by heading — every `#`/`##` is a jump point.

---

## Table of Contents

- Part 1 — Python Fundamentals
- Part 2 — Control Flow
- Part 3 — Functions
- Part 4 — Data Structures Deep Dive
- Part 5 — Modules, Packages & Environment
- Part 6 — Exceptions
- Part 7 — Files & Data
- Part 8 — Object-Oriented Programming
- Part 9 — Advanced Python
- Part 10 — Date and Time
- Part 11 — Regular Expressions
- Part 12 — NumPy
- Part 13 — Pandas
- Part 14 — Data Visualization
- Part 15 — Python Data/AI Ecosystem
- Part 16 — Python for DSA (language features)
- Part 17 — DSA Fundamentals (algorithms & patterns)
- Part 18 — Web Development Overview
- Part 19 — Testing, Debugging & Code Quality
- Part 20 — Practice Bank
- Part 21 — Projects
- Final Python → DSA Checklist


---

## Part 1 — Python Fundamentals

### 1. What is Python?
Python is a **high-level, interpreted, general-purpose** programming language created by **Guido van Rossum**, first released in **1991**. It emphasizes readability with clean, English-like syntax.

**Key features:** simple/readable syntax, interpreted (no separate compile step — runs line by line), high-level (focuses on logic, not memory management), cross-platform (Windows/macOS/Linux), huge standard library, extensible with C/C++, open-source with massive community support, dynamically typed.

**Applications:** Web development, Data Science & Machine Learning, Automation/scripting, DevOps & Infrastructure, Cybersecurity, Game development, Desktop apps.

### 2. Installation & Execution Flow

1. Download from python.org, run installer, **check "Add Python to PATH"**.
2. Verify: `python --version` (or `python3 --version` on Linux/Mac).
3. Execution flow: **Write code (.py)** → **Interpreter reads it** → **Executes line by line** → **Output displayed**.

```python
# hello.py
print("Hello, World!")
```
Run with: `python hello.py`

### 3. Python Syntax, Comments & Indentation

- Python uses **indentation** (not braces `{}`) to define code blocks. Convention: 4 spaces.
- Single-line comment: `# comment`
- Multi-line / docstring comment: `"""this is a comment"""` or `'''...'''`

```python
if True:
    print("indented block")   # 4-space indent required
```
**Common mistake:** mixing tabs and spaces → `IndentationError`. Pick one (spaces recommended) and stay consistent.

### 4. Variables & Identifiers
A variable is a name bound to a value stored in memory. Python has **no explicit declaration** — assignment creates the variable.

```python
name = "Alice"     # str
age = 25           # int
price = 19.99      # float
is_active = True   # bool
```

**Naming rules:**

| Rule | Example (valid) | Example (invalid) |
|---|---|---|
| Start with letter/underscore | `_var`, `myVar` | `2value` |
| Letters, digits, underscore only | `count_1` | `my-var` |
| Case-sensitive | `myVar` ≠ `myvar` | — |
| Cannot use keywords | `class_` | `class` |
| No spaces/special chars | `user_name` | `user name`, `user@name` |

### 5. Keywords
Reserved words that can't be used as identifiers: `False, None, True, and, as, assert, async, await, break, class, continue, def, del, elif, else, except, finally, for, from, global, if, import, in, is, lambda, nonlocal, not, or, pass, raise, return, try, while, with, yield`. Check via `import keyword; keyword.kwlist`.

### 6. Data Types

| Type | Example | Description |
|---|---|---|
| `int` | `10`, `-25` | Whole numbers (arbitrary precision in Python) |
| `float` | `3.14`, `-0.001` | Decimal numbers |
| `complex` | `2+3j` | Complex numbers |
| `str` | `"Python"` | Immutable text sequence |
| `bool` | `True`, `False` | Boolean (subclass of int: `True==1`) |
| `list` | `[1,2,3]` | Ordered, **mutable** sequence |
| `tuple` | `(1,2,3)` | Ordered, **immutable** sequence |
| `set` | `{1,2,3}` | Unordered, unique elements |
| `dict` | `{'a':1}` | Key–value mapping |
| `NoneType` | `None` | Absence of a value |

**Key understanding:** Python names refer to objects, not memory boxes with fixed types — a name can be rebound to a different type later. This is why Python is "dynamically typed."

### 7. Type Conversion (Casting) & Type Checking
```python
int("10")      # str -> int : 10
float("3.14")  # str -> float : 3.14
str(100)       # int -> str : "100"
bool(0)        # -> False   (0, "", [], {}, None, 0.0 are all "falsy")
bool(1)        # -> True
list("abc")    # -> ['a','b','c']
set([1,1,2])   # -> {1, 2}
```

- **Implicit conversion**: Python auto-converts in some numeric operations (`int + float -> float`).
- **Explicit conversion**: you call `int()`, `float()`, `str()`, etc. Python does **not** silently convert `str` + `int` — that raises `TypeError`.
- Use `type(x)` to check the exact type, `isinstance(x, int)` to check type/subclass (preferred, supports inheritance).

**Common mistake:** `int("3.14")` raises `ValueError` — go through `float()` first: `int(float("3.14"))`.

### 8. Input and Output
```python
name = input("Enter your name: ")      # input() ALWAYS returns a string
age = int(input("Enter your age: "))   # convert explicitly for numbers
a, b = map(int, input("Two nums: ").split())   # multiple values on one line

print("A", "B", "C", sep="-", end="\n")   # A-B-C
print(f"Value of x is {10+5}")            # f-strings: cleanest formatting (Python 3.6+)
print("Name: {}, Age: {}".format("Bob", 25))  # .format() style
print("Name: %s, Age: %d" % ("Bob", 25))      # old %-style
```
**Escape sequences:** `\n` newline, `\t` tab, `\\` backslash, `\"` double quote, `\'` single quote, `\r` carriage return.

### 9. Operators & Precedence

| Category | Operators |
|---|---|
| Arithmetic | `+ - * / // % **` |
| Comparison | `== != > < >= <=` |
| Logical | `and or not` |
| Assignment | `= += -= *= /= //= %= **=` |
| Membership | `in`, `not in` |
| Identity | `is`, `is not` |
| Bitwise | `& \| ^ ~ << >>` |

```python
a, b = 10, 3
a / b    # 3.3333... (true division, always float)
a // b   # 3          (floor division)
a % b    # 1          (modulus/remainder)
a ** b   # 1000       (exponent)
```
**Precedence (high → low):** `()` → `**` → unary `+x -x ~x` → `* / // %` → `+ -` → shifts `<< >>` → `&` → `^` → `\|` → comparisons → `not` → `and` → `or`.
**Rule:** Use parentheses even when you know precedence — it prevents bugs and improves readability.

**`==` vs `is`:** `==` compares **values**; `is` compares **object identity** (same memory location). Use `==` for value equality; use `is` only for `None`/singleton checks (`x is None`).

### 10. Strings
Strings are **immutable, ordered** sequences of characters, enclosed in `'...'`, `"..."`, or `'''...'''`/`"""..."""` (triple-quoted = multi-line).

```python
s = "Python Programming"
s[0]        # 'P'        (indexing, 0-based)
s[-1]       # 'g'        (negative indexing from end)
s[0:6]      # 'Python'   (slicing: [start:stop:step], stop excluded)
s[::-1]     # reverses the string
s[::2]      # every 2nd character
```

**Common methods:**

| Method | Purpose | Example |
|---|---|---|
| `.lower()` / `.upper()` | case conversion | `"Py".lower()` → `"py"` |
| `.title()` / `.capitalize()` | word/sentence case | `"hello world".title()` → `"Hello World"` |
| `.strip()` / `.lstrip()` / `.rstrip()` | remove whitespace | `"  hi  ".strip()` → `"hi"` |
| `.replace(old,new)` | substitute | `"a-b".replace("-","_")` |
| `.split(sep)` | str → list | `"a,b".split(",")` → `['a','b']` |
| `.join(iterable)` | list → str | `"-".join(['a','b'])` → `"a-b"` |
| `.find(sub)` / `.index(sub)` | locate substring | `find` returns -1 if absent, `index` raises error |
| `.count(sub)` | count occurrences | `"banana".count("a")` → 3 |
| `.startswith()`/`.endswith()` | prefix/suffix check | `"file.txt".endswith(".txt")` |
| `.isdigit()/.isalpha()/.isalnum()` | content checks | — |
| `.format()` | template substitution | `"{} is {}".format("x",1)` |

**f-strings (preferred, Python 3.6+):**
```python
name, age = "Alice", 20
print(f"{name} is {age} years old.")     # Alice is 20 years old.
print(f"{3.14159:.2f}")                  # 3.14  (format spec)
```

**Deleting a string:** since strings are immutable objects, you don't "edit" them — you either rebind the name (`s = None`) or remove the name entirely (`del s`). Both just remove the reference; the object is garbage-collected if nothing else refers to it.

**`del` vs. assigning `None` vs. deleting a variable binding — the full picture:** these three actions look similar but do different things, and the distinction applies to *any* variable, not just strings.
```python
s = "Hello, World!"

s = None            # REBINDING: 's' now points to the None object instead.
                     # The original string object still exists in memory until
                     # nothing else references it (garbage collected). 's' itself
                     # is NOT deleted — it's still a valid name, just pointing elsewhere.
print(s)             # None  -> no error, s exists

del s                # UNBINDING: removes the NAME 's' from the current scope entirely.
print(s)             # NameError: name 's' is not defined  -> s no longer exists at all

my_list = [1, 2, 3]
del my_list[0]        # del also works on a single ELEMENT of a mutable collection -> [2, 3]
del my_list             # or the whole variable
```

| Action | What happens | Can you still use the name? |
|---|---|---|
| `s = None` | rebinds `s` to the `None` object | Yes — `s` exists, holds `None` |
| `del s` | removes the name `s` from scope | No — using `s` raises `NameError` |
| `del my_list[i]` | removes one element from a mutable collection | The collection still exists, just shorter |
| (strings are immutable) | you can never do `s[i] = 'x'` | `TypeError` — must rebind the whole name instead |

**Remember:** `None` is a value; `del` is an operation on the *name*, not a value. Assigning `None` says "this name now means nothing"; `del` says "this name no longer exists."

**Common mistake:** trying to mutate a string in place — `s[0] = 'X'` → `TypeError`. Build a new string instead (`s = 'X' + s[1:]`).

**Complexity:** indexing `O(1)`; slicing/concatenation `O(k)` where k = slice length; `in` search `O(n)`.

### 11. Lists
**Ordered, mutable** collection, allows duplicates and mixed types.
```python
fruits = ["apple", "banana", "cherry"]
fruits[0]                # 'apple'         - indexing
fruits[1:3]               # slicing
fruits.append("orange")   # add to end
fruits.insert(1, "mango") # insert at index
fruits.remove("banana")   # remove by value (first occurrence)
fruits.pop()               # remove & return last item (or pop(i))
fruits.sort()               # in-place sort
sorted(fruits)               # returns NEW sorted list
fruits.reverse()
len(fruits)
```
**Methods table:**

| Method | Purpose |
|---|---|
| `append(x)` | add item to end — O(1) amortized |
| `extend(iterable)` | append all items from another iterable |
| `insert(i,x)` | insert at index — O(n) |
| `remove(x)` | remove first matching value — O(n) |
| `pop(i=-1)` | remove & return item at index — O(1) at end, O(n) elsewhere |
| `clear()` | empty the list |
| `index(x)` | first index of x |
| `count(x)` | number of occurrences |
| `sort(key=,reverse=)` | in-place sort |
| `copy()` | shallow copy |

**Complexity cheat-sheet:** index/append/pop-last = O(1); insert/delete at arbitrary index, `in` search = O(n); sort = O(n log n).

### 12. Tuples
**Ordered, immutable** collection — use for fixed data, function returns, dictionary keys.
```python
point = (10, 20)
point[0]          # 10
x, y = point       # unpacking
t = (5,)            # single-element tuple NEEDS a trailing comma
t.count(2); t.index(2)
```
**Why tuples matter:** faster than lists, hashable (usable as dict keys/set members) if all elements are hashable, signal "this data shouldn't change" — self-documenting code.

### 13. Sets
**Unordered, mutable, unique elements only.**
```python
s = {1, 2, 3, 3}      # -> {1, 2, 3}, duplicates auto-removed
s.add(4)
s.remove(2)            # raises KeyError if absent
s.discard(2)            # no error if absent
a, b = {1,2,3}, {2,3,4}
a | b   # union {1,2,3,4}
a & b   # intersection {2,3}
a - b   # difference {1}
a ^ b   # symmetric difference {1,4}
```
**Practical use:** removing duplicates, fast membership testing (`in` is O(1) average vs O(n) for list), set algebra.
**Common mistake:** `{}` creates an empty **dict**, not an empty set — use `set()`.

### 14. Dictionaries
**Key–value pairs**, keys must be unique & hashable (immutable), insertion order preserved (Python 3.7+).
```python
student = {"name": "Alice", "age": 20, "is_student": True}
student["name"]              # access - KeyError if missing
student.get("name", "N/A")    # safe access with default
student["course"] = "Python"   # add/update
student.pop("age")             # remove & return value
student.keys(); student.values(); student.items()
for k, v in student.items():
    print(k, v)
```
**Methods table:**

| Method | Purpose |
|---|---|
| `get(key, default)` | safe read, no exception |
| `pop(key, default)` | remove & return |
| `setdefault(key, default)` | get if exists, else set & return default |
| `update(other)` | merge another dict in |
| `keys()/values()/items()` | dict views (live, reflect later changes) |

**Complexity:** average O(1) for get/set/delete (hash table); O(n) worst case with hash collisions.

### 15. Booleans & None
`True`/`False` (capitalized) are of type `bool`, a subclass of `int` (`True == 1`). `None` represents "no value" (Python's null) — use `is None` / `is not None` to check.


---

## Part 2 — Control Flow

### 1. if / elif / else
```python
marks = 75
if marks >= 90:
    grade = 'A'
elif marks >= 60:
    grade = 'B'
else:
    grade = 'C'
```
**Nested conditions:** an if/else block inside another — used when a decision depends on multiple layered conditions (e.g., login systems checking username, then password).

### 2. match-case (Python 3.10+)
Structural pattern matching — selects a block based on the value/shape of an expression.
```python
match day:
    case 1:
        print("Monday")
    case 2 | 3:               # OR-pattern
        print("Tue or Wed")
    case _:                    # default / wildcard
        print("Other day")
```
Use for clean multi-branch matching on fixed values, in place of long `if/elif` chains.

### 3. Loops
```python
for i in range(5):        # 0 1 2 3 4
    print(i)

for i in range(1, 10, 2):  # start, stop, step -> 1 3 5 7 9
    print(i)

i = 0
while i < 3:
    print(i)
    i += 1
```
`range(stop)`, `range(start, stop)`, `range(start, stop, step)` — `stop` is always excluded. `range()` is memory-efficient (generates values lazily, doesn't build a list).

### 4. break / continue / pass
```python
for i in range(1, 6):
    if i == 3:
        break        # exits the loop entirely
    print(i)          # 1 2

for i in range(1, 6):
    if i == 3:
        continue      # skips this iteration, continues loop
    print(i)          # 1 2 4 5

for i in range(3):
    pass               # does nothing — placeholder for future code / empty block
```

### 5. Nested loops
```python
for i in range(1, 3):
    for j in range(1, 3):
        print(f"i={i}, j={j}")
```
Used in matrix traversal, combinations, pattern printing. `break`/`continue` inside a nested loop only affects the **innermost** loop.

**Practical use:** loops are essential for iterating collections, reading files line by line, polling APIs, generating reports. Choose the right control statement to optimize flow.

### 6. `for...else` and `while...else`
Python loops can have an **`else` clause** — a feature many languages don't have. The `else` block runs **only if the loop finished naturally (without hitting a `break`)**.

**How it works:**

- If the loop completes all its iterations (or the `while` condition becomes False) → the `else` block **runs**.
- If the loop is exited early via `break` → the `else` block is **skipped**.
- `continue` does **not** affect the `else` — the loop can `continue` freely and still reach `else` as long as no `break` occurred.

```python
# for...else — classic use case: searching for something
def find_prime_factor(n):
    for i in range(2, n):
        if n % i == 0:
            print(f"{n} is divisible by {i}")
            break
    else:                          # runs only if the loop never hit 'break'
        print(f"{n} is prime")

find_prime_factor(7)     # 7 is prime               (loop completed -> else runs)
find_prime_factor(8)     # 8 is divisible by 2       (break hit -> else skipped)
```

```python
# while...else
i = 0
while i < 3:
    print(i)
    i += 1
else:
    print("Loop finished normally")     # runs, since no break occurred

i = 0
while i < 3:
    if i == 1:
        break
    print(i)
    i += 1
else:
    print("This will NOT print")          # skipped because break was hit
```
**Mental model:** think of loop-`else` as "**no-break**" — it answers the question "did this loop complete without being interrupted?" This is most useful for **search loops**: try to find something, and if you never found it (never broke out early), do the "not found" fallback in `else` instead of using an extra flag variable.

**Common mistake:** assuming `else` runs only when the loop body never executes at all (like an `if/else`) — that's wrong. It runs whenever the loop exits **without a `break`**, including when the loop ran zero times or ran to completion normally.


---

## Part 3 — Functions

### 1. Defining Functions
```python
def greet(name):
    """Greets the user."""       # docstring - optional but good practice
    msg = f"Hello {name}, welcome to Python!"
    return msg

result = greet("Alice")
print(result)
```
Functions organize code into reusable, testable units. A function with no `return` statement returns `None` by default.

### 2. Parameters, Arguments & Return Values

- **Parameters** = variables in the function definition. **Arguments** = actual values passed when calling.
- `return` sends a result back to the caller. A function can only return one object, but that object can be a collection (list/tuple/dict) to effectively return multiple values.
```python
def divmod_custom(a, b):
    return a // b, a % b        # returns a TUPLE (2, 1)
q, r = divmod_custom(7, 3)
```

### 3. Default & Keyword Arguments
```python
def greet(name, msg="Good morning"):     # default argument
    print(f"{msg}, {name}!")

greet("Alice")                    # Good morning, Alice!
greet("Bob", "Hello")              # Hello, Bob!
greet(name="Charlie", msg="Hi")    # keyword argument - order doesn't matter
```
**Rule:** default arguments must come **after** non-default arguments in the definition.
**Common mistake:** using a mutable default (`def f(x, lst=[])`) — the same list object is reused across calls! Use the standard pattern instead:
```python
def f(x, lst=None):
    if lst is None:
        lst = []
```

### 4. *args and **kwargs
```python
def sum_all(*args):            # collects extra positional args into a tuple
    return sum(args)
sum_all(1, 2, 3, 5)              # 11

def print_info(**kwargs):       # collects extra keyword args into a dict
    for key, value in kwargs.items():
        print(f"{key}: {value}")
print_info(name="Alice", age=25, city="Hyderabad")
```
Order in a definition: `def f(positional, *args, default=val, **kwargs):`

**Argument unpacking (calling side):**
```python
nums = [1, 2, 3]
print(*nums)             # unpacks list into positional args -> print(1,2,3)
d = {"name": "Bob", "msg": "Hi"}
greet(**d)                 # unpacks dict into keyword args
```

### 5. Scope & LEGB

| Scope | Where Defined | Accessible |
|---|---|---|
| Local | Inside a function | Only inside that function |
| Enclosing | In an outer (enclosing) function | Inner nested functions |
| Global | Outside any function (module level) | Anywhere in the module |
| Built-in | Python itself | Everywhere |

**LEGB** = the order Python searches names: **L**ocal → **E**nclosing → **G**lobal → **B**uilt-in.
```python
x = 20                 # global
def show():
    x = 10               # local — shadows global x inside this function
    print(x)             # 10
show()
print(x)                # 20 (global unaffected)
```

```python
def outer():
    x = "outer value"
    def inner():
        nonlocal x        # modifies the ENCLOSING scope's x
        x = "modified"
    inner()
    print(x)              # modified

count = 0
def increment():
    global count            # modifies the GLOBAL x
    count += 1
```
**Common mistake:** forgetting `global`/`nonlocal` when trying to modify an outer-scope variable inside a function — you'll get `UnboundLocalError` or accidentally create a new local variable instead.

### 6. Lambda Functions
Small, anonymous, single-expression functions.
```python
add = lambda a, b: a + b
print(add(5, 3))            # 8
square = lambda x: x * x
```
**Use case:** short throwaway functions, especially as arguments to `map()`, `filter()`, `sorted(key=...)`.

### 7. map(), filter(), reduce()
```python
nums = [1, 2, 3, 4]
doubled = list(map(lambda x: x * 2, nums))          # [2, 4, 6, 8]
evens = list(filter(lambda x: x % 2 == 0, nums))     # [2, 4]

from functools import reduce
total = reduce(lambda a, b: a + b, nums)              # 10 (cumulative)
```
`map()`/`filter()` return **iterators** in Python 3 — wrap in `list()` to see all results at once. `reduce()` must be imported from `functools` (not built-in since Python 3).

| Feature | List Comp | Dict Comp | map() | filter() | lambda |
|---|---|---|---|---|---|
| Returns | list | dict | iterator | iterator | function |
| Syntax | `[expr for x in it]` | `{k:v for x in it}` | `map(func, it)` | `filter(func, it)` | `lambda args: expr` |
| Best for | transform+filter | build dict from data | transform each item | select matching items | short callbacks |

**Interview tip:** comprehensions are usually more readable & often faster than `map`/`filter` + `lambda` in Python — prefer comprehensions unless piping into something that wants a function object.


---

## Part 4 — Data Structures Deep Dive

*(Builds on Part 1's list/tuple/set/dict basics — focuses on comprehensions, mutability, copying, and nested structures.)*

### 1. Comprehensions
```python
# List comprehension
squares = [x**2 for x in range(1, 6)]                  # [1, 4, 9, 16, 25]
evens = [x for x in range(10) if x % 2 == 0]             # filter form
# Dict comprehension
sq_map = {x: x**2 for x in range(1, 6)}                  # {1:1, 2:4, ...}
# Set comprehension
unique_evens = {x for x in range(1, 11) if x % 2 == 0}
# Nested comprehension
matrix = [[i*j for j in range(3)] for i in range(3)]
```
**Real-world use:** data transformation, quick filtering, building lookup maps, removing duplicates.
**Common mistakes:** forgetting `list()`/`{}` when needed; overusing nested comprehensions hurts readability — a regular loop can be clearer.

### 2. Mutability & Copying (Shallow vs Deep)

- **Mutable:** list, dict, set (can change in place).
- **Immutable:** int, float, str, tuple, frozenset, bool (cannot change in place — operations create new objects).

```python
import copy
original = [[1, 2], [3, 4]]

shallow = original.copy()          # or list(original) or original[:]
shallow[0][0] = 99                  # ALSO changes original[0][0]! (inner lists shared)

deep = copy.deepcopy(original)      # fully independent copy
deep[0][0] = 0                       # original is unaffected
```
**Mental model:** a shallow copy duplicates the outer container only; nested mutable objects are still shared by reference. A deep copy recursively duplicates everything.

**Common mistake — the classic "mutable default" / aliasing bug:**
```python
a = [1, 2, 3]
b = a          # b is NOT a copy — same object!
b.append(4)
print(a)        # [1, 2, 3, 4]  <- a changed too!
```

### 3. Unpacking
```python
a, b, c = [1, 2, 3]
first, *rest = [1, 2, 3, 4]        # first=1, rest=[2,3,4]
*init, last = [1, 2, 3, 4]          # init=[1,2,3], last=4
a, (b, c) = 1, (2, 3)                 # nested unpacking
```

### 4. Nested Structures
```python
data = {"students": [{"name": "A", "grades": [90, 85]}, {"name": "B", "grades": [70]}]}
data["students"][0]["grades"][1]     # 85
```
Common in JSON/API data — combine dict/list access chains carefully; use `.get()` at each level if keys may be missing.

**Complexity summary (average case):**

| Structure | Access | Search | Insert | Delete |
|---|---|---|---|---|
| list | O(1) by index | O(n) | O(n) / O(1) at end | O(n) / O(1) at end |
| dict | O(1) by key | O(1) | O(1) | O(1) |
| set | — | O(1) | O(1) | O(1) |
| tuple | O(1) by index | O(n) | immutable | immutable |


---

## Part 5 — Modules, Packages & Environment

### 1. Modules & Import
A **module** is a single `.py` file containing functions/classes/variables. A **package** is a directory of modules; traditionally it contains an `__init__.py` file (which can be empty) to mark it as a package and optionally run setup code on import — modern Python can also recognize a plain directory as a "namespace package" without one, but for beginner projects it's standard practice to include `__init__.py`.
```python
import math
print(math.sqrt(16))          # 4.0
print(math.pi)                  # 3.14159...

from math import sqrt, pi        # import specific members
from math import sqrt as sq       # alias
import numpy as np                # common convention

# mypackage/
#   __init__.py
#   math_ops.py
#   string_ops.py
```
**Built-in modules to know:** `math`, `random`, `datetime`, `os`, `sys`, `json`, `csv`, `re`, `collections`, `itertools`, `functools`, `pathlib`.

### 2. `__name__ == "__main__"`
```python
def main():
    print("Running as script")

if __name__ == "__main__":
    main()
```
When a file is **run directly**, `__name__` is set to `"__main__"`. When it's **imported** as a module elsewhere, `__name__` is the module's name instead — so this guard lets a file be both a reusable module and a runnable script.

### 3. pip & Package Management
```bash
pip install requests           # install a package
pip install pandas==2.1.4       # install specific version
pip list                         # list installed packages
pip uninstall requests           # remove
pip freeze > requirements.txt     # export exact installed versions
pip install -r requirements.txt    # install from a requirements file
```

### 4. Virtual Environments (venv)
Isolates a project's dependencies from the global Python install and other projects.
```bash
python -m venv myenv                  # create
myenv\Scripts\activate                 # activate (Windows)
source myenv/bin/activate               # activate (macOS/Linux)
pip install pandas numpy                 # install packages inside venv
deactivate                                # exit venv
```
**Why:** avoids version conflicts, keeps projects portable/reproducible, is standard professional practice.
**Common mistakes:** forgetting to activate venv before installing; committing the venv folder to Git (add it to `.gitignore` instead); confusing venv name with package name.


---

## Part 6 — Exceptions

### 1. try / except / else / finally
```python
try:
    x = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero")
except (TypeError, ValueError) as e:      # catch multiple types
    print(f"Error: {e}")
else:
    print("Runs only if NO exception occurred")
finally:
    print("Always runs — cleanup code goes here")
```
**Order matters:** `try` → `except` (one or more) → `else` (optional) → `finally` (optional). `finally` runs whether or not an exception occurred — ideal for closing files/connections.

### 2. Common Exception Types

| Exception | When it happens |
|---|---|
| `ZeroDivisionError` | dividing by zero |
| `ValueError` | right type, wrong value (`int("abc")`) |
| `TypeError` | wrong type for the operation |
| `IndexError` | list/string index out of range |
| `KeyError` | dict key not found |
| `AttributeError` | object has no such attribute/method |
| `FileNotFoundError` | file doesn't exist |
| `ImportError`/`ModuleNotFoundError` | module can't be found |
| `IOError` | input/output operation fails (e.g., file operations) |
| `StopIteration` | iterator exhausted (raised internally by `next()`) |

### 3. raise & Custom Exceptions
```python
def set_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative")

class InsufficientFundsError(Exception):        # custom exception - inherit from Exception
    """Raised when a withdrawal exceeds the balance."""
    pass

def withdraw(balance, amount):
    if amount > balance:
        raise InsufficientFundsError(f"Cannot withdraw {amount}, balance is {balance}")
```

### 4. Exception Hierarchy (essentials)
`BaseException` → `Exception` → (`ArithmeticError`, `LookupError`, `ValueError`, `TypeError`, `OSError`, ...). Catching `Exception` catches almost everything except system-exit signals (`SystemExit`, `KeyboardInterrupt`) which derive directly from `BaseException`.

### 5. Good Practices

- Catch **specific** exceptions, not a bare `except:` (hides real bugs).
- Use `finally` (or a `with` block) to guarantee cleanup (closing files/connections).
- Don't use exceptions for normal control flow where a simple `if` check suffices.
- Include meaningful messages when raising — future-you (or teammates) will read them in production logs.

**Practical use in file operations:**
```python
try:
    f = open("example.txt", "r")
except IOError:
    print("An error occurred")
finally:
    f.close()          # ensures the file is properly closed even if an exception occurs
```


---

## Part 7 — Files & Data

### 1. Opening & Modes
```python
f = open("data.txt", mode="r", encoding="utf-8")
```

| Mode | Meaning |
|---|---|
| `'r'` | Read (default). Errors if file doesn't exist |
| `'w'` | Write — **overwrites** the file if it exists, creates if not |
| `'a'` | Append — adds to end, doesn't overwrite |
| `'x'` | Create — fails if the file already exists |
| `'b'` | Binary mode (combine e.g. `'rb'`) |
| `'t'` | Text mode (default) |

### 2. Reading & Writing
```python
with open("data.txt", "r", encoding="utf-8") as f:
    content = f.read()            # entire file as one string
    # or:
    for line in f:                 # memory-efficient line-by-line iteration
        print(line.strip())
    # or:
    lines = f.readlines()           # list of lines

with open("output.txt", "w", encoding="utf-8") as f:
    f.write("Hello Python!\n")

with open("log.txt", "a", encoding="utf-8") as f:
    f.write("New log entry\n")       # appends, doesn't overwrite
```

### 3. `with` Statement (Best Practice)
`with` automatically closes the file when the block ends — **even if an exception occurs** — preventing resource leaks. Always prefer `with open(...)` over manual `open()`/`close()`.

### 4. CSV Files
```python
import csv
with open("data.csv", newline="", encoding="utf-8") as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)               # each row is a list of strings

with open("out.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["Name", "Age"])
    writer.writerow(["Alice", 25])

# DictReader / DictWriter - work with column names instead of positions
reader = csv.DictReader(open("data.csv"))
```

### 5. JSON Files
```python
import json
with open("data.json", "r") as f:
    data = json.load(f)             # JSON text -> Python dict/list

with open("info.json", "w") as f:
    json.dump({"name": "Alice", "age": 25}, f, indent=4)

json_string = json.dumps(data)       # dict -> JSON string (for APIs)
parsed = json.loads(json_string)     # JSON string -> dict
```
**JSON ↔ Python type mapping:** object↔dict, array↔list, string↔str, number↔int/float, true/false↔True/False, null↔None.

### 6. Directories — `os`, `pathlib`, `shutil`
```python
import os
os.listdir(".")            # list directory contents
os.path.exists("f.txt")     # check existence
os.makedirs("newdir")        # create a directory, including any missing intermediate directories
os.makedirs("newdir", exist_ok=True)   # don't raise an error if the target already exists
os.getcwd()                   # current working directory

from pathlib import Path      # modern, object-oriented (preferred over os.path)
p = Path("data") / "file.txt"
p.exists(); p.suffix; p.stem; p.parent
for file in Path(".").glob("*.csv"):
    print(file)

import shutil
shutil.copy("a.txt", "b.txt")
shutil.rmtree("folder")          # remove a directory tree
```
**Pro tip:** always handle exceptions around file operations (`try/except FileNotFoundError`) for robust code.


---

## Part 8 — Object-Oriented Programming

### 1. Classes & Objects
```python
class Person:
    species = "Homo sapiens"          # class variable - shared by ALL instances

    def __init__(self, name, age):     # constructor
        self.name = name                # instance variable - unique per object
        self.age = age

    def greet(self):                    # instance method - 'self' = the calling object
        return f"Hi, I'm {self.name}"

p = Person("Alice", 20)
print(p.greet())          # Hi, I'm Alice
print(Person.species)      # Homo sapiens (accessed via class)
```

- `self` is the instance itself — always the first parameter of instance methods (Python passes it automatically).
- **Class variables** are shared across all instances; **instance variables** belong to one object.

### 2. Class Methods & Static Methods
```python
class Circle:
    pi = 3.14159
    def __init__(self, r):
        self.r = r

    @classmethod
    def from_diameter(cls, d):        # takes 'cls' (the class) instead of 'self'
        return cls(d / 2)              # alternate constructor pattern

    @staticmethod
    def is_valid_radius(r):            # no 'self'/'cls' - just a regular function in the class's namespace
        return r > 0
```

| Type | First param | Access | Use case |
|---|---|---|---|
| Instance method | `self` | instance + class data | normal behavior |
| `@classmethod` | `cls` | class data only | alternate constructors, factory methods |
| `@staticmethod` | none | neither | utility function logically grouped with the class |

### 3. Encapsulation
```python
class Account:
    def __init__(self, balance):
        self._balance = balance       # convention: "protected" (single underscore)
        self.__pin = 1234              # "private" (double underscore -> name mangling)

    def get_balance(self):             # getter
        return self._balance
```
Python doesn't enforce true private access — `_x` is a convention ("don't touch this from outside"), `__x` triggers **name mangling** (`_ClassName__x`) making accidental external access harder but not impossible.

**`@property` — Pythonic getters and setters.** Rather than calling `obj.get_name()` / `obj.set_name(x)` explicitly, `@property` lets a method be **accessed like a plain attribute**, while still running code behind the scenes (validation, computed values, etc.).
```python
class Employee:
    def __init__(self, name):
        self._name = name

    @property
    def name(self):              # the "getter" - note: no parentheses needed when calling
        return self._name

    @name.setter
    def name(self, value):         # the "setter" - runs whenever someone does  e.name = "..."
        if not value:
            raise ValueError("Name cannot be empty")
        self._name = value

e = Employee("Alice")
print(e.name)          # "Alice"   <- looks like a plain attribute, but calls the getter method
e.name = "Bob"           # calls the setter, which can validate the new value
```
**Why it matters:** you can start with plain attributes and add validation/computed logic later via `@property` **without breaking any existing code** that reads/writes `obj.attribute` — the calling syntax never has to change.

### 4. Inheritance
```python
class Animal:
    def __init__(self, name):
        self.name = name
    def speak(self):
        return "..."

class Dog(Animal):                    # Dog inherits from Animal
    def speak(self):                   # method overriding
        return f"{self.name} says Woof!"

class Puppy(Dog):
    def speak(self):
        return super().speak() + " (puppy voice)"   # super() calls the parent's method
```
**Multiple inheritance:**
```python
class Flyable:
    def fly(self): return "Flying"
class Swimmable:
    def swim(self): return "Swimming"
class Duck(Flyable, Swimmable):        # inherits from both
    pass
```
Python resolves multiple inheritance via **MRO (Method Resolution Order)** — check with `ClassName.__mro__`.

### 5. Polymorphism & Abstraction
**Polymorphism** — the same method name behaves differently depending on the object:
```python
for animal in [Dog("Rex"), Animal("Generic")]:
    print(animal.speak())       # each calls its own version of speak()
```
**Abstraction** — hiding implementation details behind a simple interface, often via `abc`:
```python
from abc import ABC, abstractmethod
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass                     # subclasses MUST implement this

class Square(Shape):
    def __init__(self, side): self.side = side
    def area(self): return self.side ** 2
```
`Shape()` cannot be instantiated directly — it's abstract; only concrete subclasses that implement `area()` can be.

### 6. Magic / Dunder Methods
Special methods (double underscore) that let your objects work with Python's built-in syntax.

| Method | Triggered by | Purpose |
|---|---|---|
| `__init__` | `Obj()` | constructor |
| `__str__` | `print(obj)`, `str(obj)` | human-readable string |
| `__repr__` | `repr(obj)`, console echo | developer/debug string |
| `__len__` | `len(obj)` | define custom length |
| `__eq__` | `obj1 == obj2` | custom equality logic |
| `__add__` | `obj1 + obj2` | operator overloading |
| `__sub__` / `__mul__` / `__truediv__` / `__floordiv__` | `obj1 - obj2` / `*` / `/` / `//` | overload the other arithmetic operators the same way |
| `__getitem__` | `obj[i]` | indexing/slicing support |
| `__iter__` / `__next__` | `for x in obj` | make object iterable |
| `__enter__` / `__exit__` | `with obj as x` | context manager protocol |
| `__call__` | `obj()` | make instance callable like a function |

```python
class Point:
    def __init__(self, x, y): self.x, self.y = x, y
    def __add__(self, other): return Point(self.x+other.x, self.y+other.y)
    def __str__(self): return f"Point({self.x}, {self.y})"

p1, p2 = Point(1,2), Point(3,4)
print(p1 + p2)      # Point(4, 6)  <- __add__ + __str__ working together
```

**Common mistakes:** forgetting `self` in method definitions; modifying a mutable class variable expecting it to be per-instance (it's shared!); forgetting `super().__init__()` in a subclass constructor, losing parent initialization.


---

## Part 9 — Advanced Python

### 1. Iterators & Iterables
An **iterable** is anything you can loop over (`__iter__` defined) — list, str, dict, etc. An **iterator** is the object produced by `iter()` that actually tracks progress via `__next__()`.
```python
nums = [1, 2, 3]
it = iter(nums)          # get an iterator from the iterable
next(it)                  # 1
next(it)                  # 2
next(it)                  # 3
next(it)                  # raises StopIteration
```

### 2. Generators & `yield`
A generator is a function that **produces values lazily** (one at a time) using `yield` instead of building a full list in memory.
```python
def count_up(n):
    i = 1
    while i <= n:
        yield i          # pauses here, resumes on next call
        i += 1

for num in count_up(5):
    print(num)             # 1 2 3 4 5

gen_expr = (x**2 for x in range(5))    # generator expression (like list comp but lazy, uses () )
```
**Why it matters:** massive memory savings for large/infinite sequences — values are computed on demand, not stored all at once.

### 3. Decorators
A decorator wraps a function to add behavior without modifying its code.
```python
import functools
def timer(func):
    @functools.wraps(func)          # preserves original function's name/docstring
    def wrapper(*args, **kwargs):
        import time
        start = time.time()
        result = func(*args, **kwargs)
        print(f"{func.__name__} took {time.time()-start:.4f}s")
        return result
    return wrapper

@timer
def slow_function():
    import time; time.sleep(1)

slow_function()          # automatically timed
```
Common built-in decorators: `@staticmethod`, `@classmethod`, `@property`, `@functools.lru_cache`.

### 4. Closures
A closure is a nested function that "remembers" variables from its enclosing scope even after that scope has finished executing.
```python
def make_multiplier(factor):
    def multiply(x):
        return x * factor          # 'factor' is captured from the enclosing scope
    return multiply

double = make_multiplier(2)
print(double(5))       # 10
```
Decorators are built on closures.

### 5. Context Managers (`with`, `__enter__`/`__exit__`)
```python
class FileManager:
    def __init__(self, filename, mode):
        self.filename, self.mode = filename, mode
    def __enter__(self):
        self.file = open(self.filename, self.mode)
        return self.file
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()             # guaranteed cleanup, even on exception

with FileManager("data.txt", "r") as f:
    print(f.read())
```
Simpler alternative using `contextlib`:
```python
from contextlib import contextmanager
@contextmanager
def open_file(name, mode):
    f = open(name, mode)
    try:
        yield f
    finally:
        f.close()
```

### 6. Useful Built-in Functions

| Function | Purpose | Example |
|---|---|---|
| `enumerate(it)` | (index, value) pairs while looping | `for i, v in enumerate(lst):` |
| `zip(a, b)` | pair up multiple iterables | `for x, y in zip(a, b):` |
| `any(it)` | True if ANY element is truthy | `any([0, 0, 1])` → True |
| `all(it)` | True if ALL elements are truthy | `all([1, 1, 0])` → False |
| `sorted(it, key=, reverse=)` | returns new sorted list | `sorted(nums, reverse=True)` |
| `min()`/`max()` | smallest/largest, supports `key=` | `max(words, key=len)` |
| `sum(it, start=0)` | sum of elements | `sum([1,2,3])` → 6 |
| `callable(x)` | is x callable (function/class)? | — |
| `isinstance(x, T)` | type check (supports subclasses) | `isinstance(5, int)` |
| `id(x)` | object's memory identity | — |
| `hasattr/getattr/setattr` | dynamic attribute access | `getattr(obj, "name", "default")` |
| `reversed(it)` | reverse iterator | `list(reversed([1,2,3]))` |

**Quick worked examples for each (so every entry above has a concrete, runnable example):**
```python
# enumerate() - index + value together, optional start=
for i, fruit in enumerate(["apple", "banana"], start=1):
    print(i, fruit)                    # 1 apple  /  2 banana

# zip() - walk multiple iterables in parallel; stops at the SHORTEST one
names = ["A", "B"]; scores = [90, 85, 70]
list(zip(names, scores))                # [('A', 90), ('B', 85)]  <- 70 dropped, 'scores' longer

# any() / all()
any([0, 0, 3])        # True   - at least one truthy value
all([1, 1, 0])          # False  - not every value is truthy

# sorted() - key= and reverse=
sorted([-5, 2, -1], key=abs)             # [-1, 2, -5]  sorted by absolute value

# reversed() - returns an iterator, not a list
list(reversed([1, 2, 3]))                  # [3, 2, 1]

# callable() - checks if something can be called with ()
callable(len)         # True   (functions/classes/methods are callable)
callable(42)            # False  (an int is not callable)

# id() - unique identity (memory address in CPython) for the object's lifetime
a = [1, 2]
id(a) == id(a)          # True  - same object
id(a) == id([1, 2])       # False - different (equal-VALUE) object

# isinstance() - preferred over type() == ... because it respects inheritance
isinstance(True, int)     # True  - bool IS-A int (subclass)
isinstance([1,2], (list, tuple))    # True - accepts a tuple of types to check against

# hasattr() / getattr() / setattr() - dynamic attribute access
class Config: pass
cfg = Config()
setattr(cfg, "debug", True)        # dynamically create an attribute
hasattr(cfg, "debug")                # True
getattr(cfg, "debug")                 # True
getattr(cfg, "missing", "N/A")          # "N/A"  - safe default, no AttributeError
```

### 7. Functional Programming Concepts
Python supports functional-style code where **functions are first-class citizens** — they can be assigned to variables, passed as arguments, and returned from other functions. This underlies `map`/`filter`/`reduce`, decorators, and closures above. Functional style favors **immutability** and avoiding side effects (not changing state outside a function's own scope) for more predictable, testable code — though Python is not a purely functional language.

### 8. Modern Python Syntax (3.8+)
A handful of newer language features worth knowing, since they show up more and more in modern codebases:

**The walrus operator `:=` (Python 3.8+)** — assigns a value to a variable **as part of an expression**, instead of needing a separate statement first. Named for its resemblance to a walrus's eyes and tusks; officially called an "assignment expression."
```python
# Without walrus - two lines, computes len() only to use it once
n = len([1, 2, 3, 4, 5])
if n > 3:
    print(f"List is too long ({n} elements)")

# With walrus - assign AND test in one expression
if (n := len([1, 2, 3, 4, 5])) > 3:
    print(f"List is too long ({n} elements)")
```
**Practical use:** avoids computing the same value twice — common inside `while` loops reading input, or inside comprehension filters where you need the computed value again (`[y for x in data if (y := f(x)) is not None]`).

**Type hints** — optional annotations that document expected types; Python does **not** enforce them at runtime (they're for readers, IDEs, and external tools like `mypy`), but they make code self-documenting.
```python
age: int = 25                              # variable type hint
def greeting(name: str) -> str:              # parameter and return type hints
    return f"Hello, {name}!"

from typing import List, Tuple, Dict, Union
numbers: List[int] = [1, 2, 3]
person: Tuple[str, int] = ("Alice", 30)
scores: Dict[str, int] = {"Alice": 90}
identifier: Union[int, str] = "ID123"          # can legally hold either type
```

**Dictionary merge & update operators (Python 3.9+)** — `|` and `|=` merge dictionaries without needing `.update()` or `{**d1, **d2}`.
```python
dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}
merged = dict1 | dict2          # {'a': 1, 'b': 3, 'c': 4}  - dict2's values win on key conflicts
dict1 |= dict2                    # in-place merge (equivalent to dict1.update(dict2))
```

**Multiple context managers, parenthesized (Python 3.10+)** — cleaner syntax for opening several `with` resources at once, without backslash line-continuations:
```python
with (
    open('file1.txt') as f1,
    open('file2.txt') as f2,
):
    # both files open, both auto-closed on exit
    ...
```

---

## Part 10 — Date and Time

### 1. The `datetime` module — core classes

| Class | Represents |
|---|---|
| `date` | a calendar date (year, month, day) — no time component |
| `time` | a time of day (hour, minute, second, microsecond) — no date component |
| `datetime` | a combined date **and** time |
| `timedelta` | a **duration** — the difference between two dates/times |

```python
from datetime import date, datetime, timedelta

today = date.today()                    # current local date, e.g. date(2026, 9, 18)
now = datetime.now()                      # current local date AND time
print(today.year, today.month, today.day)
```

### 2. Creating dates/datetimes directly
```python
d = date(2024, 1, 15)                    # year, month, day
dt = datetime(2024, 1, 15, 10, 30, 0)      # + hour, minute, second
```

### 3. Date Arithmetic with `timedelta`
```python
from datetime import timedelta

tomorrow = today + timedelta(days=1)         # add a duration to a date
last_week = today - timedelta(weeks=1)         # subtract a duration
deadline = now + timedelta(hours=5, minutes=30)

diff = date(2024, 12, 31) - date(2024, 1, 1)     # subtracting two dates gives a timedelta
diff.days                                          # 365   - number of days between them
```
**Rule:** `date/datetime - date/datetime` → `timedelta`. `date/datetime ± timedelta` → `date/datetime`. You cannot add two dates together (there's no sensible meaning for "date + date").

### 4. Formatting — `strftime()` (date/time **object → string**)
```python
now.strftime("%Y-%m-%d")            # '2026-09-18'
now.strftime("%d/%m/%Y %H:%M:%S")     # '18/09/2026 14:30:05'
now.strftime("%B %d, %Y")               # 'September 18, 2026'
```

| Code | Meaning | Example |
|---|---|---|
| `%Y` | 4-digit year | 2026 |
| `%y` | 2-digit year | 26 |
| `%m` | month (01-12) | 09 |
| `%B` / `%b` | full / short month name | September / Sep |
| `%d` | day of month | 18 |
| `%A` / `%a` | full / short weekday name | Friday / Fri |
| `%H` | hour, 24-hour clock | 14 |
| `%I` | hour, 12-hour clock | 02 |
| `%M` | minute | 30 |
| `%S` | second | 05 |
| `%p` | AM/PM | PM |

### 5. Parsing — `strptime()` (**string → date/time object**)
```python
from datetime import datetime
parsed = datetime.strptime("18/09/2026", "%d/%m/%Y")     # string -> datetime object
parsed2 = datetime.strptime("2026-09-18 14:30", "%Y-%m-%d %H:%M")
```
**Mental model / mnemonic:** **`strftime`** = **"string FROM time"** (object → string, for display). **`strptime`** = **"string PARSED into time"** (string → object, for reading input). The **format-code string must match the input's actual layout exactly**, or `strptime` raises a `ValueError`.

### 6. Comparing Dates
```python
date(2024,1,1) < date(2024,6,1)      # True  - dates/datetimes support direct comparison operators
```

### 7. `pandas.date_range()`
Already introduced in Part 12 §11 — included here too since it's the Pandas-side counterpart to this section:
```python
import pandas as pd
pd.date_range('2024-01-01', periods=5, freq='D')      # 5 consecutive daily dates -> DatetimeIndex
pd.date_range('2024-01-01', '2024-01-31', freq='W')     # weekly dates within a range
```
**Common `freq` codes:** `'D'` day, `'W'` week, `'M'` month-end, `'MS'` month-start, `'Y'` year, `'H'` hour.

**Common mistakes:** confusing `strftime`/`strptime` direction; forgetting that `datetime.now()` returns a **naive** (timezone-unaware) datetime by default — for timezone-aware work, use `datetime.now(timezone.utc)` or the third-party `pytz`/`zoneinfo` (standard library since Python 3.9) modules.

---

## Part 11 — Regular Expressions

### 1. What & Why
Regex (`re` module) lets you search, match, and manipulate text using **patterns** rather than exact substrings — essential for validation, parsing logs, and text cleaning.

```python
import re
```

### 2. Core Functions

| Function | Purpose |
|---|---|
| `re.compile(pattern)` | turns a pattern into a reusable regex object (efficient if used repeatedly) |
| `re.search(pattern, s)` | finds the **first** occurrence anywhere in the string |
| `re.match(pattern, s)` | matches only at the **start** of the string |
| `re.fullmatch(pattern, s)` | matches the **whole** string against the pattern |
| `re.findall(pattern, s)` | returns a **list** of all matches |
| `re.finditer(pattern, s)` | returns an **iterator** of match objects (memory-efficient for many matches) |
| `re.split(pattern, s)` | splits a string wherever the pattern matches |
| `re.sub(pattern, repl, s)` | replaces the first occurrence of pattern with `repl` |
| `re.escape(s)` | escapes all special regex characters in `s` — for safely inserting user text into a pattern |
| `re.purge()` | clears the internal regex cache |

```python
re.findall(r'\d+', "I have 2 cats and 10 dogs")   # ['2', '10']
re.sub(r'\s+', ' ', "too   many   spaces")           # 'too many spaces'
m = re.search(r'(\d+)-(\d+)', "range: 10-20")
m.group(0)   # '10-20'   (whole match)
m.group(1)   # '10'      (first capture group)
```

### 3. Character Classes & Quantifiers

| Pattern | Meaning |
|---|---|
| `.` | any character except newline |
| `\d` / `\D` | digit / non-digit |
| `\w` / `\W` | word character (alnum+_) / non-word |
| `\s` / `\S` | whitespace / non-whitespace |
| `[abc]` | any of a, b, c |
| `[^abc]` | NOT a, b, or c |
| `[a-z]` | range |
| `*` | 0 or more | `+` | 1 or more |
| `?` | 0 or 1 (optional) |
| `{n}` / `{n,m}` | exactly n / between n and m times |
| `^` / `$` | start / end of string (anchors) |
| `\|` | OR |
| `()` | capture group |
| `(?:...)` | non-capturing group |

### 4. Practical Examples
```python
re.match(r'^\d{10}$', "9876543210")            # validate a 10-digit phone number
re.findall(r'[\w.-]+@[\w.-]+', text)             # extract emails
re.sub(r'[^a-zA-Z0-9]', '', "he!!lo@123")         # strip non-alphanumeric -> "helo123"
```
**Practical use:** form validation, log parsing, data cleaning before feeding into Pandas, web scraping.


---

## Part 12 — NumPy

### 1. What is NumPy?
NumPy (**Numerical Python**) is the foundational library for scientific computing in Python — it provides the `ndarray` (N-dimensional array) object and fast, vectorized operations. Pandas, SciPy, scikit-learn, and most of the ML/AI ecosystem are built on top of NumPy arrays.

**Why NumPy is faster than Python lists:**

- Implemented in C (optimized), stores data in one **contiguous memory block** (vs. lists of scattered Python object pointers), avoids per-element Python object overhead, and supports **vectorized operations** (apply an operation to a whole array at once, no explicit Python-level loop).

```python
import numpy as np
a = np.array([1, 2, 3, 4])          # 1-D array
b = np.array([[1, 2], [3, 4]])       # 2-D array (matrix)
```

### 2. Array Attributes
For `a = np.array([1, 2, 3, 4])`:

| Attribute | Meaning | Example |
|---|---|---|
| `a.shape` | dimensions (rows, cols, ...) | `(4,)` |
| `a.ndim` | number of axes/dimensions | `1` |
| `a.size` | total element count | `4` |
| `a.dtype` | data type of elements | `dtype('int64')` |
| `a.itemsize` | bytes per element | `8` |
| `a.nbytes` | total bytes used | `32` |

### 3. Array Creation
```python
np.array([1, 2, 3])              # from a Python list
np.zeros((2, 3))                    # array of 0s, shape (2,3)
np.ones((2, 3))                      # array of 1s
np.empty((2, 3))                      # uninitialized (faster, garbage values)
np.full((2, 3), 7)                     # filled with a constant
np.eye(3)                                # identity matrix
np.arange(0, 10, 2)                       # [0 2 4 6 8]  (like range(), but returns array)
np.linspace(0, 1, 5)                       # 5 evenly spaced numbers between 0 and 1 (inclusive)
np.logspace(1, 3, 4)                        # 4 numbers evenly spaced on a log scale
```
**Random arrays (modern API, preferred over legacy `np.random.*`):**
```python
rng = np.random.default_rng(42)        # create a seeded Generator (reproducible)
rng.random(5)                           # uniform [0,1)
rng.integers(1, 10, size=5)              # random ints in [low, high)
rng.normal(loc=0, scale=1, size=5)        # normal/Gaussian distribution
rng.choice([1,2,3,4], size=2, replace=False)
rng.shuffle(arr)                          # in-place shuffle
```
**Good practice:** always create your own `Generator` (`default_rng`) for reproducible, thread-safe randomness instead of relying on the legacy global `np.random.*` functions.

### 4. Data Types (dtype)

| Category | Types | Notes |
|---|---|---|
| Integer | `int8, int16, int32, int64` | signed; range grows with byte size |
| Unsigned int | `uint8, uint16, uint32, uint64` | no negative values |
| Float | `float16, float32, float64` | more bytes = more precision (float64 ≈ 15 decimal digits, float32 ≈ 7) |
| Boolean | `bool_` | `True`/`False`, 1 byte |
| Complex | `complex64, complex128` | real + imaginary parts |
| String | `<U10` etc. | fixed-length; longer strings get **silently truncated** |
| Datetime | `datetime64[D/h/m/s]` | dates/times |

```python
a = np.array([1, 2, 3], dtype=np.int32)
b = a.astype(np.float32)               # convert dtype - RETURNS A COPY, doesn't modify in place
```
**Why dtype matters (memory):** for 1 million integers, `int8` = ~1MB vs `int64` = ~8MB. **Use the smallest dtype that safely holds your data** for better memory usage and performance.
**Overflow/underflow:** a value exceeding the dtype's max wraps around (overflow); a value too small to represent becomes 0 (underflow, e.g. `np.float32(1e-50)` → `0.0`). Watch for this especially with small integer dtypes.

### 5. Indexing & Slicing
```python
a = np.array([10, 20, 30, 40, 50])
a[2]              # 30            - single element
a[1:4]             # [20 30 40]     - slice (VIEW, not a copy!)
a[-1]               # 50             - negative indexing
a[::2]               # [10 30 50]      - step slicing
a[a > 20]             # [30 40 50]       - boolean indexing (mask)
a[[0, 2, 4]]           # [10 30 50]        - fancy indexing (integer array)

b = np.array([[1,2,3],[4,5,6]])
b[0, 1]                 # 2     - 2D indexing
b[1, :]                  # [4 5 6]  - full row
```
**Critical distinction:**

| Expression | Returns | Type |
|---|---|---|
| `a[2]` | single element | scalar |
| `a[2:5]` | slice | **view** (shares memory with original!) |
| `a[[2,5,7]]` | elements at indices | **copy** |
| `a[a>10]` | elements matching condition | **copy** |

**Common mistake:** modifying a basic slice (`a[1:3][0]=99`) silently changes the original array because it's a view, not a copy — use `.copy()` explicitly if you need independence.

**Useful indexing functions:** `np.where(cond)` → indices where condition is True; `np.take(a, indices)`; `np.put(a, indices, values)`.

### 6. Reshaping & Array Manipulation
```python
a = np.arange(1, 7)                # [1 2 3 4 5 6]
a.reshape(2, 3)                       # new shape, same data
a.T                                     # transpose (swap rows/cols)
a.ravel()                                # flatten to 1D - returns a VIEW when possible
a.flatten()                               # flatten to 1D - always returns a COPY
a.resize(3, 2)                             # resize IN-PLACE

np.concatenate([a, b], axis=0)              # join along existing axis
np.stack([a, b])                              # join along a NEW axis
np.vstack([a, b])                              # stack vertically (axis=0)
np.hstack([a, b])                               # stack horizontally (axis=1)
np.split(a, 3)                                    # split into 3 equal parts
```

### 7. Broadcasting (Very Important)
Broadcasting lets NumPy operate on arrays of **different shapes** by virtually "stretching" the smaller one — no data is actually copied.

**Rules (align shapes from the right):**

1. Compare dimensions from right to left.
2. Dimensions are compatible if they're equal, **or** one of them is 1.
3. If one array has fewer dimensions, prepend 1s to its shape.
4. If any dimension pair is neither equal nor 1 → `Error`.

```python
a = np.array([1, 2, 3])          # shape (3,)
b = 10                              # scalar - broadcasts to every element
a + b                                 # [11 12 13]

a = np.array([[1,2,3],[4,5,6]])   # shape (2,3)
b = np.array([10, 20, 30])           # shape (3,) - broadcasts down the rows
a + b                                  # [[11 22 33],[14 25 36]]
```
**Compatible:** `(3,)` & `(3,1)` → `(3,3)` | `(2,1,5)` & `(1,4,5)` → `(2,4,5)`. **Incompatible:** `(2,3)` & `(3,2)` — neither dim matches nor is 1.
Use `np.newaxis` (or `None`) or `np.expand_dims()` to insert a new axis and make shapes compatible for broadcasting.

### 8. Vectorization
"Vectorization" = doing whole-array operations instead of writing explicit Python-level `for` loops — this is the #1 reason NumPy is fast (operations run in optimized C, not the slow Python interpreter loop).
```python
# SLOW (Python loop):
result = [x * 2 for x in big_list]
# FAST (vectorized):
result = big_array * 2
```
**Universal functions (ufuncs)** — fast element-wise operations, all vectorized by default: `np.add, np.subtract, np.multiply, np.divide, np.power, np.sqrt, np.exp, np.log, np.sin, np.cos, np.abs, np.maximum, np.minimum, np.floor, np.ceil`. Real-world speedups from vectorization are commonly **50–100x** over an equivalent Python loop.

### 9. Aggregation & Statistics

| Function | What it does |
|---|---|
| `sum()`, `mean()`, `median()` | total / average / middle value |
| `min()`, `max()` | extremes |
| `std()`, `var()` | standard deviation / variance |
| `argmin()`, `argmax()` | **index** of min/max |
| `cumsum()`, `cumprod()` | running total / running product |
| `percentile(a, p)`, `quantile(a, q)` | pth percentile / qth quantile |

**The `axis` parameter (most important concept here):**
```python
a = np.array([[1,2,3],[4,5,6]])       # shape (2,3)
a.sum(axis=0)      # [5 7 9]     - axis=0: DOWN the rows -> one value per COLUMN
a.sum(axis=1)       # [6 15]       - axis=1: ACROSS the columns -> one value per ROW
a.sum(axis=None)      # 21            - axis=None (default): flatten, single scalar
```
Mnemonic: **axis is the dimension that COLLAPSES.**

### 10. Searching & Sorting

| Function | Purpose |
|---|---|
| `np.sort(a)` | returns a sorted COPY |
| `np.argsort(a)` | returns indices that WOULD sort the array |
| `np.where(cond)` | indices where condition is True |
| `np.nonzero(a)` | indices of non-zero elements |
| `np.any(a)` / `np.all(a)` | True if any/all elements are truthy |
| `np.partition(a, k)` | partially sorts so the k-th smallest is in place |
| `np.searchsorted(a, v)` | index to insert v while keeping a sorted |

### 11. Missing / Invalid Values
```python
a = np.array([1.0, np.nan, np.inf, -np.inf])
np.isnan(a)          # [False True False False]
np.isinf(a)            # [False False True True]
np.isfinite(a)           # [True False False False]
np.nan_to_num(a)           # replaces nan->0, inf->large finite, -inf->large negative

np.nansum(a); np.nanmean(a); np.nanmax(a)     # NaN-aware aggregations - ignore NaNs
```
**Key distinction:** `None` is Python's null object (works anywhere); `np.nan` is a special **float** value used inside NumPy arrays to mark missing numeric data (`np.nan == np.nan` is actually `False` — always test with `np.isnan()`, never `==`).

### 12. Views vs Copies & Memory Model

- A **view** shares the same underlying data as the original (`arr.base` points to it); changing one changes the other.
- A **copy** owns independent memory (`arr.base is None`).
- Basic slicing (`a[1:4]`) → view. Fancy/boolean indexing (`a[[1,3]]`, `a[a>5]`) → copy.
- Check with `np.shares_memory(a, b)`.
```python
a.flags['C_CONTIGUOUS']       # True if stored row-major (NumPy's default, C-order)
a.strides                        # bytes to step to move along each dimension
```
**Performance tips:** prefer vectorized ops over loops; use broadcasting instead of manually tiling arrays; `np.empty` is faster than `np.zeros`/`np.ones` when you'll overwrite every value anyway; avoid unnecessary temporary arrays in chained operations; use in-place ops (`a += b`) to save memory when the original isn't needed.

### 13. Linear Algebra (`np.linalg`)

| Function | What it does |
|---|---|
| `np.dot(a,b)` / `a @ b` | dot product / matrix multiplication |
| `np.matmul(a,b)` | matrix multiplication (stacks of matrices aware) |
| `a.T` | transpose |
| `np.linalg.inv(A)` | matrix inverse (square matrices only) |
| `np.linalg.det(A)` | determinant |
| `np.linalg.matrix_rank(A)` | rank |
| `np.linalg.norm(v)` | vector/matrix norm (magnitude) |
| `np.linalg.eig(A)` | eigenvalues & eigenvectors |
| `np.linalg.solve(A, b)` | solve `Ax = b` (faster & more numerically stable than computing `inv(A) @ b`) |
| `np.linalg.svd(A)` | Singular Value Decomposition — powerful for dimensionality reduction, ML |
| `np.linalg.qr(A)` | QR decomposition |

**Note:** a singular matrix (determinant = 0) has no inverse — `np.linalg.inv` will raise an error; check `det()` first if unsure, or use `solve()` which avoids explicit inversion.

### 14. Advanced NumPy Operations
*(Specialized tools beyond everyday array work — useful for specific domains: tabular/mixed-type data, invalid-data handling, curve fitting, signal processing, and high-performance linear algebra.)*

#### 14.1 Structured / Record Arrays
**What:** an ndarray where each element is a "row" with **named fields of different dtypes** — like a lightweight, fixed-schema table (a precursor to what Pandas DataFrames formalize).
**Why:** lets you store heterogeneous, labeled data (e.g., name + age + height) in a single NumPy array instead of separate arrays or Python objects, while keeping NumPy's speed.
```python
dt = np.dtype([('name', 'U10'), ('age', 'i4'), ('height', 'f4')])
people = np.array([('Sam', 20, 175.5), ('Sita', 18, 160.2)], dtype=dt)
people['age']            # array([20, 18], dtype=int32)   - access a "column" by field name
people[0]                  # ('Sam', 20, 175.5)              - access a "row"
```
A **record array** (`np.rec.array`) is the same idea but additionally lets you access fields as attributes (`people.age` instead of `people['age']`).
**Limitation:** fixed schema (like a struct in C) — adding/removing fields means building a new array. For real tabular work with flexible columns, prefer Pandas.

#### 14.2 Masked Arrays (`numpy.ma`)
**What:** an array paired with a **boolean mask** that marks certain elements as "invalid" so they're automatically excluded from computations.
**Why:** cleanly handle missing/invalid values (sensor errors, corrupted readings) without manually filtering them out every time.
```python
import numpy.ma as ma
data = ma.array([1, 2, -999, 4], mask=[False, False, True, False])   # -999 marked invalid
data.mean()          # 2.333...   - automatically ignores the masked value
data.sum()             # 7          - masked element excluded from the sum
data.filled(0)           # [1, 2, 0, 4]  - replace masked entries with a fill value when needed
```
**Note:** similar in spirit to `np.nan`-based handling (Part 12 §11), but a masked array explicitly separates "the data" from "which values are valid," which is useful when 0/NaN could also be a legitimate value.

#### 14.3 NumPy Polynomial (`numpy.polynomial`)
**What:** tools for representing and working with polynomials (creation, evaluation, roots, fitting curves to data).
**Why:** avoids manually writing coefficient arithmetic — represents a polynomial as an object you can evaluate, differentiate, or fit to data points.
```python
from numpy.polynomial import Polynomial
p = Polynomial([1, 2, 3])        # represents 1 + 2x + 3x^2
p(2)                                # 17  -> 1 + 2*2 + 3*4 = 17  (evaluate at x=2)
p.roots()                             # roots of the polynomial
fitted = Polynomial.fit(x_data, y_data, deg=2)     # least-squares fit a degree-2 curve to data
```
**Practical use:** quick curve-fitting/trend modeling without pulling in a full ML library.

#### 14.4 FFT — Fast Fourier Transform (`np.fft`)
**What:** converts a signal from the **time domain to the frequency domain** — decomposes it into the sine/cosine frequencies that compose it.
**Why:** used in signal processing, audio analysis, image processing, and detecting periodicity/cycles in data.
```python
signal = np.random.rand(8)
freq_data = np.fft.fft(signal)          # forward transform: time domain -> frequency domain
recovered = np.fft.ifft(freq_data)        # inverse transform: frequency domain -> time domain (recovers original)
```
**Note:** this is a specialized topic — the key takeaway for a Python learner is *what it's for* (finding frequency components in data), not memorizing the full signal-processing theory behind it.

#### 14.5 Binning / Digitization (`np.digitize`)
**What:** assigns each value in an array to a **bin index** based on a set of bin-edge boundaries.
**Why:** used to bucket continuous data into discrete categories (e.g., grouping ages into age-brackets, or continuous scores into grade bands).
```python
values = np.array([5, 12, 17, 25])
bins = np.array([0, 10, 20, 30])              # bin edges: [0-10), [10-20), [20-30)
np.digitize(values, bins)                        # [1 2 2 3]  - index of the bin each value falls into
```

#### 14.6 `np.argpartition()`
**What:** like `np.partition` (Part 12 §10), but returns the **indices** that would partition the array around the k-th smallest element, instead of the partitioned values themselves.
**Why:** the fastest way to get the **indices of the top-k / bottom-k elements** of a large array without fully sorting it (avoids the O(n log n) cost of a full sort when you only need k elements).
```python
a = np.array([7, 2, 9, 4, 3, 8])
idx = np.argpartition(a, 2)              # indices such that a[idx[:2]] are the 2 smallest (unordered among themselves)
a[idx[:2]]                                  # the 2 smallest values, e.g. [2, 3]
```
**Practical use:** exactly the "find top-10 largest values from a huge array" pattern shown in Part 11 §10 — `argpartition` is the O(n) step that makes it fast.

#### 14.7 `np.einsum()` — Einstein Summation
**What:** a compact, general notation for expressing sums, products, transposes, and contractions over array axes in one expression — one function that can replace many separate calls to `dot`, `matmul`, `transpose`, `sum`, etc.
**Why:** for complex tensor operations (common in ML), `einsum` is often both more readable (once you know the notation) and faster than chaining multiple NumPy calls, because it can avoid building unnecessary intermediate arrays.
```python
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])

np.einsum('ij,jk->ik', A, B)      # matrix multiplication  (same as A @ B)
np.einsum('ii', A)                  # trace (sum of diagonal) - same as np.trace(A)
np.einsum('ij->ji', A)                # transpose - same as A.T
np.einsum('ij,ij->', A, B)              # sum of element-wise product (like np.sum(A*B))
```
**Note:** the string `'ij,jk->ik'` means "for input axes labeled i,j and j,k, sum over the repeated index j, output axes i,k" — this is the core Einstein-summation convention. It has a learning curve, but is worth recognizing since it appears often in ML codebases.


---

## Part 13 — Pandas

### 1. What is Pandas?
Pandas is a Python library for **data manipulation and analysis**, built on top of NumPy. It provides two core structures: **Series** (1-D labeled) and **DataFrame** (2-D labeled, like a spreadsheet/SQL table). Why use it: easy handling of structured data, powerful cleaning/aggregation tools, integrates with NumPy/Matplotlib/scikit-learn.

```python
import pandas as pd
```

### 2. Series
```python
s = pd.Series([10, 20, 30, 40])              # default index 0..n-1
s2 = pd.Series([10, 20, 30], index=['a','b','c'])   # custom index
s['a']              # 10 - access by label
s.iloc[0]             # 10 - access by position
s[s > 15]              # boolean filtering
s.sort_values(); s.sort_index()
s.isna(); s.notna(); s.fillna(0); s.dropna()
s.count(); s.sum(); s.mean(); s.min(); s.max(); s.std(); s.median()
```

### 3. DataFrame — Creation
```python
# from a dict of lists (most common)
df = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 28],
    'City': ['Delhi', 'Mumbai', 'Kolkata']
})
df = pd.DataFrame(np_array, columns=['A','B','C'])   # from a NumPy array
df = pd.read_csv('data.csv')                            # from CSV
df = pd.read_excel('data.xlsx', sheet_name='Sheet1')      # from Excel
df = pd.read_json('data.json')                              # from JSON
df = pd.read_sql('SELECT * FROM t', conn)                     # from SQL
```

### 4. Inspection

| Method | Purpose |
|---|---|
| `df.head(n)` / `df.tail(n)` | first/last n rows (default 5) |
| `df.shape` | (rows, columns) |
| `df.columns` | column labels |
| `df.index` | row labels |
| `df.dtypes` | data type of each column |
| `df.info()` | summary: dtypes, non-null counts, memory |
| `df.describe()` | statistics (count, mean, std, min, quartiles, max) for numeric columns |
| `df.value_counts()` | frequency of unique values (on a Series/column) |
| `df.nunique()` | number of unique values per column |

### 5. Selection — `loc` vs `iloc`
```python
df['Name']                    # single column -> Series
df[['Name', 'Age']]            # multiple columns -> DataFrame
df.loc[1:2, ['Name','City']]     # LABEL-based: rows/cols by NAME, end-inclusive
df.iloc[0:3, 0:2]                  # POSITION-based: rows/cols by INTEGER, end-exclusive
df.at['row_label', 'col']            # single value, label-based (fast)
df.iat[2, 3]                           # single value, position-based (fast)
```
**Decision rule:** use `loc` when you know row/column **names**; use `iloc` when you know **positions**. `loc` slicing is inclusive of the end label; `iloc` slicing (like Python lists) excludes the end position.

### 6. Filtering
```python
df[df['Age'] > 25]                                        # boolean filter
df[(df['Age'] > 21) & (df['City'] == 'Delhi')]              # multiple conditions - use & | ~, NOT and/or
df[df['City'].isin(['Delhi', 'Mumbai'])]                      # membership test
df[df['Age'].between(20, 30)]                                   # inclusive range
df.query("Age > 21 and City == 'Delhi'")                         # string-based query syntax
```
**Common mistake:** using Python's `and`/`or` instead of `&`/`|` on boolean Series — raises an ambiguity error. Also always wrap each condition in parentheses because `&`/`|` have higher precedence than comparisons.
**Tip:** use `.copy()` after filtering if you intend to modify the result, to avoid the `SettingWithCopyWarning`.

### 7. Adding / Removing Columns
```python
df['Age_plus_5'] = df['Age'] + 5                  # add/derive a new column
df['Category'] = df['Age'].apply(lambda x: 'Senior' if x > 60 else 'Adult')
df.drop('City', axis=1, inplace=True)                # remove a column (axis=1) - or columns=['City']
df.drop(0, axis=0)                                     # remove a row (axis=0)
df.rename(columns={'Age': 'Years'}, inplace=True)
```

### 8. Missing Data & Cleaning
```python
df.isnull().sum()               # count missing values per column
df.dropna()                       # drop rows with ANY missing value
df.dropna(subset=['Age'])           # drop rows missing in specific column
df.fillna(0)                          # fill missing with a constant
df.fillna(df['Age'].mean())             # fill with column mean (common technique)
df.duplicated().sum()                     # count duplicate rows
df.drop_duplicates()                        # remove duplicates
df['Age'] = df['Age'].astype(int)             # type conversion
```

### 9. Sorting, Grouping & Aggregation
```python
df.sort_values('Age')                                    # ascending by default
df.sort_values('Age', ascending=False)
df.sort_values(['City','Age'])                             # multi-column sort

df.groupby('City')['Age'].mean()                             # group then aggregate
df.groupby('City').agg({'Age': 'mean', 'Name': 'count'})        # multiple aggregations
df.groupby('City').size()                                         # group counts
```

### 10. Merging & Joining
```python
pd.merge(df1, df2, on='id', how='inner')      # SQL-style join: 'inner','left','right','outer'
pd.concat([df1, df2], axis=0)                    # stack rows
pd.concat([df1, df2], axis=1)                     # stack columns side-by-side
df1.join(df2, on='key')                             # join on index
```

### 11. Dates & Time Series
```python
pd.date_range('2024-01-01', periods=5, freq='D')       # DatetimeIndex
df['date'] = pd.to_datetime(df['date_str'])               # parse strings to datetime
df['year'] = df['date'].dt.year                              # extract components (.dt.month, .day, etc)
df.set_index('date').resample('M').mean()                       # resample to monthly averages
now = pd.Timestamp.now()
```

### 12. Reading/Writing Common Files
```python
pd.read_csv('f.csv'); df.to_csv('out.csv', index=False)
pd.read_excel('f.xlsx'); df.to_excel('out.xlsx', index=False)
pd.read_json('f.json'); df.to_json('out.json')
```
**Complexity/practical note:** groupby/merge on large DataFrames can be expensive — index the join columns, and filter data down *before* expensive operations where possible.


---

## Part 14 — Data Visualization

### 1. Matplotlib — the foundation
```python
import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [10, 20, 15, 30, 25]
plt.plot(x, y, marker='o')            # line plot
plt.title('Line Plot Example')
plt.xlabel('X axis'); plt.ylabel('Y axis')
plt.legend(['series 1'])
plt.show()

plt.bar(categories, values)             # bar chart
plt.scatter(x, y)                         # scatter plot
plt.hist(data, bins=20)                     # histogram
plt.pie(values, labels=labels)                # pie chart

fig, axes = plt.subplots(1, 2, figsize=(10,4))   # multiple subplots in a grid
axes[0].plot(x, y)
axes[1].bar(categories, values)
```

### 2. Seaborn — statistical visualization built on Matplotlib
```python
import seaborn as sns
sns.barplot(x='City', y='Age', data=df)
sns.lineplot(x='date', y='value', data=df)
sns.scatterplot(x='a', y='b', hue='category', data=df)
sns.histplot(df['Age'], kde=True)            # histogram + density curve
sns.boxplot(x='City', y='Age', data=df)         # spot outliers, spread
sns.heatmap(df.corr(), annot=True)                # correlation matrix, annotated
plt.title('Average Age by City')
plt.show()
```
Seaborn works seamlessly with Pandas DataFrames and NumPy arrays, and adds nicer defaults/statistical plot types (box, violin, heatmap, pairplot) on top of Matplotlib.

### 3. Basic Visualization Workflow

1. Clean & prepare data (Pandas).
2. Choose the right chart for the question: **line** = trend over time; **bar** = compare categories; **scatter** = relationship between 2 numeric variables; **histogram** = distribution of one variable; **heatmap** = correlations/matrices; **box plot** = spread & outliers.
3. Add labels, titles, and a legend — an unlabeled chart is not useful.
4. `plt.show()` to render (or `plt.savefig('chart.png')` to export).


---

## Part 15 — Python Data/AI Ecosystem

NumPy sits at the heart of the scientific Python ecosystem — nearly everything else is either built on it or interoperates with its arrays.

| Library | Built on | Role |
|---|---|---|
| **NumPy** | — (foundation) | N-dimensional arrays, fast numerical computing, the common data language all others share |
| **SciPy** | NumPy | Advanced scientific algorithms: optimization, integration, linear algebra, statistics, signal processing |
| **Pandas** | NumPy | Labeled tabular data structures (Series/DataFrame), data manipulation & analysis |
| **Matplotlib** | NumPy | 2D plotting — charts, histograms, scatter plots |
| **Seaborn** | Matplotlib | Statistical visualization with nicer defaults, built on Matplotlib |
| **Scikit-learn** | NumPy, SciPy, Matplotlib | Classical machine learning: classification, regression, clustering, preprocessing |
| **JAX** | NumPy-compatible API | High-performance numerical computing — autograd (automatic differentiation) + JIT compilation, great for research |
| **PyTorch** | Built on tensors (NumPy-like) | Popular deep learning framework, dynamic computation graphs, GPU acceleration |
| **TensorFlow** | Built on tensors | End-to-end platform for ML/deep learning at scale |

**Which is "core Python" vs. a library:** none of NumPy/Pandas/Matplotlib/Seaborn/SciPy/Scikit-learn/TensorFlow/PyTorch/JAX ship with base Python — all are installed via `pip`. Only the standard library (`math`, `os`, `json`, `re`, `collections`, etc.) is core Python.

**Key takeaway:** you don't need to memorize every library's internals — **master NumPy arrays first** (shape, dtype, indexing, broadcasting, vectorization). That single mental model — the ndarray — is what every other library in this ecosystem is speaking underneath its own API.

**A minimal scikit-learn example (pattern to recognize, not memorize yet):**
```python
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
clf = DecisionTreeClassifier()
clf.fit(X_train, y_train)                 # train
y_pred = clf.predict(X_test)                # predict
print(accuracy_score(y_test, y_pred))          # evaluate
```


---

## Part 16 — Python for DSA (Language Features)

*Keep this separate mentally from Part 16 (actual algorithms): this part is "which Python tool do I reach for," Part 16 is "how does the algorithm work."*

### 1. Core containers for DSA

| Need | Python tool | Notes |
|---|---|---|
| Dynamic array | `list` | append/pop-end O(1); insert/delete elsewhere O(n) |
| Fixed tuple / hashable key | `tuple` | usable as dict key / set member |
| Hash map | `dict` | O(1) avg get/set/delete |
| Hash set | `set` | O(1) avg membership test |
| Stack (LIFO) | `list` | `append()`=push, `pop()`=pop — both O(1) |
| Queue (FIFO) | `collections.deque` | `append()`/`popleft()` both O(1) — **never use a plain list as a queue**, `pop(0)` is O(n) |
| Double-ended queue | `collections.deque` | O(1) at both ends |
| Priority queue / heap | `heapq` (module, operates on a list) | min-heap by default |

### 2. `collections` module — essential for DSA
```python
from collections import Counter, defaultdict, deque, OrderedDict, namedtuple

Counter("mississippi")                 # Counter({'i': 4, 's': 4, 'p': 2, 'm': 1}) - frequency map
Counter([1,1,2,3]).most_common(2)         # [(1, 2), (2, 1)] - top-k frequent items

dd = defaultdict(list)                     # auto-creates a default value on missing key access
dd['key'].append(1)                          # no KeyError, even though 'key' never existed before

dq = deque([1,2,3])
dq.appendleft(0); dq.append(4)                # O(1) both ends -> deque([0,1,2,3,4])
dq.popleft()                                    # O(1)

Point = namedtuple('Point', ['x', 'y'])            # lightweight, readable tuple-based records
p = Point(1, 2); p.x                                 # 1
```

### 3. `heapq` — priority queue
```python
import heapq
heap = [5, 1, 8, 3]
heapq.heapify(heap)              # O(n) - convert list to min-heap in place
heapq.heappush(heap, 2)             # O(log n)
smallest = heapq.heappop(heap)        # O(log n) - always removes the SMALLEST
heapq.nlargest(3, heap)                 # top-3 largest
heapq.nsmallest(3, heap)                  # top-3 smallest
# Max-heap trick: push negated values, since heapq is min-heap only
heapq.heappush(heap, -value)
```

### 4. Recursion
```python
def factorial(n):
    if n <= 1:               # base case - ALWAYS define one, or infinite recursion
        return 1
    return n * factorial(n - 1)          # recursive step - must move toward the base case
```
**Caution:** Python's default recursion depth limit is ~1000 (`sys.getrecursionlimit()`). Deep recursion can fail (`RecursionError`) even when the algorithm is logically correct — consider an iterative approach or increase the limit cautiously (`sys.setrecursionlimit()`) for genuinely deep-but-safe recursion.

### 5. Sorting for DSA
```python
sorted(nums)                                 # returns a new sorted list, O(n log n), Timsort
sorted(nums, reverse=True)
sorted(words, key=len)                         # custom sort key
sorted(people, key=lambda p: (p.age, p.name))    # multi-key sort (tuple key)
nums.sort()                                        # in-place variant of the above
```
`sorted()`/`.sort()` use **Timsort** — O(n log n) worst case, stable (equal elements keep relative order), and O(n) best case on already-sorted data.

### 6. Binary Search
```python
import bisect
bisect.bisect_left(sorted_list, x)     # leftmost insertion point keeping sorted order
bisect.bisect_right(sorted_list, x)      # rightmost insertion point
bisect.insort(sorted_list, x)              # insert x while keeping the list sorted

def binary_search(arr, target):
    lo, hi = 0, len(arr) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if arr[mid] == target: return mid
        elif arr[mid] < target: lo = mid + 1
        else: hi = mid - 1
    return -1
```

### 7. Enumerate, Zip, Slicing, Unpacking (DSA patterns)
```python
for i, val in enumerate(arr):          # index+value together, cleaner than range(len(arr))
    ...
for a, b in zip(list1, list2):          # walk two lists in parallel
    ...
arr[::-1]                                 # reverse
arr[::2]                                   # every other element
first, *middle, last = arr                   # unpack ends, grab the rest
```

### 8. Efficient Input/Output (competitive programming)
```python
import sys
data = sys.stdin.read().split()          # fast bulk input, much faster than repeated input()
print('\n'.join(results))                   # batch output once instead of many print() calls
```

### 9. Mutable vs Immutable & References (crucial for DSA correctness)

Python passes **object references** (this is sometimes called "pass by object reference" or "call by object sharing" — it's neither strictly pass-by-value nor pass-by-reference in the C/C++ sense). When you pass an argument into a function, the parameter name becomes another reference to the **same object**:

- If that object is **mutable** (list, dict, set) and the function **mutates it in place** (`.append()`, `.update()`, item assignment), the change is visible to the caller too, because both names point to the same object.
- If the function instead **rebinds** the parameter name to a new object (`lst = [1, 2, 3]` inside the function), that only changes what the *local name* points to — the caller's variable still points to the original object, unaffected.
- **Immutable** objects (int, str, tuple, frozenset) can never be mutated in place at all — any operation that looks like a modification (`x += 1`, `s = s + "!"`) actually creates a **new object** and rebinds the name to it, so the caller is never affected.

```python
def modify(lst):
    lst.append(4)          # MUTATES the same list object the caller has -> caller sees the change
a = [1, 2, 3]; modify(a); print(a)     # [1, 2, 3, 4]

def reassign(lst):
    lst = [9, 9, 9]          # REBINDS the local name only -> caller's list is untouched
a = [1, 2, 3]; reassign(a); print(a)     # [1, 2, 3]  (unchanged)

def increment(n):
    n += 1                     # int is immutable -> this creates a new int, rebinds local n only
x = 5; increment(x); print(x)     # 5  (unchanged)
```

**Common DSA bug:** forgetting to `.copy()` a list/sub-array before passing it into recursive backtracking calls, causing all branches to share (and corrupt) the same underlying data.

### 10. Time & Space Complexity — quick reference

| Notation | Name | Example operation |
|---|---|---|
| O(1) | Constant | dict/set lookup, array index |
| O(log n) | Logarithmic | binary search |
| O(n) | Linear | single loop, linear search |
| O(n log n) | Linearithmic | efficient sorting (merge/quick/heap sort) |
| O(n²) | Quadratic | nested loops, bubble/selection/insertion sort |
| O(2ⁿ) | Exponential | naive recursive subsets/Fibonacci |
| O(n!) | Factorial | brute-force permutations |

Space complexity follows the same notation, measuring auxiliary memory used (not counting the input itself, unless specified).


---

## Part 17 — DSA Fundamentals (Algorithms & Patterns)

### 1. Complexity Analysis — Big-O
`O(1) < O(log n) < O(n) < O(n log n) < O(n²) < O(2ⁿ) < O(n!)` — see table at the end of Part 16. Space complexity is analyzed the same way.

### 2. Core Data Structures Overview
**Linear:** Array, Linked List, Stack (LIFO), Queue (FIFO), Deque, String.
**Non-linear:** Tree, Binary Tree, BST, Heap (Min/Max), Graph, Hash Table.

### 3. Searching
```python
# Linear search - O(n)
def linear_search(arr, target):
    for i, v in enumerate(arr):
        if v == target: return i
    return -1

# Binary search - O(log n) - REQUIRES sorted input
def binary_search(arr, target):
    lo, hi = 0, len(arr) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if arr[mid] == target: return mid
        elif arr[mid] < target: lo = mid + 1
        else: hi = mid - 1
    return -1
```

### 4. Sorting Algorithms

| Algorithm | Best | Average | Worst | Space | Stable? |
|---|---|---|---|---|---|
| Bubble sort | O(n) | O(n²) | O(n²) | O(1) | Yes |
| Selection sort | O(n²) | O(n²) | O(n²) | O(1) | No |
| Insertion sort | O(n) | O(n²) | O(n²) | O(1) | Yes |
| Merge sort | O(n log n) | O(n log n) | O(n log n) | O(n) | Yes |
| Quick sort | O(n log n) | O(n log n) | O(n²) | O(log n) | No |
| Heap sort | O(n log n) | O(n log n) | O(n log n) | O(1) | No |
| Counting sort | O(n+k) | O(n+k) | O(n+k) | O(k) | Yes |

```python
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n - i - 1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

def merge_sort(arr):
    if len(arr) <= 1: return arr
    mid = len(arr) // 2
    left, right = merge_sort(arr[:mid]), merge_sort(arr[mid:])
    result, i, j = [], 0, 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]: result.append(left[i]); i += 1
        else: result.append(right[j]); j += 1
    return result + left[i:] + right[j:]
```

### 5. Arrays & Strings — key patterns
```python
# Kadane's Algorithm (Maximum Subarray Sum) - O(n)
def max_subarray(arr):
    max_so_far = curr = arr[0]
    for x in arr[1:]:
        curr = max(x, curr + x)
        max_so_far = max(max_so_far, curr)
    return max_so_far
```
Also: two pointers, prefix sums, sliding window (see Patterns below).

### 6. Stack & Queue
```python
stack = []
stack.append(1)          # push - O(1)
stack.pop()                # pop  - O(1) - LIFO: Last In, First Out
stack[-1]                    # peek/top

from collections import deque
queue = deque()
queue.append(1)             # enqueue - O(1)
queue.popleft()                # dequeue - O(1) - FIFO: First In, First Out
```
**Use cases:** stack → undo functionality, expression evaluation, DFS, balanced-parentheses checking. Queue → BFS, task scheduling, rate limiting.

### 7. Linked Lists
```python
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

# Reverse a linked list - O(n) time, O(1) space
def reverse(head):
    prev = None
    while head:
        nxt = head.next
        head.next = prev
        prev = head
        head = nxt
    return prev

# Floyd's Cycle Detection ("tortoise and hare") - O(n) time, O(1) space
def has_cycle(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast: return True
    return False
```

### 8. Trees, BST & Traversals
```python
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = self.right = None

def inorder(root):    # Left, Node, Right - gives SORTED order for a BST
    if root:
        inorder(root.left); print(root.val); inorder(root.right)

def preorder(root):   # Node, Left, Right - used to COPY/serialize a tree
    if root:
        print(root.val); preorder(root.left); preorder(root.right)

def postorder(root):  # Left, Right, Node - used to DELETE a tree safely (children before parent)
    if root:
        postorder(root.left); postorder(root.right); print(root.val)

from collections import deque
def level_order(root):   # BFS traversal, level by level
    if not root: return
    q = deque([root])
    while q:
        node = q.popleft()
        print(node.val)
        if node.left: q.append(node.left)
        if node.right: q.append(node.right)
```
**BST property:** left subtree < node < right subtree (all values). Enables O(log n) search/insert/delete on a **balanced** BST (O(n) worst case if skewed/unbalanced).

### 9. Heaps / Priority Queues
Complete binary tree; **min-heap**: parent ≤ children; **max-heap**: parent ≥ children. Python's `heapq` is min-heap only.

| Operation | Complexity |
|---|---|
| `heappush` | O(log n) |
| `heappop` | O(log n) |
| `heapify` (build from list) | O(n) |
| peek (smallest) | O(1) |
**Use cases:** top-k elements, scheduling, Dijkstra's algorithm, median-finding (two heaps).

### 10. Hashing & Hash Tables
Maps keys → values using a hash function; **average O(1)** for insert/get/delete (worst case O(n) with heavy collisions). Python's `dict`/`set` ARE hash tables.
**Use cases:** counting/frequency (`Counter`), caching, deduplication, the classic "two-sum" pattern:
```python
def two_sum(nums, target):
    seen = {}
    for i, n in enumerate(nums):
        if target - n in seen:
            return [seen[target - n], i]
        seen[n] = i
```

### 11. Graphs — Representations & Traversal
```python
graph = {1: [2, 3], 2: [4], 3: [4], 4: []}       # adjacency list (most common)

def bfs(graph, start):                              # O(V+E) - level-by-level, uses a QUEUE
    visited, q = {start}, deque([start])
    order = []
    while q:
        node = q.popleft()
        order.append(node)
        for nb in graph[node]:
            if nb not in visited:
                visited.add(nb); q.append(nb)
    return order

def dfs(graph, start, visited=None):                 # O(V+E) - goes deep first, uses a STACK/recursion
    if visited is None: visited = set()
    visited.add(start)
    for nb in graph[start]:
        if nb not in visited:
            dfs(graph, nb, visited)
    return visited
```
**Other key algorithms:** Dijkstra (shortest path, weighted, non-negative), Bellman-Ford (handles negative weights), Kruskal/Prim (Minimum Spanning Tree), Topological Sort (DAGs — task scheduling/dependency resolution).

### 12. Recursion & Backtracking
```python
def backtrack(state, choices):
    if is_complete(state):
        record(state); return
    for choice in choices(state):
        apply(choice, state)
        backtrack(state, choices)
        undo(choice, state)              # <- the "undo" step is what makes it backtracking
```
**Classic problems:** permutations, combinations, subsets, N-Queens, maze/path search, Sudoku solving, constraint satisfaction.

### 13. Dynamic Programming
**Core idea:** define a **state**, a **transition/recurrence**, **base cases**, and a **computation order** — useful when subproblems overlap and solutions can be reused.
```python
from functools import lru_cache
@lru_cache(None)                    # memoization - caches results automatically
def fib(n):
    if n <= 1: return n
    return fib(n-1) + fib(n-2)

def fib_tabulation(n):                # bottom-up, builds a table iteratively
    if n <= 1: return n
    dp = [0]*(n+1); dp[1] = 1
    for i in range(2, n+1):
        dp[i] = dp[i-1] + dp[i-2]
    return dp[n]
```
**Classic problems:** Fibonacci, 0/1 Knapsack, Longest Common Subsequence (LCS), Coin Change, Matrix-chain multiplication, grid/path DP.
**Optimization:** once the full DP is correct, check whether only the last 1–2 states are needed — this often reduces O(n) space to O(1).

### 14. Bit Manipulation
```python
x |= (1 << k)          # set bit k
x &= ~(1 << k)           # clear bit k
x ^= (1 << k)              # toggle bit k
is_set = (x & (1 << k)) != 0   # test bit k
x << 1                        # left shift (multiply by 2)
x >> 1                          # right shift (divide by 2)
```

### 15. Useful Formulas
```python
n * (n + 1) // 2              # sum of 1..n
n * (n + 1) * (2*n + 1) // 6    # sum of squares 1..n
```

### 16. Problem-Solving Patterns (Master These — They Solve Most Interview Problems)

| Pattern | When to use |
|---|---|
| **Two pointers** | sorted array/string problems, pair-sum, removing duplicates in place |
| **Sliding window** | contiguous subarray/substring problems (max sum of size k, longest substring without repeats) |
| **Fast & slow pointers** | cycle detection, finding the middle of a linked list |
| **Prefix sums** | range-sum queries, subarray-sum problems |
| **Merge intervals** | overlapping interval problems (meeting rooms, calendar conflicts) |
| **Cyclic sort** | array containing numbers in a known range [1..n] |
| **Top-K elements** | use a heap of size k |
| **Hash-map counting/lookup** | frequency problems, two-sum-style lookups |
| **Binary search (incl. "on the answer")** | sorted data, or search over a monotonic answer space rather than an array |
| **Backtracking** | generate all valid configurations (permutations, subsets, board puzzles) |
| **Divide & conquer** | break into independent subproblems (merge sort, quick sort) |
| **Greedy** | local optimal choice leads to global optimum (activity selection, Huffman coding) |
| **BFS/DFS** | graph/tree traversal, shortest path in unweighted graphs (BFS), connectivity/paths (DFS) |
| **Dynamic Programming** | overlapping subproblems + optimal substructure |

**Golden rules:** Understand → Dry run by hand → Code → Test edge cases → Optimize → Repeat. Patterns are clues, not magic templates — always verify the pattern's assumptions actually hold for the problem in front of you.


---

## Part 18 — Web Development Overview

*A concise orientation to Python web development — not a full framework course. Useful to know how the language you're learning fits into building web applications; revisit in depth once fundamentals/DSA are comfortable.*

### 1. What "Python Web Development" Means
Building applications that run on a server and communicate with a browser (or another program) over HTTP — a web server receives a **request**, runs Python code to decide what to do, and sends back a **response** (HTML, JSON, a file, etc.).

### 2. HTTP Request/Response

- **HTTP** (HyperText Transfer Protocol) is the request/response protocol the web is built on.
- A **request** has a **method** (`GET` read data, `POST` create data, `PUT`/`PATCH` update, `DELETE` remove), a **URL**, headers, and optionally a body (e.g., form/JSON data).
- A **response** has a **status code** (`200` OK, `301` redirect, `404` not found, `500` server error), headers, and a body.
```python
import requests                      # the standard third-party HTTP client library
r = requests.get("https://api.example.com/users")
r.status_code       # 200
r.json()               # parsed JSON body as a Python dict/list
```

### 3. URLs & Routes
A **URL** identifies a resource (`/users/42/profile`). A **route** maps a URL pattern to the Python function that handles it.
```python
# Flask-style routing example (illustrative, not a full tutorial)
@app.route("/users/<int:user_id>")
def get_user(user_id):
    return {"id": user_id, "name": "Alice"}
```

### 4. Forms
HTML forms collect user input (`<input>`, `<select>`, etc.) and submit it to a route, usually via `POST`. The framework parses the submitted field values back into something Python can read (e.g., `request.form['email']`).

### 5. Templates
Templates are HTML files with placeholders that get filled in with Python data at render time (e.g., Flask/Django use **Jinja2**-style templates: `{{ user.name }}`), separating presentation (HTML) from logic (Python).

### 6. Databases
Web apps typically persist data in a database (PostgreSQL, MySQL, SQLite). Python talks to these either with raw SQL (via a driver, or the built-in `sqlite3` module) or through an **ORM** (Object-Relational Mapper) that lets you work with database rows as Python objects instead of writing SQL directly (e.g., Django's built-in ORM, or SQLAlchemy for Flask/FastAPI).

### 7. Authentication
Verifying **who** a user is (login/password, OAuth, tokens) and **what** they're allowed to do (authorization). Common patterns: session-based login (server remembers you via a cookie) or token-based (e.g., JWT — the client sends a signed token with each request).

### 8. APIs & JSON in Web Applications
An **API** (Application Programming Interface) here usually means a set of URL routes that return structured data (typically **JSON**) instead of HTML — built for other programs/frontends to consume, not for a human to read directly in a browser.
```python
import json
return json.dumps({"status": "ok", "data": results})      # a typical API response body
```

### 9. Deployment
Getting the app from your laptop onto a server the public can reach: a **WSGI/ASGI server** (e.g., Gunicorn, Uvicorn) runs your Python app in production (Flask's/Django's built-in dev server is not meant for production traffic); this typically sits behind a reverse proxy (e.g., Nginx); the app is hosted on a cloud platform (AWS, Render, Railway, Heroku-style PaaS, etc.), often packaged in a **Docker** container for consistency between environments.

### 10. Django vs Flask vs FastAPI — Quick Comparison

| Framework | What it is | General purpose | Typical use | Basic characteristics |
|---|---|---|---|---|
| **Django** | A full-featured, "batteries-included" web framework | Complete web applications | Content-heavy sites, admin-backed apps, apps needing a lot of built-in structure fast | Built-in ORM, admin panel, authentication, templating — very structured, opinionated, more to learn upfront |
| **Flask** | A lightweight, minimalist web framework ("microframework") | Small-to-medium apps, APIs, prototypes | Projects where you want to choose your own database/tools rather than accept defaults | Minimal core, highly flexible, extensions added as needed, simple to start with |
| **FastAPI** | A modern, high-performance framework focused on APIs | Building APIs quickly, especially with strong data validation | ML model-serving APIs, microservices, async-heavy backends | Built on Python type hints for automatic request validation, auto-generated interactive API docs, native `async`/`await` support, very fast |

**Takeaway:** all three are Python web frameworks solving the same underlying problem (routes → Python code → response) with different amounts of built-in structure and different sweet spots — Django for "give me everything," Flask for "give me just the core," FastAPI for "give me a fast, type-safe API."

---

## Part 19 — Testing, Debugging & Code Quality

### 1. Reading Errors & Tracebacks
```
Traceback (most recent call last):
  File "app.py", line 12, in <module>
    result = divide(10, 0)
  File "app.py", line 4, in divide
    return a / b
ZeroDivisionError: division by zero
```
**Read tracebacks from the BOTTOM upward** — the last line is the actual error type/message; the lines above show the call chain that led there (most recent call last). Identify the exact line and the types of the variables involved.

### 2. Debugging Workflow

1. Read the traceback fully, bottom to top.
2. Identify the exact failing line and inspect variable types/values there (`print()` or a debugger like `pdb`/`breakpoint()`).
3. **Reduce the failing case** — strip the problem down to the smallest input that still reproduces the bug.
4. Test edge cases explicitly (empty input, zero, negative numbers, None, very large input).
5. Don't hide errors with a broad `except:` — that masks the real cause and makes future debugging harder.

### 3. Assertions & Small Tests
```python
def is_even(n):
    return n % 2 == 0

assert is_even(4)
assert not is_even(5)
assert add(2, 3) == 5, "add() failed on basic case"     # optional custom message
```
Assertions are lightweight sanity checks — good for catching "this should never happen" conditions during development (note: they can be globally disabled with `python -O`, so don't rely on them for production input validation).

### 4. Formal Testing
```python
import unittest
class TestMath(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2, 3), 5)
if __name__ == '__main__':
    unittest.main()

# pytest style (simpler, widely used in industry)
def test_add():
    assert add(2, 3) == 5
```

### 5. Clean Code Principles

- **Descriptive names**: `calculate_total_price()` beats `calc()`.
- **Keep functions focused**: one function, one responsibility.
- **Prefer simple, readable code** over clever one-liners.
- **Modular code**: break large scripts into functions/modules that can be tested independently.
- **Use a virtual environment per project**; keep dependencies explicit (`requirements.txt`).
- Use formatting/linting tools when a project grows (`black`, `flake8`, `pylint`).

### 6. Common Python Mistakes (Recap Across This Document)

- Using a **mutable default argument** (`def f(x, lst=[])`).
- Comparing values with `is` instead of `==` (and vice versa for `None`).
- Modifying a list while iterating over it directly.
- Off-by-one errors in slicing/`range()` (remember: stop is *excluded*).
- Shallow-copying nested structures and expecting full independence.
- Bare `except:` swallowing real bugs.
- Forgetting `self`/`cls` in class methods, or forgetting `super().__init__()`.
- Using a plain `list` as a queue (`pop(0)` is O(n)) instead of `collections.deque`.

**Revision loop:** Learn → close the notes → write the concept from memory → solve a small problem → check mistakes → repeat.

---

## Part 20 — Practice Bank

*Progressive practice problems organized by topic. Work through each group after finishing the matching chapter above — don't just read the notes, run these. Solutions aren't included on purpose: struggling with a problem for a few minutes before checking your work is where the actual learning happens.*

### 1. Basics / Variables / Operators

1. Write a program that stores your name, age, and height, then prints them in a single formatted sentence using an f-string.
2. Write a program to swap the values of two variables **without** using a third variable.
3. Take two numbers as input and print their sum, difference, product, quotient, and remainder.
4. Write a program to calculate the average of two numbers entered by the user.
5. Write a program to calculate the square and cube of a number entered by the user.
6. Check whether a given variable `a` is greater than `b` using a comparison operator (`a = 34`, `b = 80`).

### 2. Strings

1. Write a program that takes a name and prints `"Good Afternoon, <name>!"`.
2. Given `letter = "Dear <|Name|>, You are selected! <|Date|>"`, write a program that fills in the placeholders with real values.
3. Write a program to detect whether a string contains a double space.
4. Replace all double spaces in a string with single spaces.
5. Write a program to check if a string is a palindrome (reads the same forwards and backwards).
6. Write a program to count the number of vowels in a given string.
7. Reverse a string without using slicing (`[::-1]`) — use a loop instead.

### 3. Lists / Tuples

1. Store seven fruits entered by the user in a list and print them sorted alphabetically.
2. Accept marks of 6 students and display them sorted in descending order.
3. Write a program that proves a tuple cannot be modified after creation (try to change an element and observe the error).
4. Write a program to sum all numbers in a list of 4 numbers.
5. Given `a = (7, 0, 8, 0, 0, 9)`, count how many zeros it contains.
6. Write a program to find the second-largest number in a list without using `sorted()`.
7. Merge two lists into one, remove duplicates, and sort the result.

### 4. Dictionaries / Sets

1. Create a dictionary of Hindi words with their English translations; let the user look one up.
2. Take eight numbers as input and print only the unique ones.
3. What happens if you try to store `18` (int) and `'18'` (str) as two different elements of a set? Are they considered different?
4. Given `s = set(); s.add(20); s.add(20.0); s.add('20')`, what is `len(s)` after these operations, and why?
5. Create an empty dictionary and let 4 users enter their name (key) and favorite language (value). What happens if two names are the same?
6. Write a program to merge two dictionaries. If a key exists in both, the second dictionary's value should win.
7. Write a program to invert a dictionary (swap keys and values).

### 5. Conditions

1. Find the greatest of four numbers entered by the user.
2. A student passes if they score at least 40% overall **and** at least 33% in each of 3 subjects — write a program to determine pass/fail given three subject marks.
3. Write a program to calculate a student's grade from marks using: 90-100→Ex, 80-90→A, 70-80→B, 60-70→C, 50-60→D, below 50→F.
4. Write a program to check whether a given username is shorter than 10 characters.
5. Write a program that checks whether a comment contains any of these spam phrases: "buy now", "click this", "subscribe this".

### 6. Loops

1. Print the multiplication table of a number entered by the user, using a `for` loop.
2. Repeat problem 1 using a `while` loop instead.
3. Write a program to check whether a given number is prime.
4. Find the sum of the first `n` natural numbers using a `while` loop.
5. Calculate the factorial of a number using a `for` loop, then again using recursion.
6. Print a right-angled star pattern of height `n` (e.g., for n=3: `*` / `**` / `***`).
7. Print a pyramid star pattern of height `n` (e.g., for n=3: `  *` / ` ***` / `*****`).
8. Use `for...else` to search for a target value in a list and print "not found" only if the loop completes without a `break`.

### 7. Functions / Recursion

1. Write a function that returns the greatest of three numbers.
2. Write a function to convert Celsius to Fahrenheit.
3. Write a recursive function to calculate the sum of the first `n` natural numbers.
4. Write a recursive function to compute the `n`th Fibonacci number.
5. Write a function that converts inches to centimeters.
6. Write a function `remove_and_strip(lst, word)` that removes a given word from a list and strips whitespace from the remaining elements.
7. Write a function using `*args` that returns the sum of any number of arguments.
8. Write a function using `**kwargs` that pretty-prints any number of keyword arguments as `key: value` lines.

### 8. File Handling

1. Read a text file `poem.txt` and check whether it contains the word `"twinkle"`.
2. Write a program that reads a high-score file (which may be empty or contain a previous score) and updates it only if a new score beats the old one.
3. Generate multiplication tables for numbers 2 to 20 and write each to its own file inside a folder.
4. A file contains the word `"secret"` multiple times — write a program that replaces every occurrence with `#######` and saves the result.
5. Write a program that copies the contents of one text file into a new file.
6. Write a program that checks whether two text files have identical content.

### 9. OOP

1. Create a class `Student` that stores name, age, and grade, with a method that prints a summary.
2. Create a class `Calculator` with methods for square, cube, and square root of a number.
3. Create a class with a class-level attribute; create two instances and show that changing the class attribute affects both, while changing an instance attribute affects only one.
4. Create a base class `Animal` and a derived class `Dog` that overrides a `speak()` method — demonstrate polymorphism by looping over a list of mixed `Animal`/`Dog` objects.
5. Write a class `BankAccount` with `deposit()`, `withdraw()`, and a private balance attribute (using name mangling).
6. Write a class `Vector2D` that overloads `+` and `*` (via `__add__`/`__mul__`) to add and scale vectors.

### 10. Exceptions

1. Write a program that divides two numbers and gracefully handles `ZeroDivisionError`.
2. Write a program that opens three files (`1.txt`, `2.txt`, `3.txt`) and prints a message for any that don't exist, without crashing the program.
3. Create a custom exception `NegativeValueError` and raise it when a function receives a negative number where only positive numbers are valid.
4. Write a program with a `try/except/else/finally` block where each branch prints a different message, and verify your understanding by testing with both valid and invalid input.

### 11. Comprehensions

1. Write a list comprehension that generates the multiplication table of a number entered by the user.
2. Write a dict comprehension that maps each word in a sentence to its length.
3. Write a set comprehension that extracts all unique vowels from a string.
4. Write a nested list comprehension to transpose a 2D matrix (swap rows and columns).

### 12. Lambda / map / filter / reduce

1. Use `map()` with a lambda to square every number in a list.
2. Use `filter()` with a lambda to keep only the numbers in a list divisible by 5.
3. Use `reduce()` to find the maximum number in a list (without using `max()`).
4. Sort a list of tuples `(name, score)` by `score` descending using `sorted()` with a lambda key.

### 13. Mixed Python (Combine Multiple Concepts)

1. Write a program that reads a list of student dictionaries (`{"name": ..., "marks": [...]}`), computes each student's average, and writes the results sorted by average to a CSV file.
2. Write a program that reads a text file, counts word frequency using `collections.Counter`, and prints the top 5 most common words.
3. Build a simple command-line contact book: add, search, and delete contacts, persisting them to a JSON file between runs.
4. Write a program that generates 1,000 random numbers with NumPy, then reports the mean, median, standard deviation, and how many fall more than one standard deviation from the mean.

---

## Part 21 — Projects

*Three small, complete projects that combine multiple chapters above into something you actually run. Build them in order — each one leans on slightly more of the language than the last.*

### 1. Snake, Water, Gun
A three-way twist on rock-paper-scissors: **Snake** drinks **Water**, **Water** drowns **Gun**, **Gun** kills **Snake**.

**Objective:** build a playable command-line game against the computer, with a running score across multiple rounds.

**Concepts used:** functions, conditionals, the `random` module, loops, input validation, dictionaries (for the score).

**Requirements:**

- Accept the player's choice from the keyboard and validate it against the three allowed options.
- Randomly generate the computer's choice.
- Correctly decide the winner for all 9 possible combinations (including ties).
- Let the player play multiple rounds and track a running score.

**Suggested implementation approach:**

1. Represent the three choices and encode the win relationships (e.g., a dict mapping each choice to the one it beats).
2. Write a `decide_winner(player, computer)` function that returns `"player"`, `"computer"`, or `"tie"`.
3. Take the player's choice via `input()`, validate it, and re-prompt on invalid input.
4. Randomly pick the computer's choice with `random.choice()`, print both choices and the result.
5. Wrap it all in a loop so the player can keep playing, updating a score dictionary (`{"player": 0, "computer": 0, "ties": 0}`) each round.

**Optional extensions:** best-of-5 match mode; a difficulty setting where the computer's choice is weighted rather than uniform-random; save high scores to a file between sessions.

### 2. The Perfect Guess
The computer picks a random number in a range; the player tries to guess it, receiving "higher"/"lower" hints after each guess.

**Objective:** build a number-guessing game that tells the player how many attempts they needed once they succeed.

**Concepts used:** the `random` module, loops, conditionals, counting/accumulator variables.

**Requirements:**

- Generate a random target number within a fixed, clearly stated range.
- Accept repeated guesses until the player finds the number.
- After each incorrect guess, tell the player whether to guess higher or lower.
- Report the total number of attempts once the player succeeds.

**Suggested implementation approach:**

1. Generate a random target number in a fixed range (e.g., 1–100) with `random.randint()`.
2. Loop: take a guess via `input()`, compare it to the target, and print `"Lower number please"` or `"Higher number please"` as appropriate; count each attempt.
3. When the guess is correct, print how many attempts it took and end the loop.

**Optional extensions:** limit the player to a maximum number of attempts before they lose; track and display a best-score (fewest attempts) across games, persisted to a text file between runs; add a difficulty setting that changes the range.

### 3. Student Library System
A small command-line library manager: add books, let students borrow/return them, and track who has what.

**Objective:** build a menu-driven program that manages a small book collection and persists its state between runs.

**Concepts used:** OOP (a `Book` class and a `Library` class), file/JSON persistence, dictionaries, custom exceptions, CRUD-style logic (Create/Read/Update/Delete).

**Requirements:**

- Represent each book with at least a title, author, ISBN, and borrowed/available status.
- Support adding books, listing available books, borrowing, and returning.
- Prevent borrowing a book that's already checked out (raise a custom exception).
- Persist the library's state so it survives between program runs.

**Suggested implementation approach:**

1. Define a `Book` class with `title`, `author`, `isbn`, and `is_borrowed` attributes.
2. Define a `Library` class holding a collection of `Book` objects (a dict keyed by ISBN works well), with methods: `add_book()`, `remove_book()`, `list_available()`, `borrow_book(isbn, student_name)`, `return_book(isbn)`.
3. Define and raise a custom exception (e.g., `BookNotAvailableError`) when a student tries to borrow a book that's already checked out.
4. Persist the library's state to a JSON file on exit and reload it on startup.
5. Wrap everything in a simple text menu loop (`1. Add book  2. Borrow  3. Return  4. List available  5. Exit`).

**Optional extensions:** due dates using the `datetime`/`timedelta` tools from Part 10; a simple fine calculation for overdue books; search by title/author using string methods or a list comprehension.

---

## Final Python → DSA Checklist

*A comprehensive revision checklist covering everything in this document. Use it to self-test: cover the notes, recall each item from memory, then verify against the relevant Part above.*

### Python Fundamentals

- [ ] Python basics, applications, installation, execution flow (Part 1)
- [ ] Variables, identifiers, keywords (Part 1)
- [ ] Data types, type conversion, type checking (Part 1)
- [ ] Input/output, comments, indentation (Part 1)
- [ ] Operators & precedence (Part 1)
- [ ] Strings — indexing, slicing, methods, immutability, `del`/`None` nuance (Part 1)
- [ ] Lists, Tuples, Sets, Dictionaries (Part 1)
- [ ] if/elif/else, match-case (Part 2)
- [ ] for loops, while loops (Part 2)
- [ ] **for...else, while...else** (Part 2)
- [ ] break, continue, pass (Part 2)
- [ ] Functions, parameters/arguments, default & keyword arguments (Part 3)
- [ ] `*args`, `**kwargs`, argument unpacking (Part 3)
- [ ] Scope / LEGB (Part 3)
- [ ] Comprehensions (list/dict/set), Lambda, map/filter/reduce (Part 3, 4)
- [ ] Modules, packages, pip, venv (Part 5)
- [ ] Exceptions — try/except/else/finally, custom exceptions (Part 6)
- [ ] File handling, JSON, CSV (Part 7)
- [ ] OOP — classes, inheritance, polymorphism, encapsulation, abstraction, dunder methods (Part 8)
- [ ] Iterators, Generators, Decorators, Closures, Context managers (Part 9)
- [ ] Useful built-ins: `enumerate, zip, any, all, sorted, reversed, callable, id, isinstance, hasattr, getattr, setattr` (Part 9)
- [ ] Modern syntax — walrus operator, type hints, dict merge operators (Part 9)
- [ ] **Date/time — `date`, `datetime`, `timedelta`, `strftime`, `strptime`** (Part 10)
- [ ] Regex (Part 11)

### NumPy / Pandas / Data

- [ ] NumPy ndarray, array creation, dtype, shape, ndim, size (Part 12)
- [ ] Indexing, slicing, boolean/fancy indexing (Part 12)
- [ ] Reshaping, vectorization, broadcasting (Part 12)
- [ ] Aggregation, statistics, axis (Part 12)
- [ ] Searching, sorting (Part 12)
- [ ] Missing/invalid values (Part 12)
- [ ] Views/copies, strides, memory model (Part 12)
- [ ] **Structured/record arrays, masked arrays, `numpy.polynomial`, `np.fft`, `np.digitize`, `np.argpartition`, `np.einsum`** (Part 12 §14)
- [ ] Linear algebra — `np.linalg` (Part 12)
- [ ] Pandas Series, DataFrame (Part 13)
- [ ] `loc`/`iloc`, filtering (Part 13)
- [ ] Cleaning — missing data, duplicates (Part 13)
- [ ] Sorting, groupby, aggregation (Part 13)
- [ ] Merge/join, dates/time series (Part 13)
- [ ] Matplotlib, Seaborn (Part 14)

### DSA

- [ ] Big-O, space complexity (Part 16, 17)
- [ ] Arrays, strings, prefix sums, two pointers, sliding window (Part 16, 17)
- [ ] Searching — linear, binary (Part 17)
- [ ] Sorting — bubble, selection, insertion, merge, quick, heap, counting (Part 17)
- [ ] Stack, Queue, Deque (Part 16, 17)
- [ ] Linked lists, cycle detection (Part 17)
- [ ] Trees, BST, traversals (Part 17)
- [ ] Heaps, priority queue (Part 16, 17)
- [ ] Hashing, hash tables (Part 16, 17)
- [ ] Graphs, BFS, DFS, Dijkstra, Bellman-Ford, MST, topological sort (Part 17)
- [ ] Recursion, backtracking (Part 16, 17)
- [ ] Dynamic programming (Part 17)
- [ ] Bit manipulation (Part 17)
- [ ] Common DSA patterns — two pointers, sliding window, prefix sums, merge intervals, cyclic sort, top-K, hash-map, binary search on answer, backtracking, divide & conquer, greedy, BFS/DFS, DP (Part 17 §16)

### Web Development

- [ ] HTTP request/response, URLs, routes (Part 18)
- [ ] Forms, templates (Part 18)
- [ ] Databases, authentication (Part 18)
- [ ] APIs, JSON in web apps (Part 18)
- [ ] Django, Flask, FastAPI — comparison (Part 18)
- [ ] Deployment (Part 18)

---
