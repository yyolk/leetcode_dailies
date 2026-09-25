def test_brace_expansion_ii_examples(solution):
    # Example 1
    assert solution.braceExpansionII("{a,b}{c,{d,e}}") == [
        "ac",
        "ad",
        "ae",
        "bc",
        "bd",
        "be",
    ]

    # Example 2
    assert solution.braceExpansionII("{{a,z},a{b,c},{ab,z}}") == ["a", "ab", "ac", "z"]


def test_brace_expansion_ii_grammar_examples(solution):
    # Values taken from the problem statement grammar examples.
    assert solution.braceExpansionII("{a,b,c}") == ["a", "b", "c"]
    assert solution.braceExpansionII("{{a,b},{b,c}}") == ["a", "b", "c"]
    assert solution.braceExpansionII("{a,b}{c,d}") == ["ac", "ad", "bc", "bd"]
    assert solution.braceExpansionII("a{b,c}{d,e}f{g,h}") == [
        "abdfg",
        "abdfh",
        "abefg",
        "abefh",
        "acdfg",
        "acdfh",
        "acefg",
        "acefh",
    ]


def test_brace_expansion_ii_single_letter(solution):
    assert solution.braceExpansionII("a") == ["a"]
