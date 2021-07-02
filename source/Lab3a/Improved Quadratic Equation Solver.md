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

# Improved Quadratic Equation Solver

+++ {"slideshow": {"slide_type": "-"}, "tags": ["remove-cell"]}

**CS1302 Introduction to Computer Programming**
___

+++ {"slideshow": {"slide_type": "subslide"}}

In this notebook, we will improve the quadratic equation solver in the previous lab using conditional executions.  
First of all, run the following to setup the environment.

```{code-cell}
---
slideshow:
  slide_type: skip
---
%reset -f
from ipywidgets import interact
import math
```

+++ {"slideshow": {"slide_type": "subslide"}}

## Zero Discriminant

+++ {"slideshow": {"slide_type": "fragment"}}

Recall that the quadratic equation is

$$
ax^2+bx+c=0
$$
where $a$, $b$, and $c$ are real-valued coefficients, and $x$ is the unknown variable. The roots are normally given by

$$
\frac{-b-\sqrt{b^2-4ac}}{2a}, \frac{-b+\sqrt{b^2-4ac}}{2a}.
$$

+++ {"slideshow": {"slide_type": "fragment"}}

The roots are the same (repeated) when the discriminant $b^2-4ac$ is zero.

+++ {"slideshow": {"slide_type": "subslide"}}

**Exercise** Assign to `roots` only one root when the discriminant is zero. E.g., if $(a,b,c)=(1,-2,1)$, then `roots` should be assigned the value `1.0` instead of `1.0, 1.0`. If there are two roots, give them in the order of the above formula.

+++ {"slideshow": {"slide_type": "fragment"}}

*Hint*: Use the [`if` statement](https://docs.python.org/3/reference/compound_stmts.html#if).

+++

*Hint:* The following is a solution template with some missing code. You are NOT required to follow the template.
```Python
def get_roots(a, b, c):
    d = b**2 - 4 * a * c    # discriminant
    if math.isclose(d, 0):
        roots = __________  # repeated root
    else:
        d **= 0.5
        roots = __________________________________
    return roots
```

```{code-cell}
---
nbgrader:
  grade: false
  grade_id: zero_determininant
  locked: false
  schema_version: 3
  solution: true
  task: false
slideshow:
  slide_type: fragment
---
def get_roots(a, b, c):
    d = b**2 - 4 * a * c    # discriminant
    if math.isclose(d, 0):
    ### BEGIN SOLUTION
        roots = -b / 2 / a  # repeated root
    else:
        d **= 0.5           # *
        roots = (- b - d) / 2 / a, (- b + d) / 2 / a
    ### END SOLUTION
    return roots
```

```{code-cell}
---
code_folding: [0]
nbgrader:
  grade: true
  grade_id: test-zero_determinant
  locked: true
  points: 1
  schema_version: 3
  solution: false
  task: false
---
# tests
def test_get_roots(roots, a, b, c):
    roots_ = get_roots(a, b, c)
    if roots is None:
        correct = roots_ is None
    elif isinstance(roots, float):
        correct = isinstance(roots_, float) and math.isclose(roots, roots_)
    else:
        correct = isinstance(roots_, tuple) and len(roots_) == 2 and all([
            math.isclose(root, roots_) for root, roots_ in zip(roots, roots_)
        ])
    if not correct:
        print(f'With (a, b, c)={a,b,c}, roots should be {roots} not {roots_}.')
    assert correct

test_get_roots((-1.0, 0.0), 1, 1, 0)
test_get_roots(0.0, 1, 0, 0)
### BEGIN HIDDEN TESTS
test_get_roots(1.0, 1, -2, 1)
### END HIDDEN TESTS
```

+++ {"slideshow": {"slide_type": "fragment"}}

**Exercise** Why use `math.isclose(d,0)` instead of `d == 0`?

+++ {"nbgrader": {"grade": true, "grade_id": "isclose", "locked": false, "points": 1, "schema_version": 3, "solution": true, "task": false}, "slideshow": {"slide_type": "fragment"}}

Since `d` is a floating point number, it may not be the precise value of the determinant. `d == 0` may return false due to precision error even when the discriminant is supposed to be zero.

+++ {"slideshow": {"slide_type": "slide"}}

## Linear Equation

+++ {"slideshow": {"slide_type": "fragment"}}

If $a=0$, the earlier formula for the roots are invalid due to division by zero. Nevertheless, the equation remains valid:

$$
bx + c=0.
$$

+++

**Exercise** Improve the function `get_roots` to return the root $-\frac{c}{b}$ if $a=0$.

+++

*Hint:* Solution template:
```Python
def get_roots(a, b, c):
    d = b**2 - 4 * a * c    # discriminant
    if __________________:
        roots = ______
    elif math.isclose(d, 0):
        roots = __________  # repeated root
    else:
        d **= 0.5
        roots = __________________________________
    return roots
```

```{code-cell}
---
nbgrader:
  grade: false
  grade_id: linear
  locked: false
  schema_version: 3
  solution: true
  task: false
---
def get_roots(a, b, c):
    d = b**2 - 4 * a * c
    ### BEGIN SOLUTION
    if math.isclose(a, 0):
        roots = -c / b
    elif math.isclose(d, 0):
        roots = -b / 2 / a
    else:
        d **= 0.5
        roots = (-b - d) / 2 / a, (-b + d) / 2 / a
    ### END SOLUTION
    return roots
```

```{code-cell}
---
code_folding: []
nbgrader:
  grade: true
  grade_id: test-linear
  locked: true
  points: 1
  schema_version: 3
  solution: false
  task: false
---
# tests
def test_get_roots(roots, a, b, c):
    roots_ = get_roots(a, b, c)
    if roots is None:
        correct = roots_ is None
    elif isinstance(roots, float):
        correct = isinstance(roots_, float) and math.isclose(roots, roots_)
    else:
        correct = isinstance(roots_, tuple) and len(roots_) == 2 and all([
            math.isclose(root, roots_) for root, roots_ in zip(roots, roots_)
        ])
    if not correct:
        print(f'With (a, b, c)={a,b,c}, roots should be {roots} not {roots_}.')
    assert correct


test_get_roots((-1.0, -0.0), 1, 1, 0)
test_get_roots(0.0, 1, 0, 0)
test_get_roots(0.5, 0, -2, 1)
### BEGIN HIDDEN TESTS
test_get_roots(-2.0, 0, 1, 2)
test_get_roots(2.0, 0, 1, -2)
### END HIDDEN TESTS
```

## Degenerate Cases

+++

What if $a=b=0$? In that case, the equation becomes

$$
c = 0
$$
which is always satisfied if $c=0$, but never satisfied if $c\neq 0$. 

+++ {"slideshow": {"slide_type": "fragment"}}

**Exercise** Improve the function `get_roots` to return root(s) under all cases:
- If $a=0$ and $b\neq 0$, assign `roots` to the single root $-\frac{c}{b}$. 
- If $a=b=0$ and $c\neq 0$, assign `roots` to `None`.  
    Note that `None` is an object, not a string.
- If $a=b=c=0$, there are infinitely many roots. Assign to `roots` the tuple `-float('inf'), float('inf')`.  
    Note that `float('inf')` converts the string `'inf'` to a floating point value that represents $\infty$.

+++ {"slideshow": {"slide_type": "fragment"}}

*Hint:* Use nested `if` statements such as the followings (with the blanks filled in properly):
```Python
def get_roots(a, b, c):
    d = b**2 - 4 * a * c
    if __________________:
        if __________________:
            if __________________:
                roots = -float('inf'), float('inf')
            else:
                roots = None
        else:
            ______________
    elif math.isclose(d, 0):
        roots = __________  # repeated root
    else:
        d **= 0.5
        roots = __________________________________
    return roots
```

```{code-cell}
---
nbgrader:
  grade: false
  grade_id: degenerate
  locked: false
  schema_version: 3
  solution: true
  task: false
slideshow:
  slide_type: skip
---
def get_roots(a, b, c):
    d = b**2 - 4 * a * c
    ### BEGIN SOLUTION
    if math.isclose(a, 0):
        if math.isclose(b, 0):
            if math.isclose(c, 0):
                roots = -float('inf'), float('inf')
            else:
                roots = None
        else:
            roots = -c / b
    elif math.isclose(d, 0):
        roots = -b / 2 / a  # repeated root
    else:
        d **= 0.5
        roots = (-b - d) / 2 / a, (-b + d) / 2 / a
    ### END SOLUTION
    return roots
```

```{code-cell}
---
code_folding: [0]
nbgrader:
  grade: true
  grade_id: test_degenerate
  locked: true
  points: 1
  schema_version: 3
  solution: false
  task: false
slideshow:
  slide_type: skip
---
# tests
def test_get_roots(roots, a, b, c):
    roots_ = get_roots(a, b, c)
    if roots is None:
        correct = roots_ is None
    elif isinstance(roots, float):
        correct = isinstance(roots_, float) and math.isclose(roots, roots_)
    else:
        correct = isinstance(roots_, tuple) and len(roots_) == 2 and all([
            math.isclose(root, roots_) for root, roots_ in zip(roots, roots_)
        ])
    if not correct:
        print(f'With (a, b, c)={a,b,c}, roots should be {roots} not {roots_}.')
    assert correct


test_get_roots((-1.0, 0.0), 1, 1, 0)
test_get_roots(0.0, 1, 0, 0)
test_get_roots((-float('inf'), float('inf')), 0, 0, 0)
test_get_roots(None, 0, 0, 1)
test_get_roots(0.5, 0, -2, 1)
test_get_roots(1.0, 1, -2, 1)
### BEGIN HIDDEN TESTS
def generate_test_get_roots():
    for args in [(1, 1, 0), (1, 0, 0), (0, 0, 1), (0, -2, 1), (1, -2, 1)]:
        print(f'test_get_roots{(get_roots(*args),*args)}', sep='\n')


# generate_test_get_roots()
### END HIDDEN TESTS
```

## Run the calculator

+++

After you have complete the exercises, you can run your robust solver below:

```{code-cell}
---
code_folding: [0]
slideshow:
  slide_type: '-'
---
# quadratic equations solver
@interact(a=(-10,10,1),b=(-10,10,1),c=(-10,10,1))
def quadratic_equation_solver(a=1,b=2,c=1):
    print('Root(s):',get_roots(a,b,c))
```
