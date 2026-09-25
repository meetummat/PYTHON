# Python Quick Reference

*Fast revision sheet — assumes you already understand the concepts. For full explanations, see [README.md](./README.md).*

---

## 1. Python Basics
```python
# comment
"""docstring / multi-line comment"""
x = 10; name = "Py"; ok = True        # dynamic typing, no declaration needed
```
- **Naming:** start with letter/underscore, letters/digits/underscore only, case-sensitive, no keywords.
- **Types:** `int, float, complex, str, bool, list, tuple, set, dict, NoneType`
- **Conversion:** `int("10")`, `float("3.14")`, `str(100)`, `bool(0)` → False (falsy: `0, "", [], {}, None`)
- **I/O:** `input()` always returns `str`; `print(a, b, sep="-", end="\n")`; f-strings `f"{x:.2f}"` preferred.
- Indentation (4 spaces) defines blocks — not braces.

## 2. Operators
| Category | Operators |
|---|---|
| Arithmetic | `+ - * / // % **` |
| Comparison | `== != > < >= <=` | AKA Relational operator.
| Logical | `and or not` |
| Assignment | `= += -= *= /= //= %= **=` `\| \|=` (dict merge, 3.9+) |
| Membership | `in`, `not in` |
| Identity | `is`, `is not` |
| Bitwise | `& \| ^ ~ << >>` |

**Precedence (high→low):** `()` → `**` → unary → `* / // %` → `+ -` → shifts → `&` → `^` → `\|` → comparisons → `not` → `and` → `or`.
`==` compares value; `is` compares identity (use for `None` checks only).

## 3. Strings
```python
s = "Python"
s[0]; s[-1]; s[1:4]; s[::-1]; s[::2]         # indexing/slicing (immutable!)
s.lower()/.upper()/.title()/.strip()/.replace(a,b)
s.split(","); "-".join(lst); s.find(x); s.count(x)
f"{val:.2f}"                                   # f-strings (preferred)
```
**Rule:** strings are immutable — `s[0]='X'` → `TypeError`. Delete via `del s` (removes name) vs `s=None` (rebinds, name still exists).
Complexity: index O(1); slice/concat O(k); `in` search O(n).

## 4. Lists
```python
lst = [1, 2, 3]
lst.append(x); lst.insert(i,x); lst.remove(x); lst.pop(i=-1); lst.sort(key=,reverse=)
sorted(lst); lst.reverse(); lst.copy()
```
Complexity: index/append/pop-last O(1); insert/delete/`in` O(n); sort O(n log n).

## 5. Tuples
```python
t = (10, 20); t[0]; x, y = t; single = (5,)   # trailing comma required!
t.count(x); t.index(x)
```
Immutable, hashable (usable as dict key/set member), faster than lists.

## 6. Sets
```python
s = {1, 2, 3}; s.add(4); s.remove(x); s.discard(x)
a | b   # union     a & b   # intersection
a - b   # difference   a ^ b  # symmetric diff
```
Unordered, unique only. `in` is O(1) avg. `{}` = empty dict, NOT set — use `set()`.

## 7. Dictionaries
```python
d = {"a": 1}
d["a"]; d.get("a", default); d.pop("a"); d.keys()/.values()/.items()
d1 | d2          # merge (3.9+)     d1 |= d2   # in-place merge
```
Keys must be hashable/unique; insertion order preserved (3.7+). O(1) avg get/set/delete.

## 8. Conditions
```python
if x > 0: ...
elif x == 0: ...
else: ...

match status:              # 3.10+
    case 200: ...
    case 404 | 500: ...
    case _: ...
```

## 9. Loops
```python
for i in range(start, stop, step): ...      # stop excluded
while cond: ...
break     # exit loop entirely
continue  # skip to next iteration
pass      # no-op placeholder

for i in range(5):        # for...else: else runs ONLY if loop completes without break
    if i == target: break
else:
    print("not found")

while cond:                # while...else: same rule
    ...
else:
    print("completed normally")
```

## 10. Functions
```python
def f(a, b=5, *args, **kwargs):    # default must follow non-default
    return a + b

f(*[1,2,3])     # unpack list as positional args
f(**{"a":1})      # unpack dict as keyword args

square = lambda x: x*x
list(map(f, it)); list(filter(f, it))
from functools import reduce; reduce(f, it)
```
**Scope (LEGB):** Local → Enclosing → Global → Built-in. Use `global`/`nonlocal` to modify outer scope.
**Mutable default arg bug:** `def f(x, lst=[])` reuses the same list — use `lst=None` instead.

## 11. Comprehensions
```python
[x**2 for x in range(5)]                # list
{x: x**2 for x in range(5)}               # dict
{x for x in range(5) if x%2==0}             # set
(x**2 for x in range(5))                      # generator expr (lazy)
```

## 12. Modules / pip / venv
```python
import math; from math import sqrt as sq
if __name__ == "__main__": main()      # True only when run directly, not imported
```
```bash
pip install pkg==1.2.3; pip freeze > requirements.txt; pip install -r requirements.txt
python -m venv env; source env/bin/activate; deactivate
```

## 13. Exceptions
```python
try:
    ...
except ZeroDivisionError:
    ...
except (TypeError, ValueError) as e:
    ...
else:      # runs if NO exception
    ...
finally:   # always runs
    ...
raise ValueError("msg")
class MyError(Exception): pass
```
Common: `ZeroDivisionError, ValueError, TypeError, IndexError, KeyError, AttributeError, FileNotFoundError, ImportError, StopIteration`. Catch specific exceptions, never bare `except:`.

## 14. File Handling
```python
with open("f.txt", "r", encoding="utf-8") as f:
    data = f.read()                # or f.readlines() / for line in f
with open("f.txt", "w") as f:
    f.write("text")
```
Modes: `'r' 'w' 'a' 'x' 'b' 't'`. Always use `with` (auto-closes, even on exceptions).
```python
import json
json.load(f); json.dump(obj, f, indent=4); json.loads(s); json.dumps(obj)
import csv
csv.reader(f); csv.writer(f).writerow([...]); csv.DictReader(f)

from pathlib import Path
p = Path("data")/"file.txt"; p.exists(); p.suffix; p.stem
import shutil; shutil.copy(a,b); shutil.rmtree(folder)
```

## 15. OOP
```python
class Animal:
    species = "generic"                 # class variable (shared)
    def __init__(self, name):
        self.name = name                 # instance variable
    def speak(self): return "..."

    @classmethod
    def from_str(cls, s): return cls(s)    # cls = the class
    @staticmethod
    def util(): return True                 # no self/cls

class Dog(Animal):
    def speak(self):                       # method overriding (polymorphism)
        return super().speak() + " Woof"    # super() calls parent

class Employee:
    @property
    def name(self): return self._name       # getter — access like an attribute
    @name.setter
    def name(self, v): self._name = v         # setter — validates on assignment
```
**Encapsulation:** `_x` = convention (protected); `__x` = name-mangled (`_Class__x`).
**Abstraction:** `from abc import ABC, abstractmethod` — abstract classes can't be instantiated directly.
**Dunder methods:** `__init__ __str__ __repr__ __len__ __eq__ __add__/__sub__/__mul__/__truediv__ __getitem__ __iter__/__next__ __enter__/__exit__ __call__`

## 16. Advanced Python
```python
def gen():
    yield 1; yield 2                # generator - lazy, memory-efficient
next(iter([1,2,3]))                    # iterator protocol

@decorator                              # wraps a function to add behavior
def f(): ...

def outer():                              # closure
    x = 1
    def inner(): return x
    return inner

class CM:                                   # context manager
    def __enter__(self): return self
    def __exit__(self, *a): pass
# or: from contextlib import contextmanager
```
**Built-ins:** `enumerate(it, start=) zip(a,b) any(it) all(it) sorted(it,key=,reverse=) reversed(it) callable(x) id(x) isinstance(x,T) hasattr/getattr/setattr(obj,name,default)`
**Modern syntax (3.8+):** walrus `:=` (assign in expression); type hints `x: int`, `def f(x: str) -> str:`; dict merge `|`/`|=`; parenthesized multi-`with`.

## 17. Date & Time
```python
from datetime import date, datetime, timedelta
date.today(); datetime.now()
d = date(2024,1,15); dt = datetime(2024,1,15,10,30)
today + timedelta(days=1)                # date arithmetic
date(2024,12,31) - date(2024,1,1)          # -> timedelta; .days gives count

now.strftime("%Y-%m-%d %H:%M:%S")           # object -> string
datetime.strptime("18/09/2026", "%d/%m/%Y")   # string -> object
```
Codes: `%Y %y %m %B/%b %d %A/%a %H %I %M %S %p`. Mnemonic: **str-F-time** = FROM time (format); **str-P-time** = PARSE into time.
`pd.date_range('2024-01-01', periods=5, freq='D')`

## 18. Regex
```python
import re
re.search(p,s); re.match(p,s); re.fullmatch(p,s)     # search anywhere / start / whole string
re.findall(p,s); re.finditer(p,s)
re.sub(p, repl, s); re.split(p,s); re.escape(s)
```
Patterns: `. \d \D \w \W \s \S [abc] [^abc] [a-z] * + ? {n,m} ^ $ | () (?:...)`

## 19. NumPy Quick Reference
```python
import numpy as np
a = np.array([1,2,3]); a.shape; a.ndim; a.size; a.dtype
np.zeros((2,3)); np.ones((2,3)); np.arange(0,10,2); np.linspace(0,1,5); np.eye(3)
rng = np.random.default_rng(42); rng.random(5); rng.integers(1,10,5)

a[1:3]; a[-1]; a[::2]; a[a>2]; a[[0,2]]        # slice=view; fancy/bool=copy
a.reshape(2,3); a.T; a.ravel(); a.flatten()
np.concatenate([a,b]); np.vstack([a,b]); np.hstack([a,b]); np.split(a,3)

a + b                        # broadcasting: align shapes from the right, dims equal or 1
a.sum(axis=0)                  # axis=0 down rows(→col result); axis=1 across cols(→row result)
a.mean(); a.std(); a.argmax(); a.cumsum()
np.sort(a); np.argsort(a); np.where(cond); np.partition(a,k); np.argpartition(a,k)

np.isnan(a); np.nan_to_num(a); np.nansum(a)      # missing values
a.base; np.shares_memory(a,b); a.strides            # views/copies/memory

dt = np.dtype([('name','U10'),('age','i4')])          # structured/record arrays
arr = np.ma.array([1,2,-999], mask=[0,0,1])              # masked arrays
from numpy.polynomial import Polynomial                     # polynomial: Polynomial([1,2,3])
np.fft.fft(signal); np.fft.ifft(freq)                          # FFT
np.digitize(values, bins)                                        # binning
np.einsum('ij,jk->ik', A, B)                                       # einstein summation

a @ b; np.linalg.inv(A); np.linalg.det(A); np.linalg.solve(A,b); np.linalg.eig(A)
```

## 20. Pandas Quick Reference
```python
import pandas as pd
s = pd.Series([1,2,3]); df = pd.DataFrame({'A':[1,2],'B':[3,4]})
df.head(); df.info(); df.describe(); df.shape; df.dtypes

df['A']; df[['A','B']]
df.loc[1:2, ['A']]      # label-based, end-INCLUSIVE
df.iloc[0:2, 0:1]         # position-based, end-EXCLUSIVE

df[df.A > 1]; df[(df.A>1) & (df.B<5)]; df[df.A.isin([1,2])]; df.query("A > 1")
df['C'] = df['A'] + 1; df.drop('A', axis=1); df.rename(columns={'A':'X'})

df.isnull().sum(); df.dropna(); df.fillna(0); df.drop_duplicates()
df.sort_values('A'); df.groupby('A')['B'].mean(); df.groupby('A').agg({'B':'mean'})
pd.merge(df1, df2, on='id', how='inner'); pd.concat([df1,df2])

pd.to_datetime(df['date']); df['date'].dt.year
pd.read_csv('f.csv'); df.to_csv('out.csv', index=False)
```

## 21. Matplotlib / Seaborn
```python
import matplotlib.pyplot as plt
plt.plot(x,y,marker='o'); plt.bar(x,y); plt.scatter(x,y); plt.hist(data,bins=20); plt.pie(v,labels=l)
plt.title(""); plt.xlabel(""); plt.ylabel(""); plt.legend(); plt.show()
fig, axes = plt.subplots(1,2)

import seaborn as sns
sns.barplot(x='A',y='B',data=df); sns.scatterplot(...); sns.boxplot(...); sns.heatmap(df.corr(),annot=True)
```
Line=trend, bar=compare categories, scatter=relationship, histogram=distribution, heatmap=correlation, box=spread/outliers.

## 22. Python for DSA
```python
from collections import Counter, defaultdict, deque, namedtuple
Counter(lst).most_common(k); dd = defaultdict(list)
dq = deque(); dq.append(x); dq.appendleft(x); dq.pop(); dq.popleft()   # O(1) both ends

import heapq
heapq.heapify(lst); heapq.heappush(lst,x); heapq.heappop(lst)   # min-heap; negate for max-heap
heapq.nlargest(k,lst); heapq.nsmallest(k,lst)

sorted(lst, key=, reverse=)          # Timsort, O(n log n), stable
import bisect
bisect.bisect_left(lst,x); bisect.insort(lst,x)

def f(n):
    if n<=1: return 1                 # recursion needs a base case
    return n*f(n-1)

import sys
data = sys.stdin.read().split()         # fast bulk input

for i,v in enumerate(arr): ...
for a,b in zip(l1,l2): ...
arr[::-1]; first,*rest = arr

def modify(lst): lst.append(4)      # object reference passing: mutating in place is visible to the
                                        # caller; rebinding the name is not. Immutable objects cannot be
                                        # changed in place; operations that appear to modify them produce/use another object.
```

## 23. DSA Complexity Cheat Sheet
| Structure/Algo | Access | Search | Insert | Delete |
|---|---|---|---|---|
| Array/List | O(1) | O(n) | O(n)/O(1)* | O(n)/O(1)* |
| Stack (list) | O(1) top | — | O(1) | O(1) |
| Queue/Deque | O(1) ends | — | O(1) | O(1) |
| Hash Table (dict/set) | — | O(1) avg | O(1) avg | O(1) avg |
| Linked List | O(n) | O(n) | O(1)** | O(1)** |
| BST (balanced) | O(log n) | O(log n) | O(log n) | O(log n) |
| Heap | O(1) min/max | — | O(log n) | O(log n) |
| Graph BFS/DFS | — | O(V+E) | — | — |

*at end. **at known position.
**Sorting:** Bubble/Selection/Insertion O(n²); Merge/Heap O(n log n) guaranteed; Quick O(n log n) avg, O(n²) worst; Counting O(n+k).
**Binary search:** O(log n), requires sorted input.
**Big-O order:** O(1) < O(log n) < O(n) < O(n log n) < O(n²) < O(2ⁿ) < O(n!)

## 24. Common Python Mistakes
- Mutable default argument (`def f(x, lst=[])`)
- `is` vs `==` confusion (use `is` only for `None`)
- Modifying a list while iterating it
- Off-by-one in slicing/`range()` (stop excluded)
- Shallow copy of nested structures (`.copy()` doesn't deep-copy inner lists — use `copy.deepcopy()`)
- Bare `except:` hiding real bugs
- Forgetting `self`/`cls`, or forgetting `super().__init__()`
- Using `list` as a queue instead of `collections.deque` (`pop(0)` is O(n))

## 25. Python → DSA Checklist
- [ ] Fundamentals: variables, types, operators, strings, lists/tuples/sets/dicts
- [ ] Control flow: if/elif/else, match-case, for/while, **for...else/while...else**, break/continue/pass
- [ ] Functions: args, `*args`/`**kwargs`, scope/LEGB, lambda, map/filter/reduce
- [ ] Modules/pip/venv, Exceptions, File handling (JSON/CSV/pathlib)
- [ ] OOP: classes, inheritance, polymorphism, encapsulation, `@property`, dunder methods
- [ ] Advanced: iterators, generators, decorators, closures, context managers, walrus/type hints
- [ ] Date & Time, Regex
- [ ] NumPy: arrays, indexing, broadcasting, aggregation, advanced ops (structured/masked/FFT/einsum)
- [ ] Pandas: Series/DataFrame, loc/iloc, groupby, merge, dates
- [ ] Matplotlib/Seaborn basics
- [ ] Python-for-DSA toolkit: deque, heapq, Counter, defaultdict, bisect
- [ ] DSA: complexity, sorting, searching, stacks/queues, linked lists, trees, heaps, hashing, graphs, recursion/backtracking, DP, bit manipulation, patterns
- [ ] Web dev overview: HTTP, routes, ORM, APIs, Django/Flask/FastAPI
- [ ] Testing/debugging fundamentals

