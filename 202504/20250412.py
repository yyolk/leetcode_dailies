# https://leetcode.com/problems/find-the-count-of-good-integers/


class Solution:
    """3272. Find the Count of Good Integers

    You are given two **positive** integers `n` and `k`.

    An integer `x` is called **k-palindromic** if:

    * `x` is a palindrome.

    * `x` is divisible by `k`.

    An integer is called **good** if its digits can be *rearranged* to form a
    **k-palindromic** integer. For example, for `k = 2`, 2020 can be rearranged to form
    the *k-palindromic* integer 2002, whereas 1010 cannot be rearranged to form a
    *k-palindromic* integer.

    Return the count of **good** integers containing `n` digits.

    **Note** that *any* integer must **not** have leading zeros, **neither** before
    **nor** after rearrangement. For example, 1010 *cannot* be rearranged to form 101.
    """

    def count_good_integers(self, n: int, k: int) -> int:
        # Handle n = 1 separately: count single digits from 1 to 9 divisible by k
        if n == 1:
            return sum(1 for d in range(1, 10) if d % k == 0)

        # Precompute factorials up to 10 for multinomial coefficients
        fact = [1]
        for i in range(1, 11):
            fact.append(fact[-1] * i)

        # Function to check if a frequency vector has at least one valid palindrome
        def has_valid_palindrome(freq: List[int]) -> bool:
            # Determine the number of digits to generate (first half + middle if odd)
            m = n // 2  # Length of first half
            if n % 2 == 0:
                target_freq = [f // 2 for f in freq]
            else:
                odd_digits = [d for d in range(10) if freq[d] % 2 == 1]
                c = odd_digits[0]  # Digit with odd frequency (middle digit)
                target_freq = [
                    f // 2 if d != c else (f - 1) // 2 for d, f in enumerate(freq)
                ]

            # Recursive function to build palindrome and check conditions
            def recurse(
                pos: int, curr_freq: List[int], curr_sum: int, first_digit: int
            ) -> bool:
                if pos == m:
                    # Check if first digit is not zero and number is divisible by k
                    return first_digit != 0 and curr_sum % k == 0
                for d in range(10):
                    if curr_freq[d] > 0:
                        new_freq = curr_freq.copy()
                        new_freq[d] -= 1
                        # Contribution of digit d at positions pos and n-1-pos
                        contrib = d * (pow(10, pos, k) + pow(10, n - 1 - pos, k)) % k
                        new_sum = (curr_sum + contrib) % k
                        new_first = d if pos == 0 else first_digit
                        if recurse(pos + 1, new_freq, new_sum, new_first):
                            return True
                return False

            # Add middle digit contribution for odd n
            start_sum = (c * pow(10, m, k)) % k if n % 2 == 1 else 0
            return recurse(0, target_freq, start_sum, -1)

        # Generate frequency vectors with all even frequencies (n even)
        def generate_even_freq(pos: int, remaining: int, freq: List[int]):
            if pos == 10:
                if remaining == 0:
                    yield freq[:]
                return
            for f in range(0, remaining + 1, 2):
                freq[pos] = f
                yield from generate_even_freq(pos + 1, remaining - f, freq)

        # Generate frequency vectors with exactly one odd frequency (n odd)
        def generate_odd_freq(c: int, pos: int, remaining: int, freq: List[int]):
            if pos == 10:
                if remaining == 0:
                    yield freq[:]
                return
            if pos == c:
                for f in range(1, remaining + 1, 2):  # Odd frequencies
                    freq[pos] = f
                    yield from generate_odd_freq(c, pos + 1, remaining - f, freq)
            else:
                for f in range(0, remaining + 1, 2):  # Even frequencies
                    freq[pos] = f
                    yield from generate_odd_freq(c, pos + 1, remaining - f, freq)

        total = 0

        # Compute number of permutations without leading zeros
        def count_permutations(freq: List[int]) -> int:
            prod_den = 1
            for f in freq:
                prod_den *= fact[f]
            total_perms = fact[n] // prod_den
            if freq[0] == 0:
                return total_perms
            prod_den_zero = fact[freq[0] - 1]
            for d in range(1, 10):
                prod_den_zero *= fact[freq[d]]
            with_leading_zero = fact[n - 1] // prod_den_zero
            return total_perms - with_leading_zero

        # Process based on n being even or odd
        if n % 2 == 0:
            for freq in generate_even_freq(0, n, [0] * 10):
                if has_valid_palindrome(freq):
                    total += count_permutations(freq)
        else:
            for c in range(10):
                for freq in generate_odd_freq(c, 0, n, [0] * 10):
                    if has_valid_palindrome(freq):
                        total += count_permutations(freq)

        return total

    countGoodIntegers = count_good_integers
