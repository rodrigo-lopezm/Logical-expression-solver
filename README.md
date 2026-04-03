# Boolean truth table evaluator
A robust command-line based tool in order to solve simple boolean equations and returning formatted truth tables, made as a practice project

## Current progress: Single Pass Parser
Currently, a single pass parser has been implemented by which any equation is checked in a single loop to ensure the safety of the equation before any evaluation happens.

### Features (Up to now):
- **Syntax validation**: Detects and rejects any invalid operator groupings (e.g. as `&&`, `&+`, `!&`, etc.), consecutive variables (e.g. `AB`) and dangling operators
- **Parentheses tracking**: Uses a depth counter to ensure all parentheses are balanced.
- **Unary and binary operator logic**: Differentiates the rules for the `!` (NOT) operator versus `&` (AND) and `+` (OR), allowing syntax such as `A & B` or `!!A`.
- **Automatic variable extraction**: Identifies variables on first pass, with a built-in limit of *6 variables*, preventing terminal clutter ($2^6 = 64$ rows).
- **Constant support**: Accepts the use of `0` and `1` as operands.

## Roadmap:
- [] **Tokenization**: Converting the raw, parsed string into an iterable list of logical tokens.
- [] **Replacement engine**: Evaluating the logical expressions respecting standard presedence: Parentheses `()` -> NOT `!` ->  AND `&` -> OR `+`.
- [] **Terminal UI**: Rendering the final truth table with alphabetical letters and column formatting.
- [] **Sum of products formatting**: After the truth table is generated, the user will be asked if they want the sum of products equivalnce to the expression.

## Syntax:
- AND: &
- OR: +
- NOT: !
- TRUE: 1
- FALSE: 0

- Boolean variables: Uppercase letters
> Limit of 6 boolean variables.

## Usage:
*(Instructions on how to run the script will be added once the evaluation engine is complete).*