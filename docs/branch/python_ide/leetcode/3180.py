class Solution:
    def maxTotalReward(self, rewardValues: list[int]) -> int:
        """
        total reward=0
        marked=[0]*len(rewardValues)
        if (item value with unmark> now total reward){
            can plus
            marked[item]=1
        }
        pick me =(every smaller than me item sum)

        legal!=best
        best!=first chose is smallest
        """
        member = sorted(rewardValues)

        leave = set()
        result=0
        for guy in member:
            leave2=set()
            for child in leave:
                if guy<=child:
                    continue
                if guy + child >result:
                    result= guy + child


                leave2.add(guy + child)

            if guy >result:
                result=guy
            leave.add(guy)
            leave.update(leave2)




        return result

penter=Solution()
rewardValues = [1,6,4,3,2]
print(penter.maxTotalReward(rewardValues))