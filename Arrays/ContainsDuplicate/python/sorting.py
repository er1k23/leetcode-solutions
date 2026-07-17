from typing import *


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]:
                return True
        return False

def main() -> None:
    solution = Solution()

    assert solution.containsDuplicate([1,2,3,4,4]) == True
    assert solution.containsDuplicate([1,2,3,4]) == False

    print("✅ All tests passed")


if __name__ == "__main__":
    main()