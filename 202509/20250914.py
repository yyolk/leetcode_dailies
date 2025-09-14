# https://leetcode.com/problems/vowel-spellchecker/


class Solution:
    """966. Vowel Spellchecker

    Given a `wordlist`, we want to implement a spellchecker that converts a query word
    into a correct word.

    For a given `query` word, the spell checker handles two categories of spelling
    mistakes:

    * Capitalization: If the query matches a word in the wordlist (**case-
    insensitive**), then the query word is returned with the same case as the case in
    the wordlist.

      + Example: `wordlist = ["yellow"]`, `query = "YellOw"`: `correct = "yellow"`

      + Example: `wordlist = ["Yellow"]`, `query = "yellow"`: `correct = "Yellow"`

      + Example: `wordlist = ["yellow"]`, `query = "yellow"`: `correct = "yellow"`

    * Vowel Errors: If after replacing the vowels `("a", "e", "i", "o", "u")` of the
    query word with any vowel individually, it matches a word in the wordlist (**case-
    insensitive**), then the query word is returned with the same case as the match in
    the wordlist.

      + Example: `wordlist = ["YellOw"]`, `query = "yollow"`: `correct = "YellOw"`

      + Example: `wordlist = ["YellOw"]`, `query = "yeellow"`: `correct = ""` (no match)

      + Example: `wordlist = ["YellOw"]`, `query = "yllw"`: `correct = ""` (no match)

    In addition, the spell checker operates under the following precedence rules:

    * When the query exactly matches a word in the wordlist (**case-sensitive**), you
    should return the same word back.

    * When the query matches a word up to capitlization, you should return the first
    such match in the wordlist.

    * When the query matches a word up to vowel errors, you should return the first such
    match in the wordlist.

    * If the query has no matches in the wordlist, you should return the empty string.

    Given some `queries`, return a list of words `answer`, where `answer[i]` is the
    correct word for `query = queries[i]`."""

    def spellchecker(self, wordlist: list[str], queries: list[str]) -> list[str]:
        # Set for exact case-sensitive matches
        exact = set(wordlist)
        # Dict for case-insensitive matches, mapping lowercase to first original word
        cap = {}
        # Dict for vowel-error matches, mapping consonant skeleton to first original word
        vowel = {}
        # Set of lowercase vowels for replacement checks
        vows = set("aeiou")

        # Preprocess wordlist
        for word in wordlist:
            wlow = word.lower()
            # Map lowercase to first occurrence for capitalization
            if wlow not in cap:
                cap[wlow] = word
            # Compute skeleton: replace vowels with "*" to match consonant positions
            skel = "".join(c if c not in vows else "*" for c in wlow)
            # Map skeleton to first occurrence for vowel errors
            if skel not in vowel:
                vowel[skel] = word

        result = []
        for query in queries:
            # Check exact match first (case-sensitive)
            if query in exact:
                result.append(query)
                continue
            # Lowercase query for next checks
            qlow = query.lower()
            # Check capitalization match
            if qlow in cap:
                result.append(cap[qlow])
                continue
            # Compute query skeleton for vowel errors
            qskel = "".join(c if c not in vows else "*" for c in qlow)
            # Check vowel error match
            if qskel in vowel:
                result.append(vowel[qskel])
            else:
                result.append("")
        return result

    spellchecker = spellchecker
