# Pyramid
Pyramid: An stack-based esoteric language.

This language is built on [Stackylogic](http://codegolf.stackexchange.com/questions/84851/run-stackylogic).

In Pyramid, there are nine commands:

Original commands (of StackyLogic):

- `0`: Move the pointer up one place in the stack.
- `1`: Move the pointer down one place in the stack.
- `?`: Input (only 0 or 1 allowed). The input is then used as a 0 or 1 (see above).
  - Each `?` input will be stored for later use.
- `<`: Pointer. This shows where the code starts on each stack.

Added commands:

- `-`: Break between stacks.
- - `i`: Uses previous inputs.
  - If there are less `i` 'prompts' than inputs stored, a new prompt will appear (the `i` will be treated as a `?`).
- `o`: Appends the output of the previous stack to current stack's output.
- `a`: `o` command, and converts the final binary number to decimal, then to ASCII.
- `r`: Removes stored inputs made by `?`.

`o`, `a` and `r` have to be in the first line of the applied stack to work.

To launch Pyramid code, you have to paste the code into file.pmd (you can edit .pmd files using something like Notepad).
You also need:
- Python (I'm fairly sure either version is fine)
- `colorama` (do `pip install colorama` on Windows or `python -m pip install colorama` on Bash).

TODO:
- Make custom file names a "thing"
