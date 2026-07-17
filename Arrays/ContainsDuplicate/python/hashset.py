from typing import *


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        s = set()
        for num in nums:
            if num in s:
                return True
            else:
                s.add(num)
        return False




def main() -> None:
    solution = Solution()

    assert solution.containsDuplicate([1,2,3,4,4]) == True
    assert solution.containsDuplicate([1,2,3,4]) == False

    print("✅ All tests passed")


if __name__ == "__main__":
    main()