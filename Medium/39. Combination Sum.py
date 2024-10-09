import math


class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        candidates.sort()
        candidates = [i for i in candidates if i <= target]
        if not candidates:
            return []
        curr_attempt = [candidates[0]]*math.ceil(target/candidates[0])
        curr_candidate_index = 0
        curr_candidate = candidates[curr_candidate_index]
        result = []
        while curr_candidate_index < len(candidates):
            curr_sum = sum(curr_attempt)
            if curr_sum >= target and curr_attempt[0] == curr_candidate:
                curr_candidate_index += 1
                if curr_candidate_index < len(candidates):
                    curr_candidate = candidates[curr_candidate_index]
            if curr_sum > target:
                curr_attempt.pop(0)
            elif curr_sum < target:
                curr_attempt.append(curr_candidate)
            else:
                result.append(curr_attempt.copy())
                curr_attempt.pop(0)
        return result

s  = Solution()
A = s.combinationSum([2,3,5,8], 10)
print(A)
