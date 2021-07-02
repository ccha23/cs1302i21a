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

# Mastermind

+++ {"slideshow": {"slide_type": "-"}, "tags": ["remove-cell"]}

**CS1302 Introduction to Computer Programming**
___

+++ {"slideshow": {"slide_type": "subslide"}}

In this notebook, you will write a game called [*Mastermind*](https://en.wikipedia.org/wiki/Mastermind_(board_game)).  
Play the video below to learn about the rule of the game.

```{code-cell}
---
code_folding: [0]
jupyter:
  outputs_hidden: true
slideshow:
  slide_type: '-'
---
%%html
<iframe width="912" height="513" src="https://www.youtube.com/embed/wsYPsrzCKiA" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
```

1. **Mastermind** first creates a hidden `code` of length `code_length` consisting code pegs with possibly duplicate colors chosen from a sequence of `colors`.
1. **Coderbreaker** provides a `guess` of the `code`.
1. **Mastermind** generates a `feedback` consisting of key pegs of black and white colors:
    - The number of black pegs (`black_key_pegs_count`) is the number of code pegs that are the correct colors in the correct positions. 
    - The number of white pegs (`white_key_pegs_count`) is the number of code pegs that are the correct colors but in incorrect positions.
    - Each code peg should be counted only once, i.e., a code peg cannot be awarded more than one key peg. E.g.,
        - If the `code` is `'RBGG'` and `guess` is `'BGGG'`, then 
        - the feedback should be `'bbw'` with 
            - `black_key_pegs_count == 2` because of `__GG` in the guess, and
            - `white_key_pegs_count == 1` because of `_B__` in the guess. 
            - `_G__` in the `guess` should not be awarded an additional white peg because `__GG` in the `code` has been counted.
1. **Codebreaker** wins if the code is correctly guessed within certain number (`max_num_guesses`) of guesses.

+++ {"slideshow": {"slide_type": "slide"}}

## Random Code Generation

+++

The first exercise is to generate a random hidden code so even one person can play the game as Codebreaker.  
Watch the following video to understand how computers generate random objects.

```{code-cell}
---
code_folding: []
jupyter:
  outputs_hidden: true
---
%%html
<iframe width="912" height="513" src="https://www.youtube.com/embed/GtOt7EBNEwQ" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
```

To generate random content in Python, we can import the **random** module, which provides some useful functions to generate random objects as follows.

```{code-cell}
import random
for i in range(10): print(random.random())  # random floating point numbers in [0,1)
```

```{code-cell}
for i in range(10): print(random.randint(3,10),end=' ')  # random integer in range [3,10]
```

```{code-cell}
for i in range(10): print(random.choice('RBG'),end='')  # random element in the sequence 'RBG'
```

We can generate a reproducible pseudo-random sequence by specifying the seed.  
By default Python uses the system time as seed.

```{code-cell}
# repeatedly run the cell to see new sequences.
random.seed(123456)
for i in range(10): print(random.randint(3,10),end=' ')
```

**Exercise** Define a function that generates a random `code`. The functions takes in
- a string `colors` whose characters represent distinct colors to choose from, and
- a positive integer `code_length` representing the length of the code.

For instance, `get_code('ROYGBP',4)` returns a code of `4` code pegs randomly with colors chosen from `'R'`ed, `'O'`range, `'Y'`ellow, `'G'`reen, `'B'`lue, and `'P'`urple. One possible outcome is `'ROYY'`.

```{code-cell}
---
nbgrader:
  grade: false
  grade_id: get_code
  locked: false
  schema_version: 3
  solution: true
  task: false
---
import random
def get_code(colors, code_length):
    code = ''
    """
    The function body will iterate code_length times.
    In each iteration, generate a random (integer) position in range 0 to len(colors)-1. 
    From color, get the character at that random position and append the character to code
    """
    ### BEGIN SOLUTION
    for i in range(code_length):
        p = int(random.random()*len(colors))
        code += colors[p]
    ### END SOLUTION
    return code
```

```{code-cell}
---
code_folding: [0]
nbgrader:
  grade: true
  grade_id: test-get_code
  locked: true
  points: 1
  schema_version: 3
  solution: false
  task: false
slideshow:
  slide_type: '-'
---
### BEGIN HIDDEN TESTS

def test_get_code(colors, code_length):
    code = get_code(colors,code_length)
    if (len(code)!=code_length): 
        return False
    for c in code:
        if (c not in colors):
            return False
    return True

# Unused color codes to check whether the function is really reading from input string
for l in range(10):
    assert(test_get_code("ACDEFHIJ",l))  
    
### END HIDDEN TESTS    
```

+++ {"slideshow": {"slide_type": "subslide"}}

## Guess Validation

+++ {"slideshow": {"slide_type": "fragment"}}

**Exercise** Define a function `valid_code` that 
- takes `colors`, `code_length`, and `guess` as the first, second, and third arguments respectively, and
- return `True` if `guess` is a valid code, i.e., a string of length `code_length` with characters from those of `colors`, and
- `False` otherwise.

+++ {"slideshow": {"slide_type": "fragment"}}

*Hint:* Solution template:
```Python
def __________(colors, code_length, guess):
    if len(guess) __ code_length:
        is_valid = ____
    else:
        for peg in guess:
            for color in colors:
                if peg == color: ____
            else:
                is_valid = _____
                ____
        else:
            is_valid = ____
    return is_valid
```

```{code-cell}
---
nbgrader:
  grade: false
  grade_id: valid_code
  locked: false
  schema_version: 3
  solution: true
  task: false
slideshow:
  slide_type: skip
---
### BEGIN SOLUTION
def valid_code(colors, code_length, guess):
    if len(guess) != code_length:
        is_valid = False
    else:
        for peg in guess:
            for color in colors:
                if peg == color: break
            else:
                is_valid = False
                break
        else:
            is_valid = True
    return is_valid
### END SOLUTION
```

```{code-cell}
---
code_folding: [0]
nbgrader:
  grade: true
  grade_id: test-valid_code
  locked: true
  points: 1
  schema_version: 3
  solution: false
  task: false
slideshow:
  slide_type: skip
---
# tests
assert valid_code('RBG',1,'R') == True
assert valid_code('RBG',2,'B') == False
assert valid_code('RBG',2,'RP') == False
assert valid_code('RBG',0,'') == True
### BEGIN HIDDEN TESTS
assert valid_code('RBG',4,'RBBG') == True
assert valid_code('RBGY',2,'BY') == True
assert valid_code('RBGY',5,'RBGY') == False
### END HIDDEN TESTS
```

+++ {"slideshow": {"slide_type": "subslide"}}

## Feedback Generation

+++

According to the rules of Mastermind, double-counting of a single peg (as black and white) is not allowed. To facilitate this check, we have written a new module `markposition` that allows you to mark any non-negative integer position as counted.

+++

**Exercise** Write an `import` statement to import from the module `markposition` the functions 
- `mark_as_counted`
- `check_if_counted`, and 
- `reset_all_to_not_counted`.

```{code-cell}
---
nbgrader:
  grade: false
  grade_id: markposition
  locked: false
  schema_version: 3
  solution: true
  task: false
---
### BEGIN SOLUTION
from markposition import mark_as_counted, check_if_counted, reset_all_to_not_counted
### END SOLUTION
```

```{code-cell}
---
code_folding: [0]
nbgrader:
  grade: true
  grade_id: test-markposition
  locked: true
  points: 1
  schema_version: 3
  solution: false
  task: false
---
# Tests
reset_all_to_not_counted()
mark_as_counted(3)
assert check_if_counted(3) and not check_if_counted(0)
### BEGIN HIDDEN TESTS
reset_all_to_not_counted()
mark_as_counted(8)
assert check_if_counted(8) and not check_if_counted(0)
### END HIDDEN TESTS
```

**Exercise** Using the functions imported from `markposition`, mark only the positions `0`, `2`, `4`, `6`, `8`, and `10` as counted. All other positions are not counted.   
*Hint*: Use `help` to learn how to use the imported functions.

```{code-cell}
---
nbgrader:
  grade: false
  grade_id: reset_all_to_not_counted
  locked: false
  schema_version: 3
  solution: true
  task: false
---
### BEGIN SOLUTION
reset_all_to_not_counted()
for i in range(0,11,2):
    mark_as_counted(i)
### END SOLUTION
```

```{code-cell}
---
code_folding: [0]
nbgrader:
  grade: true
  grade_id: test-reset_all_to_not_counted
  locked: true
  points: 1
  schema_version: 3
  solution: false
  task: false
---
# Tests
for i in range(11):
    assert not check_if_counted(i) if i % 2 else check_if_counted(i)
### BEGIN HIDDEN TESTS
for i in range(22):
    assert not check_if_counted(
        i) if i % 2 or i > 10 or i < 0 else check_if_counted(i)
### END HIDDEN TESTS
```

+++ {"slideshow": {"slide_type": "fragment"}}

**Exercise** Define a function `get_feedback` that 
- takes `code` and `guess` as the first and second arguments respectively, and
- returns a feedback string that starts with the appropriate number of characters `'b'` (for black key pegs) followed by the appropriate number of characters `'w'` (for white key pegs).

+++ {"slideshow": {"slide_type": "fragment"}}

*Hint:* Solution template:
```Python
def get_feedback(code, guess):
    black_key_pegs_count = white_key_pegs_count = counted = 0
    reset_all_to_not_counted()
    for i in _________________:
        if ___________________:
            black_key_pegs_count += 1
            mark_as_counted(i)
    for i in range(len(guess)):
        for j in range(len(code)):
            if  __________________________________________________________:
                white_key_pegs_count += 1
                mark_as_counted(j)
                break
    key = 'b' * black_key_pegs_count + 'w' * white_key_pegs_count
    return key
```

```{code-cell}
---
nbgrader:
  grade: false
  grade_id: get_feedback
  locked: false
  schema_version: 3
  solution: true
  task: false
slideshow:
  slide_type: skip
---
### BEGIN SOLUTION
def get_feedback(code, guess):
    black_key_pegs_count = white_key_pegs_count = counted = 0
    reset_all_to_not_counted()
    for i in range(len(guess)):
        if guess[i] == code[i]:
            black_key_pegs_count += 1
            mark_as_counted(i)
    for i in range(len(guess)):
        for j in range(len(code)):
            if  code[i] != guess[i] == code[j] and not check_if_counted(j):
                white_key_pegs_count += 1
                mark_as_counted(j)
                break
    key = 'b' * black_key_pegs_count + 'w' * white_key_pegs_count
    return key
### END SOLUTION
```

```{code-cell}
---
code_folding: [0]
nbgrader:
  grade: true
  grade_id: test-get_feedback
  locked: true
  points: 1
  schema_version: 3
  solution: false
  task: false
slideshow:
  slide_type: skip
---
# tests
def test_get_feedback(feedback,code,guess):
    feedback_ = get_feedback(code,guess)
    correct = feedback == feedback_
    if not correct:
        print(
            f'With code="{code}" and guess="{guess}", feedback should be "{feedback}", not "{feedback_}".'
        )
    assert correct

test_get_feedback(10*'b'+'w'*0,"RGBRGBRGBY","RGBRGBRGBY")
test_get_feedback(0*'b'+'w'*10,"RGBRGBRGBY","YRGBRGBRGB")
test_get_feedback(8*'b'+'w'*0,"RGRGRGRG","RGRGRGRG")
test_get_feedback(0*'b'+'w'*8,"RGRGRGRG","GRGRGRGR")
test_get_feedback(0*'b'+'w'*6,"RRRRGGG","GGGGRRR")
test_get_feedback(1*'b'+'w'*6,"RRRRGGG","GGGRRRR")
test_get_feedback(5*'b'+'w'*2,"RRRRGGG","RRRGGGR")
test_get_feedback(1*'b'+'w'*0,"RRRRGGG","RYYPPBB")
test_get_feedback(0*'b'+'w'*1,"RRRRG","GBBBB")
test_get_feedback(0*'b'+'w'*0,"RRRRG","YBBBB")
### BEGIN HIDDEN TESTS
test_get_feedback(1*'b'+'w'*0,"BBBB","RGBY")
test_get_feedback(1*'b'+'w'*0,"RGBY","BBBB")
test_get_feedback(4*'b'+'w'*0,"RGBY","RGBY")
test_get_feedback(0*'b'+'w'*4,"RGBY","GBYR")
test_get_feedback(0*'b'+'w'*0,"RRYB","PPPP")
test_get_feedback(1*'b'+'w'*0,"RRYB","GRPP")
test_get_feedback(0*'b'+'w'*2,"RGYB","GRPP")
test_get_feedback(1*'b'+'w'*1,"RGRB","YRRY")
test_get_feedback(1*'b'+'w'*0,"RGRB","BBBB")
test_get_feedback(1*'b'+'w'*1,"RGRB","RBYY")
test_get_feedback(2*'b'+'w'*0,"RGRB","RGYY")
test_get_feedback(2*'b'+'w'*2,"RGRR","RRGR")

def generate_test_get_feedback(n):
    colors = 'ROYGBP'
    code_length = 4
    for code, guess in [[get_code(colors,code_length) for j in range(2)] for i in range(n)]:
        print(f'test_get_feedback{(get_feedback(code,guess),code,guess)}')


# generate_test_get_feedback(6)
### END HIDDEN TESTS
```

+++ {"slideshow": {"slide_type": "slide"}}

## Play the Game

+++ {"slideshow": {"slide_type": "fragment"}}

After finishing the previous exercises, you can play the game as a code breaker against a random mastermind.

```{code-cell}
# mastermind
import ipywidgets as widgets
from IPython.display import display, HTML


def main():
    '''The main function that runs the mastermind game.'''
    max_num_guesses = code_length = code = num_guesses_left = None
    is_game_ended = True
    colors = 'ROYGBP'
    color_code = {
        "R": "#F88,#F00,#800",
        "O": "#FD8,#F80,#840",
        "Y": "#FF8,#FF0,#AA0",
        "G": "#8F8,#0F0,#080",
        "B": "#88F,#00F,#008",
        "P": "#F8F,#F0F,#808",
        "b": "#888,#000,#000",
        "w": "#FFF,#EEE,#888"
    }

    # returns the HTML code for a colored peg.
    def getPeg(color, size=30):
        return '''<div style='display:inline-block;
                              background-image: radial-gradient(circle, {0}); 
                              width:{1}px; height:{1}px; border-radius:50%;'>
                  </div>'''.format(color_code[color], size)

    colors_display = widgets.HBox([widgets.Label(value='Color codes:')] + [
        widgets.HBox([widgets.Label(value=color),
                      widgets.HTML(getPeg(color))]) for color in colors
    ])

    max_num_guesses_input = widgets.IntSlider(min=5,
                                              max=15,
                                              value=10,
                                              description="# guesses:")
    code_length_input = widgets.IntSlider(min=2,
                                          max=10,
                                          value=4,
                                          description="Code length:")
    code_input = widgets.Password(description="Code:")
    start_new_game_button = widgets.Button(description="Start a new game")

    guess_input = widgets.Text(description="Guess:")
    submit_guess_button = widgets.Button(description="Submit guess")
    board = widgets.Output()
    message = widgets.Output()

    display(
        widgets.VBox([
            max_num_guesses_input, code_length_input, colors_display,
            widgets.HBox([code_input, start_new_game_button]),
            widgets.HBox([guess_input, submit_guess_button]), board, message
        ]))

    # A listener that starts a new game
    def start_new_game(button):
        nonlocal code, num_guesses_left, is_game_ended, max_num_guesses, code_length
        max_num_guesses = max_num_guesses_input.value
        code_length = code_length_input.value
        board.clear_output()
        message.clear_output()
        code = code_input.value or get_code(colors, code_length)
        with message:
            if not valid_code(colors, code_length, code):
                display(
                    HTML('''<p>The code {} is invalid.<br>
                        Leave the code box empty to randomly generated a code.
                        </p>'''.format(code)))
                is_game_ended = True
            else:
                num_guesses_left = max_num_guesses
                is_game_ended = num_guesses_left <= 0
                display(
                    HTML('<p>Game started! {} Guesses left.</p>'.format(
                        num_guesses_left)))

    # A listener that submits a guess
    def submit_guess(button):
        nonlocal num_guesses_left, is_game_ended
        guess = guess_input.value
        with message:
            message.clear_output()
            if is_game_ended:
                display(
                    HTML('''<p>Game has not started.<br> 
                        Please start a new game.</p>'''))
                return
            if not valid_code(colors, code_length, guess):
                display(HTML('<p>Invalid guess.</p>'))
                return
        feedback = get_feedback(code, guess)
        num_guesses_left -= 1
        with board:
            content = ""
            for k in guess:
                content += getPeg(k)
            content += '''<div style='display:inline-block; 
                             margin: 0px 5px 0px 30px; 
                             position:relative; top:5px;'>Feeback:</div>
                          <div style='display:inline-block; 
                             border: 1px solid; width:120px; height:30px;'>'''
            for k in feedback:
                content += getPeg(k, 28)
            content += "</div>"
            display(HTML(content))

        with message:
            message.clear_output()
            if feedback == 'b' * code_length:
                is_game_ended = True
                display(
                    HTML('<p>You won with {} guesses left!</p>'.format(
                        num_guesses_left)))
                return
            is_game_ended = num_guesses_left <= 0
            if is_game_ended:
                display(HTML('<p>Game over...</p>'))
                return
            display(HTML('<p>{} Guesses left.</p>'.format(num_guesses_left)))

    start_new_game_button.on_click(start_new_game)
    submit_guess_button.on_click(submit_guess)


main()
```
