class Solution:
    def out(self,a,b):
            if(a==b):
                return str(a)
            return f"{a}->{b}"
    def summaryRanges(self, nums: List[int]) -> List[str]:
        result=list()
        buffer_front=None
        buffer_back=None
        status=0
        for i in range(0,len(nums)):
            #print(buffer_front,buffer_back)
            if (buffer_front==None and buffer_back==None):
                buffer_front=nums[0]
                buffer_back=nums[0]
            else:
                if status==0:
                    #print("hihi",buffer_back+1,nums[i])
                    if buffer_back+1==nums[i]:
                        buffer_back=nums[i]
                    else:
                        #print("bad",buffer_front,buffer_back)
                        result.append(self.out(buffer_front,buffer_back))
                        buffer_front=nums[i]
                        buffer_back=nums[i]
            if i+1==len(nums):
                result.append(self.out(buffer_front,buffer_back))
        return result
                
