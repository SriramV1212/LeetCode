class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = set()  # Create an empty set to store unique elements
        for num in nums:
           if num in seen:  # If the number is already in the set, return True
              return True
           seen.add(num)  # Add the number to the set if not already present
        return False
        