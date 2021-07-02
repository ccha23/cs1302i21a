---
jupytext:
  formats: ipynb,md:myst
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.12
    jupytext_version: 1.9.1
kernelspec:
  display_name: Python 3.7 (XPython)
  language: python
  name: xpython
---

+++ {"slideshow": {"slide_type": "slide"}}

# Lists and Tuples

+++ {"slideshow": {"slide_type": "-"}, "tags": ["remove-cell"]}

**CS1302 Introduction to Computer Programming**
___

```{code-cell}
---
slideshow:
  slide_type: fragment
tags: [remove-cell]
---
%reload_ext mytutor
```

+++ {"slideshow": {"slide_type": "slide"}}

## Motivation of composite data type

+++ {"slideshow": {"slide_type": "fragment"}}

The following code calculates the average of five numbers:

```{code-cell}
---
slideshow:
  slide_type: '-'
---
def average_five_numbers(n1, n2, n3, n4, n5):
    return (n1 + n2 + n3 + n4 + n5) / 5


average_five_numbers(1, 2, 3, 4, 5)
```

+++ {"slideshow": {"slide_type": "fragment"}}

What about using the above function to compute the average household income in Hong Kong.  
The labor size in Hong Kong in 2018 is close to 4 million.
- Should we create a variable to store the income of each individual?
- Should we recursively apply the function to groups of five numbers?

+++ {"slideshow": {"slide_type": "fragment"}}

What we need is
- a *composite data type* that can keep a variable numbers of items, so that  
- we can then define a function that takes an object of the *composite data type*,
- and returns the average of all items in the object.

+++ {"slideshow": {"slide_type": "subslide"}}

**How to store a sequence of items in Python?**

+++ {"slideshow": {"slide_type": "fragment"}}

`tuple` and `list` are two built-in classes for ordered collections of objects of possibly different types.

+++ {"slideshow": {"slide_type": "fragment"}}

Indeed, we have already used tuples and lists before.

```{code-cell}
---
slideshow:
  slide_type: '-'
---
%%mytutor -h 300
a_list = '1 2 3'.split()
a_tuple = (lambda *args: args)(1,2,3)
a_list[0] = 0
a_tuple[0] = 0
```

+++ {"slideshow": {"slide_type": "subslide"}}

**What is the difference between tuple and list?**

+++ {"slideshow": {"slide_type": "fragment"}}

- List is [*mutable*](https://docs.python.org/3/library/stdtypes.html#index-21) so programmers can change its items.
- Tuple is [*immutable*](https://docs.python.org/3/glossary.html#term-immutable) like `int`, `float`, and `str`, so
   - programmers can be certain the content stay unchanged, and
   - Python can preallocate a fixed amount of memory to store its content.

+++ {"slideshow": {"slide_type": "slide"}}

## Constructing sequences

+++ {"slideshow": {"slide_type": "subslide"}}

**How to create tuple/list?**

+++ {"slideshow": {"slide_type": "fragment"}}

Mathematicians often represent a set of items in two different ways:
1. [Roster notation](https://en.wikipedia.org/wiki/Set_(mathematics)#Roster_notation), which enumerates the elements in the sequence. E.g.,
$$ \{0, 1, 4, 9, 16, 25, 36, 49, 64, 81\} $$
2. [Set-builder notation](https://en.wikipedia.org/wiki/Set-builder_notation), which describes the content using a rule for constructing the elements.
$$ \{x^2| x\in \mathbb{N}, x< 10 \}, $$
namely the set of perfect squares less than 100.

+++ {"slideshow": {"slide_type": "fragment"}}

Python also provides two corresponding ways to create a tuple/list:  
1. [Enclosure](https://docs.python.org/3/reference/expressions.html?highlight=literals#grammar-token-enclosure)
2. [Comprehension](https://docs.python.org/3/reference/expressions.html#index-12)

+++ {"slideshow": {"slide_type": "subslide"}}

**How to create a tuple/list by enumerating its items?**

+++ {"slideshow": {"slide_type": "fragment"}}

To create a tuple, we enclose a comma separated sequence by parentheses:

```{code-cell}
---
slideshow:
  slide_type: '-'
---
%%mytutor -h 450
empty_tuple = ()
singleton_tuple = (0,)   # why not (0)?
heterogeneous_tuple = (singleton_tuple,
                       (1, 2.0),
                       print)
enclosed_starred_tuple = (*range(2),
                          *'23')
```

+++ {"slideshow": {"slide_type": "fragment"}}

Note that:
- If the enclosed sequence has one term, there must be a comma after the term.
- The elements of a tuple can have different types.
- The unpacking operator `*` can unpack an iterable into a sequence in an enclosure.

+++ {"slideshow": {"slide_type": "subslide"}}

To create a list, we use square brackets to enclose a comma separated sequence of objects.

```{code-cell}
---
slideshow:
  slide_type: '-'
---
%%mytutor -h 450
empty_list = []
singleton_list = [0]  # no need to write [0,]
heterogeneous_list = [singleton_list, 
                      (1, 2.0), 
                      print]
enclosed_starred_list = [*range(2),
                         *'23']
```

+++ {"slideshow": {"slide_type": "subslide"}}

We can also create a tuple/list from other iterables using the constructors `tuple`/`list` as well as addition and multiplication similar to `str`.

```{code-cell}
---
slideshow:
  slide_type: '-'
---
%%mytutor -h 950
str2list = list('Hello')
str2tuple = tuple('Hello')
range2list = list(range(5))
range2tuple = tuple(range(5))
tuple2list = list((1, 2, 3))
list2tuple = tuple([1, 2, 3])
concatenated_tuple = (1,) + (2, 3)
concatenated_list = [1, 2] + [3]
duplicated_tuple = (1,) * 2
duplicated_list = 2 * [1]
```

+++ {"slideshow": {"slide_type": "subslide"}}

**Exercise** Explain the difference between following two expressions. Why a singleton tuple must have a comma after the item.

```{code-cell}
---
slideshow:
  slide_type: '-'
---
print((1+2)*2, 
      (1+2,)*2, sep='\n')
```

+++ {"nbgrader": {"grade": true, "grade_id": "singleton-tuple", "locked": false, "points": 0, "schema_version": 3, "solution": true, "task": false}, "slideshow": {"slide_type": "-"}}

`(1+2)*2` evaluates to `6` but `(1+2,)*2` evaluates to `(3,3)`. 
- The parentheses in `(1+2)` indicate the addition needs to be performed first, but 
- the parentheses in `(1+2,)` creates a tuple.  

Hence, singleton tuple must have a comma after the item to differentiate these two use cases.

+++ {"slideshow": {"slide_type": "subslide"}}

**How to use a rule to construct a tuple/list?**

+++ {"slideshow": {"slide_type": "fragment"}}

We can specify the rule using a [comprehension](https://docs.python.org/3/reference/expressions.html#index-12),  
which we have used in a generator expression.  
E.g., the following is a python one-liner that returns a generator for prime numbers.

```{code-cell}
---
slideshow:
  slide_type: '-'
---
all?
prime_sequence = lambda stop: (x for x in range(2, stop)
                               if all(x % divisor for divisor in range(2, x)))
print(*prime_sequence(100))
```

+++ {"slideshow": {"slide_type": "fragment"}}

There are two comprehensions used:
- In `all(x % divisor for divisor in range(2, x))`, the comprehension creates a generator of remainders to the function `all`, which returns true if all the remainders are `True` in boolean expression.
- In the return value `(x for x in range(2, stop) if ...)` of the anonymous function, the comprehension creates a generator of numbers from 2 to `stop-1` that satisfy the condition of the `if` clause. 

+++ {"slideshow": {"slide_type": "subslide"}}

**Exercise** Use comprehension to define a function `composite_sequence` that takes a non-negative integer `stop` and returns a generator of composite numbers strictly smaller than `stop`. Use `any` instead of `all` to check if a number is composite.

```{code-cell}
---
nbgrader:
  grade: false
  grade_id: composite_sequence
  locked: false
  schema_version: 3
  solution: true
  task: false
slideshow:
  slide_type: '-'
---
any?
### BEGIN SOLUTION
composite_sequence = lambda stop: (x for x in range(2, stop)
                               if any(x % divisor == 0 for divisor in range(2, x)))
### END SOLUTION

print(*composite_sequence(100))
```

+++ {"slideshow": {"slide_type": "subslide"}}

We can construct a list instead of a generator using comprehension:

```{code-cell}
---
slideshow:
  slide_type: '-'
---
print(list(x**2 for x in range(10)))  # Use the list constructor
print([x**2 for x in range(10)])      # Enclose comprehension by brackets
```

+++ {"slideshow": {"slide_type": "subslide"}}

We can also use comprehension to construct a tuple:

```{code-cell}
---
slideshow:
  slide_type: '-'
---
print(tuple(x**2 for x in range(10))) # Use the tuple constructor
```

+++ {"slideshow": {"slide_type": "subslide"}}

**Exercise** Explain the difference between the following expressions.

```{code-cell}
---
slideshow:
  slide_type: '-'
---
print((x**2 for x in range(10)),
      (*(x**2 for x in range(10)),), sep='\n')
```

+++ {"nbgrader": {"grade": true, "grade_id": "generator-vs-tuple", "locked": false, "points": 0, "schema_version": 3, "solution": true, "task": false}, "slideshow": {"slide_type": "-"}}

- The first is a generator expression, not a tuple. 
- The second is a tuple constructed by enclosing the sequence from unpacking the generator.  
  There must be a comma after the generator since there is only one enclosed term, even though that term generates multiple items.

+++ {"slideshow": {"slide_type": "subslide"}}

**Exercise** Explain the difference between the following expressions.

```{code-cell}
---
slideshow:
  slide_type: '-'
---
print([x for x in range(10)],
      [(lambda arg: arg)(x for x in range(10))], sep='\n')
```

+++ {"nbgrader": {"grade": true, "grade_id": "comprehension-as-argument", "locked": false, "points": 0, "schema_version": 3, "solution": true, "task": false}, "slideshow": {"slide_type": "-"}}

- In the second expression, the comprehension provided as an argument to a function becomes a generator object,  
  which is returned by the anonymous function and enclosed to form the singleton list. 
- In the first expression, the comprehension is not converted to a generator.

+++ {"slideshow": {"slide_type": "subslide"}}

With list comprehension, we can simulate a sequence of biased coin flips.

```{code-cell}
---
slideshow:
  slide_type: '-'
---
from random import random as rand
p = rand()  # unknown bias
coin_flips = ['H' if rand() <= p else 'T' for i in range(1000)]
print('Chance of head:', p)
print('Coin flips:',*coin_flips)
```

+++ {"slideshow": {"slide_type": "fragment"}}

We can then estimate the bias by the fraction of heads coming up.

```{code-cell}
---
slideshow:
  slide_type: '-'
---
def average(seq):
    return sum(seq)/len(seq)

head_indicators = [1 if outcome == 'H' else 0 for outcome in coin_flips]
fraction_of_heads = average(head_indicators)
print('Fraction of heads:', fraction_of_heads)
```

+++ {"slideshow": {"slide_type": "fragment"}}

Note that `sum` and `len` returns the sum and length of the sequence.

+++ {"slideshow": {"slide_type": "fragment"}}

**Exercise** Define a function `variance` that takes in a sequence `seq` and returns the [variance](https://en.wikipedia.org/wiki/Variance) of the sequence.

```{code-cell}
---
nbgrader:
  grade: false
  grade_id: variance
  locked: false
  schema_version: 3
  solution: true
  task: false
slideshow:
  slide_type: '-'
---
def variance(seq):
    ### BEGIN SOLUTION
    return sum(i**2 for i in seq)/len(seq) - average(seq)**2
    ### END SOLUTION

delta = (variance(head_indicators)/len(head_indicators))**0.5
print('95% confidence interval: [{:.2f},{:.2f}]'.format(p-2*delta,p+2*delta))
```

+++ {"slideshow": {"slide_type": "slide"}}

## Selecting items in a sequence

+++ {"slideshow": {"slide_type": "subslide"}}

**How to traverse a tuple/list?**

+++ {"slideshow": {"slide_type": "fragment"}}

Instead of calling the dunder method directly, we can use a for loop to iterate over all the items in order.

```{code-cell}
---
slideshow:
  slide_type: '-'
---
a = (*range(5),)
for item in a: print(item, end=' ')
```

+++ {"slideshow": {"slide_type": "fragment"}}

To do it in reverse, we can use the `reversed` function.

```{code-cell}
---
slideshow:
  slide_type: '-'
---
reversed?
a = [*range(5)]
for item in reversed(a): print(item, end=' ')
```

+++ {"slideshow": {"slide_type": "fragment"}}

We can also traverse multiple tuples/lists simultaneously by `zip`ping them.

```{code-cell}
---
slideshow:
  slide_type: '-'
---
zip?
a = (*range(5),)
b = reversed(a)
for item1, item2 in zip(a,b):
    print(item1,item2)
```

+++ {"slideshow": {"slide_type": "subslide"}}

**How to select an item in a sequence?**

+++ {"slideshow": {"slide_type": "fragment"}}

Sequence objects such as `str`/`tuple`/`list` implements the [*getter method* `__getitem__`](https://docs.python.org/3/reference/datamodel.html#object.__getitem__) to return their items.

+++ {"slideshow": {"slide_type": "fragment"}}

We can select an item by [subscription](https://docs.python.org/3/reference/expressions.html#subscriptions) 
```Python
a[i]
``` 
where `a` is a list and `i` is an integer index.

+++ {"slideshow": {"slide_type": "subslide"}}

A non-negative index indicates the distance from the beginning.

+++ {"slideshow": {"slide_type": "-"}}

$$\boldsymbol{a} = (a_0, ... , a_{n-1})$$

```{code-cell}
---
slideshow:
  slide_type: '-'
---
a = (*range(10),)
print(a)
print('Length:', len(a))
print('First element:',a[0])
print('Second element:',a[1])
print('Last element:',a[len(a)-1])
print(a[len(a)]) # IndexError
```

+++ {"slideshow": {"slide_type": "fragment"}}

`a[i]` with `i >= len(a)` results in an `IndexError`. 

+++ {"slideshow": {"slide_type": "subslide"}}

A negative index represents a negative offset from an imaginary element one past the end of the sequence.

+++ {"slideshow": {"slide_type": "-"}}

$$\begin{aligned} \boldsymbol{a} &= (a_0, ... , a_{n-1})\\
& = (a_{-n}, ..., a_{-1})
\end{aligned}$$

```{code-cell}
---
slideshow:
  slide_type: '-'
---
a = [*range(10)]
print(a)
print('Last element:',a[-1])
print('Second last element:',a[-2])
print('First element:',a[-len(a)])
print(a[-len(a)-1]) # IndexError
```

+++ {"slideshow": {"slide_type": "fragment"}}

`a[i]` with `i < -len(a)` results in an `IndexError`. 

+++ {"slideshow": {"slide_type": "subslide"}}

**How to select multiple items?**

+++ {"slideshow": {"slide_type": "fragment"}}

We can use a [slicing](https://docs.python.org/3/reference/expressions.html#slicings) to select a range of items:
```Python
a[start:stop]
a[start:stop:step]
```
where `a` is a list;
- `start` is an integer representing the index of the starting item in the selection;
- `stop` is an integer that is one larger than the index of the last item in the selection; and
- `step` is an integer that specifies the step/stride size through the list.

```{code-cell}
---
slideshow:
  slide_type: '-'
---
a = (*range(10),)
print(a[1:4])
print(a[1:4:2])
```

+++ {"slideshow": {"slide_type": "subslide"}}

The parameters take their default values if missing or equal to None.

```{code-cell}
---
slideshow:
  slide_type: fragment
---
a = [*range(10)]
print(a[:4])   # start defaults to 0
print(a[1:])   # stop defaults to len(a)
print(a[1:4:]) # step defaults to 1
```

+++ {"slideshow": {"slide_type": "fragment"}}

They can take negative values.

```{code-cell}
---
slideshow:
  slide_type: '-'
---
print(a[-1:])
print(a[:-1])
print(a[::-1])  
```

+++ {"slideshow": {"slide_type": "fragment"}}

They can also take a mixture of negative and postive values.

```{code-cell}
---
slideshow:
  slide_type: '-'
---
print(a[-1:1])      # equal [a[-1], a[0]]?
print(a[1:-1])      # equal []?
print(a[1:-1:-1])   # equal [a[1], a[0]]?
print(a[-100:100])  # result in IndexError like subscription?
```

+++ {"slideshow": {"slide_type": "subslide"}}

We can now implement a practical sorting algorithm called [quicksort](https://en.wikipedia.org/wiki/Quicksort) to sort a sequence.

```{code-cell}
---
slideshow:
  slide_type: '-'
---
import random


def quicksort(seq):
    '''Return a sorted list of items from seq.'''
    if len(seq) <= 1:
        return list(seq)
    i = random.randint(0, len(seq) - 1)
    pivot, others = seq[i], [*seq[:i], *seq[i + 1:]]
    left = quicksort([x for x in others if x < pivot])
    right = quicksort([x for x in others if x >= pivot])
    return [*left, pivot, *right]


seq = [random.randint(0, 99) for i in range(10)]
print(seq, quicksort(seq), sep='\n')
```

+++ {"slideshow": {"slide_type": "fragment"}}

The above recursion creates a sorted list as `[*left, pivot, *right]` where
- `pivot` is a randomly picked an item in `seq`,
- `left` is the sorted list of items smaller than `pivot`, and
- `right` is the sorted list of items no smaller than `pivot`.

The base case happens when `seq` contains at most one item, in which case `seq` is already sorted.

+++ {"slideshow": {"slide_type": "fragment"}}

There is a built-in function `sorted` for sorting a sequence. It uses the [Timsort](https://en.wikipedia.org/wiki/Timsort) algorithm.

```{code-cell}
---
slideshow:
  slide_type: '-'
---
sorted?
sorted(sorted(seq))
```

+++ {"slideshow": {"slide_type": "slide"}}

## Mutating a list

+++ {"slideshow": {"slide_type": "fragment"}}

For list (but not tuple), subscription and slicing can also be used as the target of an assignment operation to mutate the list.

```{code-cell}
---
slideshow:
  slide_type: '-'
---
%%mytutor -h 300
b = [*range(10)]  # aliasing
b[::2] = b[:5]
b[0:1] = b[:5]
b[::2] = b[:5]  # fails
```

+++ {"slideshow": {"slide_type": "fragment"}}

Last assignment fails because `[::2]` with step size not equal to `1` is an *extended slice*, which can only be assigned to a list of equal size.

+++ {"slideshow": {"slide_type": "subslide"}}

**What is the difference between mutation and aliasing?**

+++ {"slideshow": {"slide_type": "fragment"}}

In the previous code:
- The first assignment `b = [*range(10)]` is aliasing, which gives the list the target name/identifier `b`.
- Other assignments such as `b[::2] = b[:5]` are mutations that [calls `__setitem__`](https://docs.python.org/3/reference/simple_stmts.html#assignment-statements) because the target `b[::2]` is not an identifier.

+++ {"slideshow": {"slide_type": "subslide"}}

**Exercise** Explain the outcome of the following checks of equivalence?

```{code-cell}
---
slideshow:
  slide_type: '-'
---
%%mytutor -h 400
a = [10, 20, 30, 40]
b = a
print('a is b? {}'.format(a is b))
print('{} == {}? {}'.format(a, b, a == b))
b[1:3] = b[2:0:-1]
print('{} == {}? {}'.format(a, b, a == b))
```

+++ {"nbgrader": {"grade": true, "grade_id": "equivalence", "locked": false, "points": 0, "schema_version": 3, "solution": true, "task": false}, "slideshow": {"slide_type": "-"}}

- `a is b` and `a == b` returns `True` because the assignment `b = a` makes `b` an alias of the same object `a` points to.
- In particular, the operation`b[1:3] = b[2:0:-1]` affects the same list `a` points to.

+++ {"slideshow": {"slide_type": "subslide"}}

**Why mutate a list?**

+++ {"slideshow": {"slide_type": "fragment"}}

The following is another implementation of `composite_sequence` that takes advantage of the mutability of list. 

```{code-cell}
---
slideshow:
  slide_type: '-'
---
def sieve_composite_sequence(stop):
    is_composite = [False] * stop  # initialization
    for factor in range(2,stop):
        if is_composite[factor]: continue
        for multiple in range(factor*2,stop,factor):
            is_composite[multiple] = True
    return (x for x in range(4,stop) if is_composite[x])

for x in sieve_composite_sequence(100): print(x, end=' ')
```

+++ {"slideshow": {"slide_type": "fragment"}}

The algorithm 
1. changes `is_composite[x]` from `False` to `True` if `x` is a multiple of a smaller number `factor`, and
2. returns a generator that generates composite numbers according to `is_composite`.

+++ {"slideshow": {"slide_type": "subslide"}}

**Exercise** Is `sieve_composite_sequence` more efficient than your solution `composite_sequence`? Why?

```{code-cell}
---
slideshow:
  slide_type: '-'
---
for x in composite_sequence(10000): pass
```

```{code-cell}
---
slideshow:
  slide_type: '-'
---
for x in sieve_composite_sequence(1000000): pass
```

+++ {"nbgrader": {"grade": true, "grade_id": "sieve", "locked": false, "points": 0, "schema_version": 3, "solution": true, "task": false}, "slideshow": {"slide_type": "-"}}

The line `if is_composite[factor]: continue` avoids the redundant computations of checking composite factors.

+++ {"slideshow": {"slide_type": "fragment"}}

**Exercise** Note that the multiplication operation `*` is the most efficient way to [initialize a 1D list with a specified size](https://www.geeksforgeeks.org/python-which-is-faster-to-initialize-lists/), but we should not use it to initialize a 2D list. Fix the following code so that `a` becomes `[[1, 0], [0, 1]]`.

```{code-cell}
---
slideshow:
  slide_type: '-'
---
%%mytutor -h 250
a = [[0] * 2] * 2
a[0][0] = a[1][1] = 1
print(a)
```

```{code-cell}
---
code_folding: []
nbgrader:
  grade: false
  grade_id: init-2D
  locked: false
  schema_version: 3
  solution: true
  task: false
slideshow:
  slide_type: '-'
---
### BEGIN SOLUTION
a = [[0] * 2 for i in range(2)]
### END SOLUTION
a[0][0] = a[1][1] = 1
print(a)
```

+++ {"slideshow": {"slide_type": "slide"}}

## Different methods to operate on a sequence

+++ {"slideshow": {"slide_type": "fragment"}}

The following compares the lists of public attributes for `tuple` and `list`. 
- We determine membership using the [operator `in` or `not in`](https://docs.python.org/3/reference/expressions.html#membership-test-operations).
- Different from the [keyword `in` in a for loop](https://docs.python.org/3/reference/compound_stmts.html#the-for-statement), operator `in` calls the method `__contains__`.

```{code-cell}
---
slideshow:
  slide_type: '-'
---
list_attributes = dir(list)
tuple_attributes = dir(tuple)

print(
    'Common attributes:', ', '.join([
        attr for attr in list_attributes
        if attr in tuple_attributes and attr[0] != '_'
    ]))

print(
    'Tuple-specific attributes:', ', '.join([
        attr for attr in tuple_attributes
        if attr not in list_attributes and attr[0] != '_'
    ]))

print(
    'List-specific attributes:', ', '.join([
        attr for attr in list_attributes
        if attr not in tuple_attributes and attr[0] != '_'
    ]))
```

+++ {"slideshow": {"slide_type": "fragment"}}

- There are no public tuple-specific attributes, and
- all the list-specific attributes are methods that mutate the list, except `copy`.

+++ {"slideshow": {"slide_type": "subslide"}}

The common attributes
- `count` method returns the number of occurrences of a value in a tuple/list, and
- `index` method returns the index of the first occurrence of a value in a tuple/list.

```{code-cell}
---
slideshow:
  slide_type: '-'
---
%%mytutor -h 300
a = (1,2,2,4,5)
print(a.index(2))
print(a.count(2))
```

+++ {"slideshow": {"slide_type": "subslide"}}

`reverse` method reverses the list instead of returning a reversed list.

```{code-cell}
---
slideshow:
  slide_type: '-'
---
%%mytutor -h 300
a = [*range(10)]
print(reversed(a))
print(*reversed(a))
print(a.reverse())
```

+++ {"slideshow": {"slide_type": "subslide"}}

- `copy` method returns a copy of a list.  
- `tuple` does not have the `copy` method but it is easy to create a copy by slicing.

```{code-cell}
---
slideshow:
  slide_type: fragment
---
%%mytutor -h 400
a = [*range(10)]
b = tuple(a)
a_reversed = a.copy()
a_reversed.reverse()
b_reversed = b[::-1]
```

+++ {"slideshow": {"slide_type": "subslide"}}

`sort` method sorts the list *in place* instead of returning a sorted list.

```{code-cell}
---
slideshow:
  slide_type: '-'
---
%%mytutor -h 300
import random
a = [random.randint(0,10) for i in range(10)]
print(sorted(a))
print(a.sort())
```

+++ {"slideshow": {"slide_type": "subslide"}}

- `extend` method that extends a list instead of creating a new concatenated list.
- `append` method adds an object to the end of a list.
- `insert` method insert an object to a specified location.

```{code-cell}
---
slideshow:
  slide_type: '-'
---
%%mytutor -h 300
a = b = [*range(5)]
print(a + b)
print(a.extend(b))
print(a.append('stop'))
print(a.insert(0,'start'))
```

+++ {"slideshow": {"slide_type": "subslide"}}

- `pop` method deletes and return the last item of the list.  
- `remove` method removes the first occurrence of a value in the list.  
- `clear` method clears the entire list.

We can also use the function `del` to delete a selection of a list.

```{code-cell}
---
slideshow:
  slide_type: '-'
---
%%mytutor -h 300
a = [*range(10)]
del a[::2]
print(a.pop())
print(a.remove(5))
print(a.clear())
```
