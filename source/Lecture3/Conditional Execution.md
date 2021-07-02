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

# Conditional Execution

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

+++ {"slideshow": {"slide_type": "subslide"}}

## Motivation

+++ {"slideshow": {"slide_type": "fragment"}}

Conditional execution means running different pieces of code based on different conditions. Why?

+++ {"slideshow": {"slide_type": "fragment"}}

For instance, when trying to compute `a/b`, `b` may be `0` and division by `0` is invalid.

```{code-cell}
---
slideshow:
  slide_type: '-'
---
def multiply_or_divide(a, b):
    print('a:{}, b:{}, a*b:{}, a/b:{}'.format(a, b, a * b, a / b))


multiply_or_divide(1, 2)
multiply_or_divide(1, 0)  # multiplication is valid but not shown
```

+++ {"slideshow": {"slide_type": "subslide"}}

Can we skip only the division but not multiplication when `b` is `0`? 

```{code-cell}
---
slideshow:
  slide_type: fragment
---
def multiply_or_divide(a, b):
    fix = a / b if b else 'undefined'
    print('a:{}, b:{}, a*b:{}, a/b:{}'.format(a, b, a * b, fix))


multiply_or_divide(1, 2)
multiply_or_divide(1, 0)  # multiplication is valid but not shown
```

+++ {"slideshow": {"slide_type": "fragment"}}

The above solution involve:
- a *boolean expression* `fix` that checks whether a condition holds, and
- a *conditional construct* `... if ... else ...` that specify which code block should be executed under what condition. 

+++ {"slideshow": {"slide_type": "subslide"}}

## Boolean expressions

+++ {"slideshow": {"slide_type": "subslide"}}

### Comparison Operators

+++ {"slideshow": {"slide_type": "fragment"}}

**How to compare different values?**

+++ {"slideshow": {"slide_type": "fragment"}}

Like the equality and inequality relationships in mathematics,  
Python also have binary [*comparison/relational operators*](https://docs.python.org/3/reference/expressions.html#comparisons):

+++ {"slideshow": {"slide_type": "-"}}

| Expression |  True iff  |
| ---------: | :--------- |
|   `x == y` | $x=y$.     |
|    `x < y` | $x<y$.     |
|   `x <= y` | $x\leq y$. |
|    `x > y` | $x>y$.     |
|   `x >= y` | $x\geq y$. |
|   `x != y` | $x\neq y$. |

+++ {"slideshow": {"slide_type": "fragment"}}

Explore these operators using the widgets below:

```{code-cell}
---
code_folding: []
slideshow:
  slide_type: '-'
---
# Comparisons
from ipywidgets import interact
comparison_operators = ['==','<','<=','>','>=','!=']
@interact(operand1='10',
          operator=comparison_operators,
          operand2='3')
def comparison(operand1,operator,operand2):
    expression = f"{operand1} {operator} {operand2}"
    value = eval(expression)
    print(f"""{'Expression:':>11} {expression}\n{'Value:':>11} {value}\n{'Type:':>11} {type(value)}""")
```

+++ {"slideshow": {"slide_type": "fragment"}}

- These operators return either `True` or `False`, which are `keywords` of type *boolean*.
- The expressions are called *boolean expressions* or *predicates*, named after [George Boole](https://en.wikipedia.org/wiki/George_Boole).
- N.b., the equality operator `==` consists of *two equal signs*, different from the assignment operator `=`.

+++ {"slideshow": {"slide_type": "subslide"}}

**What is the precedence of comparison operators?**

+++ {"slideshow": {"slide_type": "fragment"}}

 All the comparison operators have the [same precedence](https://docs.python.org/3/reference/expressions.html?highlight=precedence#operator-precedence) lower than that of `+` and `-`.

```{code-cell}
---
slideshow:
  slide_type: fragment
---
1 + 2 >= 3  # (1 + 2) >= 3
```

+++ {"slideshow": {"slide_type": "fragment"}}

Python allows multiple comparison operations to be chained together:

```{code-cell}
---
slideshow:
  slide_type: '-'
---
2.0 == 2>1 #equivalent to (2.0 ==2) and (2>1)
```

+++ {"slideshow": {"slide_type": "subslide"}}

**What is the associativity?**

+++ {"slideshow": {"slide_type": "fragment"}}

Comparison operations are [*non-associative*](https://en.wikipedia.org/wiki/Operator_associativity#Non-associative_operators):

```{code-cell}
---
slideshow:
  slide_type: '-'
---
(2.0 == 2) > 1, 2.0 == (2 > 1)  # not the same as 2.0 == 2 > 1
```

+++ {"slideshow": {"slide_type": "fragment"}}

**Errorata** in [Halterman17] due to a misunderstanding of non-associativity vs left-to-right evaluation order:

- [Halterman17, p.69](https://archive.org/stream/2018Fundamentals.ofPython?ref=ol#page/n79/mode/1up):
    > The relational operators are binary operators and are all ~left associative~ **non-associative**.
- [Halterman17, p.50, Table 3.2](https://archive.org/stream/2018Fundamentals.ofPython?ref=ol#page/n60/mode/1up):
    - `=` should be non-associative instead of right-associative.
    - The corresponding table in `Lecture2/Expressions and Arithmetic.ipynb` should also be corrected accordingly.

+++ {"slideshow": {"slide_type": "subslide"}}

**Exercise** Explain why the following boolean expressions have different values.

```{code-cell}
---
slideshow:
  slide_type: '-'
---
1 <= 2 < 3 != 4, (1 <= 2) < (3 != 4)
```

+++ {"nbgrader": {"grade": true, "grade_id": "chained_relational_operator", "locked": false, "points": 0, "schema_version": 3, "solution": true, "task": false}, "slideshow": {"slide_type": "-"}}

The second expression is not a chained comparison: 
- The expressions in the parentheses are evaluated to boolean values first to `True`, and so
- the overall expression `True < True` is evaluated to `False`.

+++ {"slideshow": {"slide_type": "subslide"}}

**Exercise** The comparison operators can be applied to different data types, as illustrated below.  
Explain the meaning of the operators in each of the following expressions.

```{code-cell}
---
code_folding: []
slideshow:
  slide_type: '-'
---
# Comparisons beyond numbers
@interact(expression=[
    '10 == 10.', '"A" == "A"', '"A" == "A "', '"A" != "a"', 
    '"A" > "a"', '"aBcd" < "abd"', '"A" != 64', '"A" < 64'
])
def relational_expression(expression):
    print(eval(expression))
```

+++ {"nbgrader": {"grade": true, "grade_id": "relational_expression", "locked": false, "points": 0, "schema_version": 3, "solution": true, "task": false}, "slideshow": {"slide_type": "-"}}

1. Checks whether an integer is equal to a floating point number.
1. Checks whether two characters are the same.
1. Checks whether two strings are the same. Note the space character.
1. Checks whether a character is larger than the order character according to their unicodes.
1. Checks whether a string is lexicographically smaller than the other string.
1. Checks whether a character is not equal to an integer.
1. TypeError because there is no implementation that evaluates whether a string is smaller than an integer.

+++ {"slideshow": {"slide_type": "subslide"}}

**Is `!` the same as the `not` operator?**

+++ {"slideshow": {"slide_type": "fragment"}}

**Errata** There is an error in [Halterman17, p.69](https://archive.org/stream/2018Fundamentals.ofPython?ref=ol#page/n79/mode/1up) due to confusion with C language:  
> ... `!(x >= 10)` and `!(10 <= x)` are ~equivalent~ **invalid**.
- We can write `1 != 2` as `not 1 == 2` but not `!(1 == 2)` because
- `!` is not a logical operator. It is used to call a [system shell command](https://ipython.readthedocs.io/en/stable/interactive/tutorial.html?highlight=system%20call#system-shell-commands) in IPython.

```{code-cell}
---
slideshow:
  slide_type: fragment
---
!(1 == 2)
```

```{code-cell}
---
slideshow:
  slide_type: '-'
---
!ls  # a bash command that lists files in the current directory
```

+++ {"slideshow": {"slide_type": "subslide"}}

**How to compare floating point numbers?**

```{code-cell}
---
slideshow:
  slide_type: fragment
---
x = 10
y = (x**(1/3))**3
x == y
```

+++ {"slideshow": {"slide_type": "fragment"}}

Why False? Shouldn't $(x^{\frac13})^3=x$?

+++ {"slideshow": {"slide_type": "fragment"}}

- Floating point numbers have finite precisions and so  
- we should instead check whether the numbers are close enough.

+++ {"slideshow": {"slide_type": "subslide"}}

One method of comparing floating point numbers:

```{code-cell}
---
slideshow:
  slide_type: fragment
---
abs(x - y) <= 1e-9
```

+++ {"slideshow": {"slide_type": "fragment"}}

`abs` is a function that returns the absolute value of its argument. Hence, the above translates to

$$|x - y| \leq \delta_{\text{abs}}$$ 
or equivalently 

$$y-\delta_{\text{abs}} \leq x \leq y+\delta_{\text{abs}} $$
where $\delta_{\text{abs}}$ is called the *absolute tolerance*. 

+++ {"slideshow": {"slide_type": "subslide"}}

**Is an absolute tolerance of `1e-9` good enough?**

+++ {"slideshow": {"slide_type": "fragment"}}

What if we want to compare `x = 1e10` instead of `10`?

```{code-cell}
---
slideshow:
  slide_type: fragment
---
x = 1e10
y = (x**(1/3))**3
abs(x - y) <= 1e-9
```

+++ {"slideshow": {"slide_type": "fragment"}}

Floating point numbers "float" at different scales.  
A better way to use the [`isclose`](https://docs.python.org/3/library/math.html#math.isclose) function from `math` module. 

```{code-cell}
---
slideshow:
  slide_type: fragment
---
import math
math.isclose(x, y)
```

+++ {"slideshow": {"slide_type": "subslide"}}

**How does it work?**

+++ {"slideshow": {"slide_type": "fragment"}}

`math.isclose(x,y)` implements

$$ |x - y| \leq \max\{\delta_{\text{rel}} \max\{|x|,|y|\},\delta_{\text{abs}}\}$$
with the default
- *relative tolerance* $\delta_{\text{rel}}$ equal to `1e-9`, and
- absolute tolerance $\delta_{\text{abs}}$ equal to `0.0`.

+++ {"slideshow": {"slide_type": "fragment"}}

**Exercise** Write the boolean expression implemented by `isclose`. You can use the function `max(a,b)` to find the maximum of `a` and `b`. 

```{code-cell}
---
nbgrader:
  grade: false
  grade_id: isclose
  locked: false
  schema_version: 3
  solution: true
  task: false
slideshow:
  slide_type: '-'
---
rel_tol, abs_tol = 1e-9, 0.0
x, y = 1e-100, 2e-100
### BEGIN SOLUTION
abs(x-y) <= max(rel_tol * max(abs(x), abs(y)), abs_tol)
### END SOLUTION
```

+++ {"slideshow": {"slide_type": "slide"}}

### Boolean Operations

+++ {"slideshow": {"slide_type": "fragment"}}

Since chained comparisons are non-associative. It follows a different evaluation rule than arithmetical operators.

+++ {"slideshow": {"slide_type": "fragment"}}

E.g., `1 <= 2 < 3 != 4` is evaluated as follows:

```{code-cell}
---
slideshow:
  slide_type: '-'
---
1 <= 2 and 2 < 3 and 3 != 4
```

+++ {"slideshow": {"slide_type": "fragment"}}

The above is called a *compound boolean expression*, which is formed using the *boolean/logical operator* `and`.

+++ {"slideshow": {"slide_type": "subslide"}}

**Why use boolean operators?**

+++ {"slideshow": {"slide_type": "fragment"}}

What if we want to check whether a number is either $< 0$ or $\geq 100$?  
Can we achieve this only by chaining the comparison operators or applying the logical `and`?

```{code-cell}
---
code_folding: []
slideshow:
  slide_type: '-'
---
# Check if a number is outside a range.
@interact(x='15')
def check_out_of_range(x):
    x_ = float(x)
    is_out_of_range = x_<0 or x_>=100
    print('Out of range [0,100):', is_out_of_range)
```

+++ {"slideshow": {"slide_type": "fragment"}}

- `and` alone is not [functionally complete](https://en.wikipedia.org/wiki/Functional_completeness),  i.e., not enough to give all possible boolean functions. 
- In addition to `and`, we can also use `or` and `not`. 

+++ {"slideshow": {"slide_type": "fragment"}}

|   `x`   |   `y`   | `x and y` | `x or y` | `not x` |
| :-----: | :-----: | :-------: | :------: | :-----: |
| `True`  | `True`  |  `True`   |  `True`  | `False` |
| `True`  | `False` |  `False`  |  `True`  | `False` |
| `False` | `True`  |  `False`  |  `True`  | `True`  |
| `False` | `False` |  `False`  | `False`  | `True`  |

+++ {"slideshow": {"slide_type": "fragment"}}

The above table is called a *truth table*. It enumerates all possible input and output combinations for each boolean operator. 

+++ {"slideshow": {"slide_type": "subslide"}}

**How are chained logical operators evaluated?  
What are the precedence and associativity for the logical operators?**

+++ {"slideshow": {"slide_type": "fragment"}}

- All binary boolean operators are left associative.  
- [Precedence](https://docs.python.org/3/reference/expressions.html?highlight=precedence#operator-precedence): `comparison operators` > `not` > `and` > `or` 




+++ {"slideshow": {"slide_type": "subslide"}}

**Exercise** Explain what the values of the following two compound boolean expressions are:
- Expression A: `True or False and True`
- Expression B: `True and False and True`
- Expression C: `True or True and False`

+++ {"nbgrader": {"grade": true, "grade_id": "compound-boolean", "locked": false, "points": 0, "schema_version": 3, "solution": true, "task": false}, "slideshow": {"slide_type": "-"}}

- Expression A evaluates to `True` because `and` has higher precedence and so the expression has the same value as `True or (False and True)`.
- Expression B evaluates to `False` because `and` is left associative and so the expression has the same value as `(True and False) and True`.
- Expression C evaluates to `True` because `and` has a higher precedence and so the expression has the same value as `True or (True and False)`. Note that `(True or True) and False` evaluates to something `False` instead, so precedence matters.

+++ {"slideshow": {"slide_type": "subslide"}}

Instead of following the precedence and associativity, however, a compound boolean expression uses a [short-circuit evaluation](https://docs.python.org/3/reference/expressions.html?highlight=precedence#boolean-operations).  

+++ {"slideshow": {"slide_type": "fragment"}}

To understand this, we will use the following function to evaluate a boolean expression verbosely.

```{code-cell}
---
slideshow:
  slide_type: '-'
---
def verbose(id,boolean):
    '''Identify evaluated boolean expressions.'''
    print(id,'evaluated:',boolean)
    return boolean
```

```{code-cell}
---
slideshow:
  slide_type: '-'
---
verbose('A',verbose(1,True) or verbose(2,False) and verbose(3,True))  # True or (False and True)
```

+++ {"slideshow": {"slide_type": "fragment"}}

**Why expression 2 and 3 are not evaluated?**

+++ {"slideshow": {"slide_type": "fragment"}}

Because True or ... must be True (Why?) so Python does not look further. From the [documentation](https://docs.python.org/3/reference/expressions.html?highlight=precedence#boolean-operations):

+++ {"slideshow": {"slide_type": "fragment"}}

> The expression `x or y` first evaluates `x`; if `x` is true, its value is returned; otherwise, `y` is evaluated and the resulting value is returned.

+++ {"slideshow": {"slide_type": "fragment"}}

Note that:
- Even though `or` has lower precedence than `and`, it is still evaluated first. 
- The evaluation order for logical operators is left-to-right.

```{code-cell}
---
slideshow:
  slide_type: subslide
---
verbose('B',verbose(4,True) and verbose(5,False) and verbose(6,True))  # (True and False) and True
```

+++ {"slideshow": {"slide_type": "subslide"}}

**Why expression 6 is not evaluated?**

+++ {"slideshow": {"slide_type": "fragment"}}

`True and False and ...` must be `False` so Python does not look further.

+++ {"slideshow": {"slide_type": "fragment"}}

> The expression `x and y` first evaluates `x`; if `x` is false, its value is returned; otherwise, `y` is evaluated and the resulting value is returned.

+++ {"slideshow": {"slide_type": "subslide"}}

Indeed, logical operators can even be applied to non-boolean operands. From the [documentation](https://docs.python.org/3/reference/expressions.html?highlight=precedence#boolean-operations):

+++ {"slideshow": {"slide_type": "fragment"}}

> In the context of Boolean operations, and also when expressions are used by control flow statements, the following values are interpreted as false: `False`, None, numeric zero of all types, and empty strings and containers (including strings, tuples, lists, dictionaries, sets and frozensets). All other values are interpreted as true.

+++ {"slideshow": {"slide_type": "subslide"}}

**Exercise** How does the following code work?

```{code-cell}
---
slideshow:
  slide_type: '-'
tags: [remove-output]
---
print('You have entered', input() or 'nothing')
```

+++ {"nbgrader": {"grade": true, "grade_id": "or", "locked": false, "points": 0, "schema_version": 3, "solution": true, "task": false}, "slideshow": {"slide_type": "-"}}

- The code replaces empty user input by the default string `nothing` because empty string is regarded as False in a boolean operation.
- If user input is non-empty, it is regarded as True in the boolean expression and returned immediately as the value of the boolean operation.

+++ {"slideshow": {"slide_type": "fragment"}}

**Is empty string equal to False?**

```{code-cell}
---
slideshow:
  slide_type: '-'
---
print('Is empty string equal False?',''==False)
```

+++ {"slideshow": {"slide_type": "fragment"}}

- An empty string is regarded as False in a boolean operation but
- a *comparison operation is not a boolean operation*, even though it forms a boolean expression.

+++ {"slideshow": {"slide_type": "slide"}}

## Conditional Constructs

+++ {"slideshow": {"slide_type": "fragment"}}

Consider writing a program that sorts values in *ascending* order.  
A *sorting algorithm* refers to the procedure of sorting values in order.  

+++ {"slideshow": {"slide_type": "subslide"}}

### If-Then Construct

+++ {"slideshow": {"slide_type": "subslide"}}

**How to sort two values?**

+++ {"slideshow": {"slide_type": "fragment"}}

Given two values are stored as `x` and `y`, we want to 
- `print(x,y)` if `x <= y`, and
- `print(y,x)` if `y < x`.

+++ {"slideshow": {"slide_type": "subslide"}}

Such a program flow is often represented by a flowchart like the following:

+++ {"slideshow": {"slide_type": "fragment"}}

<img src="https://www.cs.cityu.edu.hk/~ccha23/cs1302/Lecture3/sort_two_values1.svg" style="max-width:300px;" alt="sort_two_values(x,y);
if(x<=y) {
  print(x, y)
}
if (y<x) {
  print(y, x)
}">

+++ {"slideshow": {"slide_type": "fragment"}}

Python provides the [`if` statement](https://docs.python.org/3/reference/compound_stmts.html#the-if-statement) to implement the above [*control flow*](https://en.wikipedia.org/wiki/Control_flow) specified by the diamonds.

```{code-cell}
---
code_folding: [8]
slideshow:
  slide_type: '-'
---
# Sort two values using if statement
def sort_two_values(x, y):
    if x <= y:
        print(x, y)
    if y < x: print(y, x)


@interact(x='1', y='0')
def sort_two_values_app(x, y):
    sort_two_values(eval(x), eval(y))
```

+++ {"slideshow": {"slide_type": "subslide"}}

We can visualize the execution as follows:

```{code-cell}
---
slideshow:
  slide_type: '-'
---
%%mytutor -h 350
def sort_two_values(x, y):
    if x <= y:
        print(x, y)
    if y < x: print(y, x)
        
sort_two_values(1,0)
sort_two_values(1,2)
```

+++ {"slideshow": {"slide_type": "fragment"}}

Python use indentation to indicate code blocks or *suite*: 
- `print(x, y)` (Line 5) is indented to the right of `if x <= y:` (Line 4) to indicate it is the body of the if statement.
- For convenience, `if y < x: print(y, x)` (Line 6) is a one-liner for an `if` statement that only has one line in its block.
- Both `if` statements (Line 4-6) are indented to the right of `def sort_two_values(x,y):` (Line 3) to indicate that they are part of the body of the function `sort_two_values`.

+++ {"slideshow": {"slide_type": "subslide"}}

**How to indent?**

+++ {"slideshow": {"slide_type": "fragment"}}

- The [style guide](https://www.python.org/dev/peps/pep-0008/#indentation) recommends using 4 spaces for each indentation.  
- In IPython, you can simply type the `tab` key and IPython will likely enter the correct number of spaces for you.

+++ {"slideshow": {"slide_type": "subslide"}}

**What if you want to leave a block empty?**

+++ {"slideshow": {"slide_type": "fragment"}}

In programming, it is often useful to delay detailed implementations until we have written an overall skeleton.  
To leave a block empty, Python uses the keyword [`pass`](https://docs.python.org/3/tutorial/controlflow.html#pass-statements).

```{code-cell}
---
slideshow:
  slide_type: '-'
---
# write a code skeleton
def sort_two_values(x, y):
    pass
    # print the smaller value first followed by the larger one
    
sort_two_values(1,0)
sort_two_values(1,2)
```

+++ {"slideshow": {"slide_type": "fragment"}}

Without `pass`, the code will fail to run, preventing you from checking other parts of the code.

```{code-cell}
---
code_folding: []
slideshow:
  slide_type: fragment
---
# You can add more details to the skeleton step-by-step
def sort_two_values(x, y):
    if x <= y:
        pass  
        # print x before y
    if y < x: pass  # print y before x

sort_two_values(1,0)
sort_two_values(1,2)
```

+++ {"slideshow": {"slide_type": "slide"}}

### If-Then-Else Construct

+++ {"slideshow": {"slide_type": "fragment"}}

The sorting algorithm is not efficient enough. Why not?  
Hint: `(x <= y) and not (y < x)` is a *tautology*, i.e., always true.

+++ {"slideshow": {"slide_type": "fragment"}}

To improve the efficient, we should implement the following program flow.

+++ {"slideshow": {"slide_type": "-"}}

<img src="https://www.cs.cityu.edu.hk/~ccha23/cs1302/Lecture3/sort_two_values2.svg" style="max-width:300px;" alt="sort_two_values(x,y);
if(x<=y) {
  print(x, y)
}
else {
  print(y, x)
}">

+++ {"slideshow": {"slide_type": "fragment"}}

This can be down by the `else` clause of the [`if` statement](https://docs.python.org/3/tutorial/controlflow.html#if-statements).

```{code-cell}
---
slideshow:
  slide_type: fragment
---
%%mytutor -h 350
def sort_two_values(x, y):
    if x <= y:
        print(x, y)
    else:
        print(y,x)
        
sort_two_values(1,0)
sort_two_values(1,2)
```

+++ {"slideshow": {"slide_type": "subslide"}}

We can also use a [*conditional expression*](https://docs.python.org/3/reference/expressions.html#conditional-expressions) to shorten the code.

```{code-cell}
---
code_folding: [5]
slideshow:
  slide_type: '-'
---
def sort_two_values(x, y):
    print(('{0} {1}' if x <= y else '{1} {0}').format(x, y))


@interact(x='1', y='0')
def sort_two_values_app(x, y):
    sort_two_values(eval(x), eval(y))
```

+++ {"slideshow": {"slide_type": "subslide"}}

**Exercise** Explain why the followings have syntax errors.

```{code-cell}
---
slideshow:
  slide_type: '-'
---
1 if True
```

```{code-cell}
---
slideshow:
  slide_type: '-'
---
x = 1 if True else x = 0 
```

+++ {"nbgrader": {"grade": true, "grade_id": "conditional-expression", "locked": false, "points": 0, "schema_version": 3, "solution": true, "task": false}, "slideshow": {"slide_type": "-"}}

A conditional expression must be an expression:
1. It must give a value under all cases. To enforce that, `else` keyword must be provided.
1. An assignment statement does not return any value and therefore cannot be used for the conditional expression.  
    `x = 1 if True else 0` is valid because `x =` is not part of the conditional expression.

+++ {"slideshow": {"slide_type": "slide"}}

### Nested Conditionals

+++ {"slideshow": {"slide_type": "subslide"}}

Consider sorting three values instead of two. A feasible algorithm is as follows:

+++ {"slideshow": {"slide_type": "fragment"}}

<img src="https://www.cs.cityu.edu.hk/~ccha23/cs1302/Lecture3/sort_three_values1.svg" style="max-width:800px;" alt="sort_three_values(x,y,z);
if(x<=y<=z) {
  print(x, y, z)
} else
if (x<=z<=y) {
  print(x, z, y)
} else
if (y<=x<=z) {
  print(y, x, z)
} else
if (y<=z<=x) {
  print(y, z, x)
} else
if (z<=x<=y) {
  print(z, x, y)
} else {
  print(z, y, x)
}">

+++ {"slideshow": {"slide_type": "fragment"}}

We can implement the flow using *nested conditional constructs*:

```{code-cell}
---
code_folding: []
slideshow:
  slide_type: '-'
---
def sort_three_values(x, y, z):
    if x <= y <= z:
        print(x, y, z)
    else:
        if x <= z <= y:
            print(x, z, y)
        else:
            if y <= x <= z:
                print(y, x, z)
            else:
                if y <= z <= x:
                    print(y, z, x)
                else:
                    if z <= x <= y:
                        print(z, x, y)
                    else:
                        print(z, y, x)

def test_sort_three_values():
    sort_three_values(0,1,2)
    sort_three_values(0,2,1)
    sort_three_values(1,0,2)
    sort_three_values(1,2,0)
    sort_three_values(2,0,1)
    sort_three_values(2,1,0)

test_sort_three_values()
```

+++ {"slideshow": {"slide_type": "slide"}}

Imagine what would happen if we have to sort many values.  
To avoid an excessively long line due to the indentation, Python provides the `elif` keyword that combines `else` and `if`.

```{code-cell}
---
slideshow:
  slide_type: fragment
---
def sort_three_values(x, y, z):
    if x <= y <= z:
        print(x, y, z)
    elif x <= z <= y:
        print(x, z, y)
    elif y <= x <= z:
        print(y, x, z)
    elif y <= z <= x:
        print(y, z, x)
    elif z <= x <= y:
        print(z, x, y)
    else:
        print(z, y, x)


test_sort_three_values()
```

+++ {"slideshow": {"slide_type": "subslide"}}

**Exercise** The above sorting algorithm is inefficient because some conditions may be checked more than once.  
Improve the program to eliminate duplicate checks.  
*Hint:* Do not use chained comparison operators or compound boolean expressions.

```{code-cell}
---
nbgrader:
  grade: false
  grade_id: efficient-sort_three_values
  locked: false
  schema_version: 3
  solution: true
  task: false
slideshow:
  slide_type: '-'
---
def sort_three_values(x, y, z):
    if x <= y:
        if y <= z:
            print(x, y, z)
        elif x <= z:
            print(x, z, y)
        else:
            print(z, x, y)
    ### BEGIN SOLUTION
    elif z <= y:
        print(z, y, x)
    elif z <= x:
        print(y, z, x)
    else:
        print(y, x, z)
    ### END SOLUTION
        
sort_three_values(10,17,14)
```
