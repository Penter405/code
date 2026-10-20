class Solution:
    @staticmethod
    def countFairPairs(self, nums: list[int], lower: int, upper: int) -> int:
        nums.sort()
        st=[]
        end=[]
        for x in range(len(nums)):
            #we can binary search in these inner for loops (total=2)
            for y in range(len(nums)):
                if lower<=nums[y]+nums[x]:
                    st.append(y)
                    break
            end.append(-1)
            for y in range(len(nums)-1,-1,-1):
                if not(nums[y]+nums[x]>upper):
                    end[-1]=y
                    break
                
        res=0
        good=0
        for rs in range(len(st)):
            if end[rs]>=st[rs]:
                res+=end[rs]-st[rs]+1
            if rs>=st[rs]:
                good+=1
        return (res-good)//2+good


nums = [0,1,7,4,4,5]
lower = 3
upper = 6
print(Solution.countFairPairs(None,nums,lower,upper))