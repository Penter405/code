class Solution:
    @staticmethod
    def findTargetSumWays(nums: list[int], target: int) -> int:
        #plus or take off
        achive_here={0:1}

        for guy in nums:
            to_add={}
            walk=list(achive_here.keys()).copy()
            for place in walk:

                to_add[place+guy]=to_add.get(place+guy,0)+achive_here[place]
                to_add[place-guy]=to_add.get(place-guy,0)+achive_here[place]
            
            achive_here=to_add.copy()

        return to_add.get(target,0)
nums=[7,4,3,8,1]
target=7
print(Solution.findTargetSumWays(nums,target))