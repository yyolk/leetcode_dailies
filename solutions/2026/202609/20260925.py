# https://leetcode.com/problems/brace-expansion-ii/


class Solution:
    """1096. Brace Expansion II

    Under the grammar given below, strings can represent a set of lowercase words. Let
    `R(expr)` denote the set of words the expression represents.

    The grammar can best be understood through simple examples:

    * Single letters represent a singleton set containing that word.

      + `R("a") = {"a"}`

      + `R("w") = {"w"}`

    * When we take a comma-delimited list of two or more expressions, we take the union
    of possibilities.

      + `R("{a,b,c}") = {"a","b","c"}`

      + `R("{{a,b},{b,c}}") = {"a","b","c"}` (notice the final set only contains each
    word at most once)

    * When we concatenate two expressions, we take the set of possible concatenations
    between two words where the first word comes from the first expression and the
    second word comes from the second expression.

      + `R("{a,b}{c,d}") = {"ac","ad","bc","bd"}`

      + `R("a{b,c}{d,e}f{g,h}") = {"abdfg", "abdfh", "abefg", "abefh", "acdfg", "acdfh",
    "acefg", "acefh"}`

    Formally, the three rules for our grammar:

    * For every lowercase letter `x`, we have `R(x) = {x}`.

    * For expressions `e1, e2, ... , ek` with `k >= 2`, we have `R({e1, e2, ...}) =
    R(e1) ∪ R(e2) ∪ ...`

    * For expressions `e1` and `e2`, we have `R(e1 + e2) = {a + b for (a, b) in R(e1) ×
    R(e2)}`, where `+` denotes concatenation, and `×` denotes the cartesian product.

    Given an expression representing a set of words under the given grammar, return *the
    sorted list of words that the expression represents*.

    Constraints:

    * `1 <= expression.length <= 60`

    * `expression[i]` consists of `'{'`, `'}'`, `','`or lowercase English letters.

    * The given `expression` represents a set of words based on the grammar given in the
    description.
    """

    def brace_expansion_i_i(self, expression: str) -> list[str]:
        """Parse the brace-expansion grammar and return sorted unique words."""
        n = len(expression)
        i = 0

        def union_inside_braces() -> set[str]:
            """Parse comma-separated alternatives after consuming '{'."""
            nonlocal i
            words: set[str] = set()
            words |= parse_expr()
            while i < n and expression[i] == ",":
                i += 1
                words |= parse_expr()
            # consume matching '}'
            i += 1
            return words

        def parse_unit() -> set[str]:
            """Parse a letter or a `{...}` group."""
            nonlocal i
            if expression[i] == "{":
                i += 1
                return union_inside_braces()
            letter = expression[i]
            i += 1
            return {letter}

        def parse_expr() -> set[str]:
            """Parse a concatenation of units until ',' or '}' or end."""
            nonlocal i
            # empty product is {""} so the first unit can stand alone
            result = {""}
            while i < n and expression[i] not in ",}":
                unit = parse_unit()
                result = {prefix + suffix for prefix in result for suffix in unit}
            return result

        return sorted(parse_expr())

    braceExpansionII = brace_expansion_i_i
