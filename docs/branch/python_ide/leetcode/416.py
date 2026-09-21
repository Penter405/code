class Solution:
    def canPartition(self, nums: list[int]) -> bool:
        if sum(nums)%2!=0:
            return False
        can_arrive_here=[0]*(sum(nums)//2+1)
        can_arrive_here[0]=1
        
        for guy in sorted(nums):
            to_add=[]
            for place in range(len(can_arrive_here)):
                if can_arrive_here[place]!=1:
                    continue
                
                if guy+place>len(can_arrive_here)-1:
                    continue
                to_add.append(guy+place)
            for need in to_add:
                can_arrive_here[need]=1
            #print("hi")
            #print(can_arrive_here)
            if can_arrive_here[-1]==1:
                return True
            
        return bool(can_arrive_here[-1])