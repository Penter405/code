class Solution:
    def search(self, nums: list[int], target: int) -> int:
        place=dict()
        for rs in range(len(nums)):
            place[nums[rs]]=rs
        return place.get(target,-1)
