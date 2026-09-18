#did not finish
class Solution:
    def maxTotalReward(self, rewardValues: List[int]) -> int:
        """
        total reward=0
        marked=[0]*len(rewardValues)
        if (item value with unmark> now total reward){
            can plus
            marked[item]=1
        }
        pick me =(every smaller than me item sum)

        """
