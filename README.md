# Pyramid
Pyramid: An stack-based esoteric language.

~~Built on top on~~ Heavily inspired by [Stackylogic](http://codegolf.stackexchange.com/questions/84851/run-stackylogic).

In Pyramid, there are nine commands:

- `0`: Move the pointer up one place in the stack.
- `1`: Move the pointer down one place in the stack.
- `?`: Input (only 0 or 1 allowed). The input is then used as a 0 or 1 (see above).
  - Each `?` input will be stored for later use.
- `<`: Pointer. This shows where the code starts on each stack.
- `-`: Break between stacks.
- `o`: Appends the output of the previous stack to current stack's output.
- `i`: Uses previous inputs.
  - If there are less "i" 'prompts' than inputs stored, a new prompt will appear (the `i` will be treated as a `?`).
- `a`: `o` command, and converts the final binary number to decimal, then to ASCII.
- `r`: Removes stored inputs made by `?`.
