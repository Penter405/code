class Solution:
    @staticmethod
    def validPartition(self, nums: list[int]) -> bool:
        """legal subarray: 
        2 both same , 
        3 both same , 
        3 increasing(at most different 1)

        
        """
        
        """
        i am legal [index] =any(
        take until me is legal[index-1] is True and array range(index-1 to index) their value is same
        take until me is legal[index-2] is True and array range(index-2 to index) their value is same
        take until me is legal[index-2] is True and array range(index-2 to index) their value is increasing with different exactly just one
        )
        """
        legal=[False]*len(nums)#take_me_is_legal, im contained in a subarray

        for rs in range(len(nums)):
            if rs-1>=0:
                if rs-1==0 or legal[rs-2]:
                    if nums[rs-1]==nums[rs]:
                        legal[rs]=True
                        continue
            
            if rs-2>=0:
                if rs-2==0 or legal[rs-3]:
                    if nums[rs-2:rs+1].count(nums[rs-2])==3:
                        legal[rs]=True
                        continue
            
            if rs-2>=0:
                if rs-2==0 or legal[rs-3]:
                    last=None
                    bad=False
                    for iterator in nums[rs-2:rs+1]:
                        if last==None or last+1==iterator:
                            pass#i am good
                        else:
                            bad=True
                            break
                        last=iterator
                    if bad:
                        continue
                    legal[rs]=True
                    


        return legal[-1]

nums=[4,4,4,5,6]
print(Solution.validPartition(None,nums))