class Solution:
    @staticmethod
    def findDuplicate(nums: list[int]) -> int:
        bool_list = [False] * len(nums)
        dup = -1
        for i in nums:
            if bool_list[i]:
                dup = i
                break
            else:
                bool_list[i] = True
        return dup



if __name__ == '__main__':
    sol = Solution()
    print(sol.findDuplicate([1, 3, 4, 4, 2]))
