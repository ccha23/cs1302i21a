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

# Cybersecurity

+++ {"slideshow": {"slide_type": "-"}, "tags": ["remove-cell"]}

**CS1302 Introduction to Computer Programming**
___

+++ {"slideshow": {"slide_type": "subslide"}}

Python is a popular tool among hackers and engineers. In this lab, you will learn Cryptology in cybersecurity, which covers
- [Cryptography](https://en.wikipedia.org/wiki/Cryptography): Encryption and decryption using a cipher.
- [Cryptanalysis](https://en.wikipedia.org/wiki/Cryptanalysis): Devising an attack to break a cipher.

+++ {"slideshow": {"slide_type": "slide"}}

## Caesar symmetric key cipher

+++ {"slideshow": {"slide_type": "fragment"}}

We first implements a simple cipher called the [Caesar cipher](https://en.wikipedia.org/wiki/Caesar_cipher).

```{code-cell}
---
slideshow:
  slide_type: '-'
---
%%html
<iframe width="912" height="513" src="https://www.youtube.com/embed/sMOZf4GN3oc" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
```

+++ {"slideshow": {"slide_type": "subslide"}}

### Encrypt/decrypt a character

+++ {"slideshow": {"slide_type": "fragment"}}

**How to encrypt a character?**

+++ {"slideshow": {"slide_type": "fragment"}}

The following code encrypts a character `char` using a non-negative integer `key`.

```{code-cell}
---
code_folding: []
slideshow:
  slide_type: '-'
---
cc_n = 1114112


def cc_encrypt_character(char, key):
    '''
    Return the encryption of a character by an integer key using Caesar cipher.
    
    Parameters
    ----------
    char (str): a unicode (UTF-8) character to be encrypted.
    key (int): secret key to encrypt char.
    '''
    char_code = ord(char)
    shifted_char_code = (char_code + key) % cc_n
    encrypted_char = chr(shifted_char_code)
    return encrypted_char
```

+++ {"slideshow": {"slide_type": "fragment"}}

For example, to encrypt the letter `'A'` using a secret key `5`:

```{code-cell}
---
slideshow:
  slide_type: '-'
---
cc_encrypt_character('A', 5)
```

+++ {"slideshow": {"slide_type": "fragment"}}

The character `'A'` is encrypted to the character `'F'` as follows:

1. `ord(char)` return the integer `65` that is the code point (integer representation) of the unicode of `'A'`. 
2. `(char_code + key) % cc_n` cyclic shifts the code by the key `5`.
3. `chr(shifted_char_code)` converts the shifted code back to a character, which is `'F'`.

| Encryption                      |     |       |     |     |     |     |     |     |
| ------------------------------- | --- | ----- | --- | --- | --- | --- | --- | --- |
| `char`                          | ... | **A** | B   | C   | D   | E   | F   | ... |
| `ord(char)`                     | ... | **65**| 66  | 67  | 68  | 69  | 70  | ... |
| `(ord(char) + key) % cc_n`      | ... | **70**| 71  | 72  | 73  | 74  | 75  | ... |
| `(chr(ord(char) + key) % cc_n)` | ... | **F** | G   | H   | I   | J   | K   | ... |

+++ {"slideshow": {"slide_type": "fragment"}}

You may learn more about `ord` and `chr` from their docstrings:

```{code-cell}
---
slideshow:
  slide_type: '-'
---
help(ord)
help(chr)
```

+++ {"slideshow": {"slide_type": "subslide"}}

**How to decrypt a character?**

+++ {"slideshow": {"slide_type": "fragment"}}

Mathematically, we define the encryption and decryption of a character for Caesar cipher as

$$ \begin{aligned} E(x,k) &:= x + k \mod n & \text{(encryption)} \\
D(x,k) &:= x - k \mod n & \text{(decryption),} \end{aligned}
$$
where $x$ is the character code in $\{0,\dots,n\}$ and $k$ is the secret key. `mod` operator above is the modulo operator. In Mathematics, it has a lower precedence than addition and multiplication and is typeset with an extra space accordingly.

+++ {"slideshow": {"slide_type": "fragment"}}

The encryption and decryption satisfies the recoverability condition

$$ D(E(x,k),k) = x $$
so two people with a common secret key can encrypt and decrypt a character, but others not knowing the key cannot. This is a defining property of a [symmetric cipher](https://en.wikipedia.org/wiki/Symmetric-key_algorithm).  

+++ {"slideshow": {"slide_type": "fragment"}}

The following code decrypts a character using a key.

```{code-cell}
---
slideshow:
  slide_type: '-'
---
def cc_decrypt_character(char, key):
    '''
    Return the decryption of a character by the key using Caesar cipher.
    
    Parameters
    ----------
    char (str): a unicode (UTF-8) character to be decrypted.
    key (int): secret key to decrypt char.
    '''
    char_code = ord(char)
    shifted_char_code = (char_code - key) % cc_n
    decrypted_char = chr(shifted_char_code)
    return decrypted_char
```

+++ {"slideshow": {"slide_type": "fragment"}}

For instance, to decrypt the letter `'F'` by the secret key `5`:

```{code-cell}
---
slideshow:
  slide_type: '-'
---
cc_decrypt_character('F',5)
```

+++ {"slideshow": {"slide_type": "fragment"}}

The character `'F'` is decrypted back to `'A'` because
`(char_code - key) % cc_n` reverse cyclic shifts the code by the key `5`.

| Encryption                      |     |       |     |     |     |     |     |     | Decryption                      |
| ------------------------------- | --- | ----- | --- | --- | --- | --- | --- | --- | ------------------------------- |
| `char`                          | ... | **A** | B   | C   | D   | E   | F   | ... | `(chr(ord(char) - key) % cc_n)` |
| `ord(char)`                     | ... | **65**| 66  | 67  | 68  | 69  | 70  | ... | `(ord(char) - key) % cc_n`      |
| `(ord(char) + key) % cc_n`      | ... | **70**| 71  | 72  | 73  | 74  | 75  | ... | `ord(char)`                     |
| `(chr(ord(char) + key) % cc_n)` | ... | **F** | G   | H   | I   | J   | K   | ... | `char`                          |

+++ {"slideshow": {"slide_type": "subslide"}}

**Exercise** Why did we set `cc_n = 1114112`? Explain whether the recoverability property may fail if we set `cc_n` to a bigger number or remove `% cc_n` for both `cc_encrypt_character` and `cc_decrypt_character`.

+++ {"nbgrader": {"grade": true, "grade_id": "modulo", "locked": false, "points": 1, "schema_version": 3, "solution": true, "task": false}, "slideshow": {"slide_type": "-"}}

`cc_n` is set to be the number of unicode characters. `ord` returns a code point between `0` and `cc_n-1`, so *the modulo operator ensures the shifted character code `shifted_char_code` remains a valid character code*. If we set `cc_n` to a bigger number or remove the modular operation, the code can fail because `shifted_char_code` may not be a valid code. E.g., `chr(1114112)` causes a ValueError.

+++ {"slideshow": {"slide_type": "slide"}}

### Encrypt a plaintext and decrypt a ciphertext

+++ {"slideshow": {"slide_type": "fragment"}}

Of course, it is more interesting to encrypt a string instead of a character. The following code implements this in one line.

```{code-cell}
---
slideshow:
  slide_type: '-'
---
def cc_encrypt(plaintext, key):
    '''
    Return the ciphertext of a plaintext by the key using Caesar cipher.
    
    Parameters
    ----------
    plaintext (str): a unicode (UTF-8) message in to be encrypted.
    key (int): secret key to encrypt plaintext.
    '''
    return ''.join([chr((ord(char) + key) % cc_n) for char in plaintext])
```

+++ {"slideshow": {"slide_type": "fragment"}}

The above function encrypts a message, referred to as the *plaintext*, by replacing each character with its encryption.  
This is referred to as a [*substitution cipher*](https://en.wikipedia.org/wiki/Substitution_cipher).

+++ {"slideshow": {"slide_type": "subslide"}}

**Exercise** Define a function `cc_decrypt` that
- takes a string `ciphertext` and an integer `key`, and
- returns the plaintext that encrypts to `ciphertext` by the key using Caesar cipher.

```{code-cell}
---
nbgrader:
  grade: false
  grade_id: cc_decrypt
  locked: false
  schema_version: 3
  solution: true
  task: false
slideshow:
  slide_type: '-'
---
def cc_decrypt(ciphertext, key):
    '''
    Return the plaintext that encrypts to ciphertext by the key using Caesar cipher.
    
    Parameters
    ----------
    ciphertext (str): message to be decrypted.
    key (int): secret key to decrypt the ciphertext.
    '''
    ### BEGIN SOLUTIONS
    return ''.join([chr((ord(char) - key) % cc_n) for char in ciphertext])
    ### END SOLUTIONS
```

```{code-cell}
---
code_folding: []
nbgrader:
  grade: true
  grade_id: test-cc_decrypt
  locked: true
  points: 1
  schema_version: 3
  solution: false
  task: false
slideshow:
  slide_type: '-'
---
# tests
assert cc_decrypt(r'bcdefghijklmnopqrstuvwxyz{',1) == 'abcdefghijklmnopqrstuvwxyz'
assert cc_decrypt(r'Mjqqt1%\twqi&',5) == 'Hello, World!'
### BEGIN HIDDEN TESTS
assert cc_decrypt(r'­ÒÇÖÝÔØÓËÖÅÔÌÝÅ×ÙÆ×ØÍØÙØÍÓÒÇÍÔÌÉÖÍ×ÅÑÉØÌÓÈÓÊÉÒÇÖÝÔØÍÒËÍÒÛÌÍÇÌÙÒÍØ×ÓÊÔÐÅÍÒØÉÜØÅÖÉÖÉÔÐÅÇÉÈÛÍØÌÇÍÔÌÉÖØÉÜØÅÇÇÓÖÈÍÒËØÓÅÊÍÜÉÈ×Ý×ØÉÑØÌÉÙÒÍØ×ÑÅÝÆÉ×ÍÒËÐÉÐÉØØÉÖ×ØÌÉÑÓ×ØÇÓÑÑÓÒÔÅÍÖ×ÓÊÐÉØØÉÖ×ØÖÍÔÐÉØ×ÓÊÐÉØØÉÖ×ÑÍÜØÙÖÉ×ÓÊØÌÉÅÆÓÚÉÅÒÈ×ÓÊÓÖØÌ',100) == 'In cryptography, a substitution cipher is a method of encrypting in which units of plaintext are replaced with ciphertext, according to a fixed system; the "units" may be single letters (the most common), pairs of letters, triplets of letters, mixtures of the above, and so forth.'
### END HIDDEN TESTS
```

+++ {"slideshow": {"slide_type": "slide"}}

## Brute-force attack

+++

### Create an English dictionary

+++ {"slideshow": {"slide_type": "fragment"}}

You will launch a brute-force attack to guess the key that encrypts an English text. The idea is simple: 

- You try decrypting the ciphertext with different keys, and 
- see which of the resulting plaintexts make most sense (most english-like).

+++ {"slideshow": {"slide_type": "fragment"}}

To check whether a plaintext is English-like, we need to have a list of English words. One way is to type them out
but this is tedious. Alternatively, we can obtain the list from the *Natural Language Toolkit (NLTK)*: 

```{code-cell}
---
slideshow:
  slide_type: '-'
---
import nltk
nltk.download('words')
from nltk.corpus import words
```

+++ {"slideshow": {"slide_type": "subslide"}}

`words.words()` returns a list of words. We can check whether a string is in the list using the operator `in`. 

```{code-cell}
---
slideshow:
  slide_type: '-'
---
for word in 'Ada', 'ada', 'Hello', 'hello':
    print('{!r} in dictionary? {}'.format(word, word in words.words()))
```

+++ {"slideshow": {"slide_type": "fragment"}}

However there are two issues:
- Checking membership is slow for a long list.
- Both 'Hello' and 'ada' are English-like but they are not in the words_list.

+++ {"slideshow": {"slide_type": "subslide"}}

**Exercise** Using the method `lower` of `str` and the constructor `set`, assign `dictionary` to a set of lowercase English words from `words.words()`.

```{code-cell}
---
nbgrader:
  grade: false
  grade_id: nltk
  locked: false
  schema_version: 3
  solution: true
  task: false
slideshow:
  slide_type: '-'
---
### BEGIN SOLUTION
dictionary = set(word.lower() for word in words.words())
#dictionary=set()
for word in words.words():
    dictionary.add(word.lower())

### END SOLUTION
```

```{code-cell}
---
code_folding: []
nbgrader:
  grade: true
  grade_id: test-nltk
  locked: true
  points: 1
  schema_version: 3
  solution: false
  task: false
slideshow:
  slide_type: '-'
---
# tests
assert isinstance(dictionary,set) and len(dictionary) == 234377
assert all(word in dictionary for word in ('ada', 'hello'))
assert all(word not in dictionary for word in ('Ada', 'hola'))
### BEGIN TESTS
assert 'world' in dictionary
assert not 'mundo' in dictionary
### END TESTS
```

+++ {"slideshow": {"slide_type": "subslide"}}

### Identify English-like text

+++ {"slideshow": {"slide_type": "fragment"}}

To determine how English-like a text is, we calculate the following score:

$$
\frac{\text{number of English words in the text}}{\text{number of tokens in the text}} 
$$
where tokens are substrings (not necessarily an English word) separated by white space characters in the text.

```{code-cell}
---
slideshow:
  slide_type: '-'
---
def tokenizer(text):
    '''Returns the list of tokens of the text.'''
    return text.split()

def get_score(text):
    '''Return the fraction of tokens which appear in dictionary.'''
    tokens = tokenizer(text)
    words = [token for token in tokens if token in dictionary]
    return len(words)/len(tokens)

# tests
get_score('hello world'), get_score('Hello, World!')
```

+++ {"slideshow": {"slide_type": "fragment"}}

As shown in tests above, the code fails to handle text with punctuations and uppercase letters properly.  
In particular, 
- while `get_score` recognizes `hello world` as English-like and returns the maximum score of 1, 
- it fails to recognize `Hello, World!` as English-like and returns the minimum score of 0.

+++ {"slideshow": {"slide_type": "fragment"}}

Why? This is because every words in `dictionary`
- are in lowercase, and
- have no leading/trailing punctuations.

+++ {"slideshow": {"slide_type": "subslide"}}

**Exercise** Define a funtion `tokenizer` that 
- takes a string `text` as an argument, and
- returns a `list` of tokens obtained by
  1. splitting `text` into a list using `split()`;
  2. removing leading/trailing punctuations in `string.punctuation` using the `strip` method; and
  3. converting all items of the list to lowercase using `lower()`.

```{code-cell}
---
nbgrader:
  grade: false
  grade_id: tokenizer
  locked: false
  schema_version: 3
  solution: true
  task: false
slideshow:
  slide_type: '-'
---
import string

def tokenizer(text):
    '''Returns the list of tokens of the text such that 
    1) each token has no leading or training spaces/punctuations, and 
    2) all letters in each tokens are in lowercase.'''
    ### BEGIN SOLUTION
    return [token.strip(string.punctuation).lower() for token in text.split()]
    ### END SOLUTION
```

```{code-cell}
---
code_folding: []
nbgrader:
  grade: true
  grade_id: test-tokenizer
  locked: true
  points: 1
  schema_version: 3
  solution: false
  task: false
slideshow:
  slide_type: '-'
---
# tests
assert tokenizer('Hello, World!') == ['hello', 'world']
assert get_score('Hello, World!') >= 0.99999
assert tokenizer('Do you know Jean-Pierre?') == ['do', 'you', 'know', 'jean-pierre']
assert get_score('Do you know Jean-Pierre?') >= 0.99999
### BEGIN HIDDEN TESTS
assert tokenizer('Jean-Christophe is a good friend of mine.' ) == ['jean-christophe', 'is', 'a', 'good', 'friend', 'of', 'mine']
assert get_score('Jean-Christophe is a good friend of mine.' ) >= 0.99999
assert tokenizer('Hello, 昍昍.') == ['hello', '昍昍']
assert get_score('Hello, 昍昍.') >= 0.49999
### END HIDDEN TESTS
```

+++ {"slideshow": {"slide_type": "slide"}}

### Launch a brute-force attack

+++ {"slideshow": {"slide_type": "subslide"}}

**Exercise** Define the function `cc_attack` that 
- takes as arguments
    - a string `ciphertext`,
    - a floating point number `threshold` in the interval $(0,1)$ with a default value of $0.6$, and
- returns a generator that  
    - generates one-by-one in ascending order guesses of the key that
    - decrypt `ciphertext` to texts with scores at least the `threshold`.

```{code-cell}
---
nbgrader:
  grade: false
  grade_id: cc_attack
  locked: false
  schema_version: 3
  solution: true
  task: false
slideshow:
  slide_type: '-'
---
def cc_attack(ciphertext, threshold = 0.6):
    '''Returns a generator that generates the next guess of the key that 
    decrypts the ciphertext to a text with get_score(text) at least the threshold.
    '''
    ### BEGIN SOLUTION
    for key in range(cc_n):
        if get_score(cc_decrypt(ciphertext,key)) >= threshold:
            yield key
    ### END SOLUTION
```

```{code-cell}
---
code_folding: []
nbgrader:
  grade: true
  grade_id: test-cc_attack
  locked: true
  points: 1
  schema_version: 3
  solution: false
  task: false
slideshow:
  slide_type: '-'
---
# tests
ciphertext = cc_encrypt("Hello, World!",12345)
key_generator = cc_attack(ciphertext)
key_guess = next(key_generator)
assert key_guess == 12345
text = cc_decrypt(ciphertext, key_guess)
print('guess of the key: {}\nscore: {}\ntext :{}'.format(key_guess,get_score(text),text))
### BEGIN HIDDEN TESTS
assert next(cc_attack(cc_encrypt("Jean-Christophe is a good friend of mine.", 10))) == 10
assert next(cc_attack(cc_encrypt("Jean-Christophe is a good friend of mine.", 123))) == 123
### END HIDDEN TESTS
```

+++ {"slideshow": {"slide_type": "slide"}}

## Challenge

+++

Another symmetric key cipher is [columnar transposition cipher](https://en.wikipedia.org/wiki/Transposition_cipher#Columnar_transposition). A transposition cipher encrypts a text by permuting instead of substituting characters.

+++ {"slideshow": {"slide_type": "subslide"}}

**Exercise** Study and implement the irregular case of the [columnar transposition cipher](https://en.wikipedia.org/wiki/Transposition_cipher#Columnar_transposition) as described in Wikipedia page. Define the functions 
- `ct_encrypt(plaintext, key)` for encryption, and 
- `ct_decrypt(ciphertext, key)` for decryption. 

You can assume the plaintext is in uppercase and has no spaces/punctuations. 

+++

*Hints:* See the text cases for an example of `plaintext`, `key`, and the corresponding `ciphertext`. You can but are not required to follow the solution template below:

```Python
def argsort(seq):
    '''A helper function that returns the tuple of indices that would sort the
    sequence seq.'''
    return tuple(x[0] for x in sorted(enumerate(seq), key=lambda x: x[1]))


def ct_idx(length, key):
    '''A helper function that returns the tuple of indices that would permute 
    the letters of a message according to the key using the irregular case of 
    columnar transposition cipher.'''
    seq = tuple(range(length))
    return [i for j in argsort(key) for i in _______________]


def ct_encrypt(plaintext, key):
    '''
    Return the ciphertext of a plaintext by the key using the irregular case
    of columnar transposition cipher.
    
    Parameters
    ----------
    plaintext (str): a message in uppercase without punctuations/spaces.
    key (str): secret key to encrypt plaintext.
    '''
    return ''.join([plaintext[i] for i in ct_idx(len(plaintext), key)])


def ct_decrypt(ciphertext, key):
    '''
    Return the plaintext of the ciphertext by the key using the irregular case
    of columnar transposition cipher.
    
    Parameters
    ----------
    ciphertext (str): a string in uppercase without punctuations/spaces.
    key (str): secret key to decrypt ciphertext.
    '''        
    return _______________________________________________________________________
```

```{code-cell}
---
nbgrader:
  grade: false
  grade_id: ct
  locked: false
  schema_version: 3
  solution: true
  task: false
slideshow:
  slide_type: '-'
---
### BEGIN SOLUTION
def argsort(seq):
    '''A helper function that returns the tuple of indices that would sort the
    sequence seq.'''
    return tuple(x[0] for x in sorted(enumerate(seq), key=lambda x: x[1]))


def ct_idx(length, key):
    '''A helper function that returns the tuple of indices that would permute 
    the letters of a message according to the key using the irregular case of 
    columnar transposition cipher.'''
    seq = tuple(range(length))
    return [i for j in argsort(key) for i in seq[j::len(key)]]


def ct_encrypt(plaintext, key):
    '''
    Return the ciphertext of a plaintext by the key using the irregular case
    of columnar transposition cipher.
    
    Parameters
    ----------
    plaintext (str): a message in uppercase without punctuations/spaces.
    key (str): secret key to encrypt plaintext.
    '''
    return ''.join([plaintext[i] for i in ct_idx(len(plaintext), key)])


def ct_decrypt(ciphertext, key):
    '''
    Return the plaintext of the ciphertext by the key using the irregular case
    of columnar transposition cipher.
    
    Parameters
    ----------
    ciphertext (str): a string in uppercase without punctuations/spaces.
    key (str): secret key to decrypt ciphertext.
    '''        
    return ''.join([ciphertext[i] for i in argsort(ct_idx(len(ciphertext), key))])
### END SOLUTION
```

```{code-cell}
---
nbgrader:
  grade: true
  grade_id: test-ct
  locked: true
  points: 1
  schema_version: 3
  solution: false
  task: false
slideshow:
  slide_type: '-'
---
# tests
key = 'ZEBRAS'
plaintext = 'WEAREDISCOVEREDFLEEATONCE'
ciphertext = 'EVLNACDTESEAROFODEECWIREE'
assert ct_encrypt(plaintext, key) == ciphertext
assert ct_decrypt(ciphertext, key) == plaintext
### BEGIN HIDDEN TESTS
key = 'PYTHON'
assert ct_encrypt('CS1302INTRODUCTIONTOCOMPUTERPROGRAMMING', key) == '3RIORA2DNPRM0OOMPMCIUTUOI1TTCERGSNCOTGN'
assert ct_decrypt('3RIORA2DNPRM0OOMPMCIUTUOI1TTCERGSNCOTGN', key) == 'CS1302INTRODUCTIONTOCOMPUTERPROGRAMMING'
### END HIDDEN TESTS
```
