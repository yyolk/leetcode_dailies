# https://leetcode.com/problems/coupon-code-validator


class Solution:
    """3606. Coupon Code Validator

    You are given three arrays of length n that describe the properties of n
    coupons: code, business_line, and is_active. The ith coupon has:

    code[i]: a string representing the coupon identifier.
    business_line[i]: a string denoting the business category of the coupon.
    is_active[i]: a boolean indicating whether the coupon is currently active.
    A coupon is considered valid if all of the following conditions hold:

    code[i] is non-empty and consists only of alphanumeric characters (a-z, A-Z,
    0-9) and underscores (_).
    business_line[i] is one of the following four categories: "electronics",
    "grocery", "pharmacy", "restaurant".
    is_active[i] is true.
    Return an array of the codes of all valid coupons, sorted first by their
    business_line in the order: "electronics", "grocery", "pharmacy",
    "restaurant", and then by code in lexicographical (ascending) order within
    each category.
    """
    def validate_coupons(self, code: list[str], business_line: list[str], is_active: list[bool]) -> list[str]:
        # Define sort order for business lines
        order = {"electronics": 0, "grocery": 1, "pharmacy": 2, "restaurant": 3}
        valid_categories = set(order.keys())
        # Collect valid coupons as (sort_key, code) tuples
        valid = []
        for i in range(len(code)):
            c = code[i]
            bl = business_line[i]
            active = is_active[i]
            # Skip if not active
            if not active:
                continue
            # Skip if business line invalid
            if bl not in valid_categories:
                continue
            # Skip if code empty or contains invalid chars
            if not c or not all(ch.isalnum() or ch == '_' for ch in c):
                continue
            # Add tuple for sorting
            valid.append((order[bl], c))
        # Sort by sort_key then code lexicographically
        valid.sort(key=lambda x: (x[0], x[1]))
        # Extract codes
        return [c for _, c in valid]

    validateCoupons = validate_coupons