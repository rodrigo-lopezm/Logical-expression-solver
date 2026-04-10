# Boolean truth table evaluator
A robust command-line based tool in order to solve simple boolean equations and returning formatted truth tables, made as a practice project

## Current progress: Simple equation solving
Currently, simple boolean expressions can be evaluated and the results formatted into a table, all terminal based.

### Features (Up to now):
- **Syntax validation**: Detects and rejects any invalid operator groupings (e.g. as `&&`, `&+`, `!&`, etc.), consecutive variables (e.g. `AB`) and dangling operators
- **Parentheses tracking**: Uses a depth counter to ensure all parentheses are balanced.
- **Unary and binary operator logic**: Differentiates the rules for the `!` (NOT) operator versus `&` (AND) and `+` (OR), allowing syntax such as `A & B` or `!!A`.
- **Automatic variable extraction**: Identifies variables on first pass, with a built-in limit of *6 variables*, preventing terminal clutter ($2^6 = 64$ rows).
- **Constant support**: Accepts the use of `0` and `1` as operands.
- **Tokenization**: Converts the raw, parsed boolean expression into an iterable list of logical tokens.
- **Replacement engine**: Replaces the boolean variables in the tokens list to their corresponding set of values, following the correct precedence order (Parentheses `()` -> NOT `!` ->  AND `&`-> XOR `^` -> OR `+`).
-  **Terminal UI**: Simple formatted truth table output and input/validation of expressions.

## Roadmap:
- [] **Sum of products formatting**: After the truth table is generated, the user will be asked if they want the sum of products equivalnce to the expression.
- [**DONE**] **Logic gate operators**: Allow for XOR operators.
- [**IN PROGRESS**] **Conditional and biconditional**: Allow for conditional and biconditional operators.
- [] **More complex simplification**: Simplify more complex equations for faster solving and for user's sake.
- [] **K-Map generation**: Generate a K-Map and draw appropiate loops around correct groups (allows for simplified sum of products).
- [] **Non-terminal interface**: Change the interface to a executable program window with its own UI rather than the terminal.
- [] **Ask for exporting of table**: Ask the user if they want the truth table to be exported into a text file.

## Syntax:
- AND: &
- OR: +
- NOT: !
- XOR: ^
- CONDITIONAL: >
- BICONDITIONAL: =
- TRUE: 1
- FALSE: 0

- Boolean variables: Uppercase letters
> Limit of 6 boolean variables.

## Usage:
On running the tablesolver.py script, you'll be met with an expression input. Once an expression with the correct formatting has been entered, the rest of the program will be executed.