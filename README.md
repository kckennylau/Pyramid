# Pyramid
Pyramid: An stack-based esoteric language.

In Pyramid, there are eight commands:

- `0`: Move the pointer up one place in the stack.
- `1`: Move the pointer down one place in the stack.
- `?`: Input (only 0 or 1 allowed). The input is then used as a 0 or 1 (see above).
- `<`: Pointer. This shows where the code starts on each stack.
- `-`: Break between stacks.
- `o`: Appends the output of the previous stack to current stack's output.
- `i`: Uses previous inputs.
- `a`: `o` command, and converts the final binary number to decimal, then to ASCII.
