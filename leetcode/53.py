class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        """
        my max option= if i positive -> choose me , else can choose me
        the easyest option is o(n**2) and get their sum
        for every node these things will happen:
            take myself with privious
            only take myself
        """

        dp=[]
        for rs in nums:
            if len(dp)==0:
                dp.append(rs)
            else:
                dp.append(max(rs,rs+dp[-1]))
        return max(dp)
