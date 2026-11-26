class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = fast = second = 0

        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]

            if slow == fast:
                second = slow
                break

        first = 0

        while True:
            if first == second:
                return first

            first = nums[first]
            second = nums[second]
            

