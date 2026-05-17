# https://leetcode.com/problems/combination-sum-ii/


class Solution:
    """40. Combination Sum II

    Given a collection of candidate numbers (`candidates`) and a target number
    (`target`), find all unique combinations in `candidates` where the candidate numbers
    sum to `target`.

    Each number in `candidates` may only be used **once** in the combination.

    **Note:** The solution set must not contain duplicate combinations.

    """

    def combination_sum2(self, candidates: list[int], target: int) -> list[list[int]]:
        def backtrack(start, target, path):
            # If the target is zero, we've found a valid combination
            if target == 0:
                result.append(path[:])
                return

            # Iterate through the candidates starting from 'start'
            for i in range(start, len(candidates)):
                # Skip duplicates
                if i > start and candidates[i] == candidates[i - 1]:
                    continue

                # If the current candidate exceeds the target, no need to proceed further
                if candidates[i] > target:
                    break

                # Include the current candidate and move forward
                path.append(candidates[i])

                # Recur with updated target and starting index
                backtrack(i + 1, target - candidates[i], path)

                # Backtrack, remove the last added element
                path.pop()

        # Sort the candidates to handle duplicates easily
        candidates.sort()

        result = []
        backtrack(0, target, [])
        return result

    combinationSum2 = combination_sum2
