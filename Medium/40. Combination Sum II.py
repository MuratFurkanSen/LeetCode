class Solution:
    count = 0

    def combinationSum2(self, candidates: list[int], target: int) -> list[list[int]]:
        result = []
        candidates.sort()
        no_candidates = len(candidates)

        def solve(index, cur, total):
            if total == target:
                result.append(cur.copy())
                return
            if index >= no_candidates or total > target:
                return

            # Left Child
            cur.append(candidates[index])
            solve(index+1, cur, total + candidates[index])
            # Right Child
            counter = 0
            while counter + index < no_candidates and candidates[counter+index] == candidates[index]:
                counter += 1
            cur.pop()
            solve(index + counter, cur, total)

        solve(0, [], 0)
        return result
