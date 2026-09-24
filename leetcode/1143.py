from collections import defaultdict,deque
"""
find out equation
my_max=me+a friend + friend's max

"""
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        def update_postfix(index):
            now_largest_dp=0
            for rs in range(index,len(dp)):
                now_largest_dp=max(now_largest_dp,dp[index])
                postfix_dp[rs]=now_largest_dp

        def update_postfix1(index,value):
            now_largest_dp=value
            for rs in range(index,len(dp)):
                now_largest_dp=max(now_largest_dp,dp[index])
                postfix_dp1[rs]=now_largest_dp
        def update_postfix2(index,value):
            now_largest_dp=value
            for rs in range(index,len(dp)):
                now_largest_dp=max(now_largest_dp,dp[index])
                postfix_dp2[rs]=now_largest_dp
        size1=len(text1)
        size2=len(text2)
        if size1<size2:
            text1=text1+"1"*(size2-size1)
        elif size1>size2:
                    text2=text2+"1"*(size1-size2)
        """
        what are necceary to find common subsequence? which is ordered


        we can use two pointer to a text
        dp[i]=biggest common of must pick up me(or not) 
        but we have two text
        """
        dp=[0]*max(len(text1),len(text2))
        postfix_dp=[0]*max(len(text1),len(text2))
        postfix_dp1=[0]*max(len(text1),len(text2))
        postfix_dp2=[0]*max(len(text1),len(text2))
        untaked1=defaultdict(deque)
        untaked2=defaultdict(deque)#guy:list of index
        #text1="pmjghexybyrgzczy"
        #           4   8 0  3
        #text2="hafcdqbgncrcbihkd"
        #       0     6   01
        #4
        pointer1=0
        pointer2=0
        while True:
            if not(0<=pointer1<=len(text1)-1 and 0<=pointer2<=len(text2)-1):
                return max(dp)
            did1=False
            did2=False
            if len(untaked2[text1[pointer1]])!=0:
                the_other_index=untaked2[text1[pointer1]].popleft()
                dp[pointer1]=max(dp[pointer1],postfix_dp2[the_other_index-1]+1)
                update_postfix2(the_other_index,dp[pointer1])#text2 落後
                update_postfix1(pointer1,dp[pointer1])

                pointer1+=1
                did1=True
            
            #------------- the other pointer
            if len(untaked1[text2[pointer2]])!=0:
                the_other_index=untaked1[text2[pointer2]].popleft()
                dp[pointer2]=max(dp[pointer2],postfix_dp1[the_other_index]+1)
                update_postfix1(the_other_index,dp[pointer2])
                update_postfix2(pointer2,dp[pointer2])
                pointer2+=1
                did2=True




            if did1==False and did2==False and text1[pointer1]==text2[pointer2]:
                big=max(pointer1,pointer2)
                small=min(pointer1,pointer2)
                if small==0:
                    dp[0]+=1
                    for rs in range(0,len(dp)):
                        if postfix_dp1[rs]!=0 or postfix_dp2[rs]!=0:
                            print("error")
                        postfix_dp1[rs]=1
                        postfix_dp2[rs]=1
                else:
                    if pointer2>pointer1:
                        dp[big]=max(dp[big],postfix_dp1[small-1]+1)
                    else:
                        dp[big]=max(dp[big],postfix_dp2[small-1]+1)
                    update_postfix2(small,dp[big])
                    update_postfix1(small,dp[big])
                    #update_postfix(pointer1)
                pointer1+=1
                pointer2+=1
                continue
            else:
                if did1==False:
                    untaked1[text1[pointer1]].append(pointer1)
                    pointer1+=1

                if did2==False:
                    untaked2[text2[pointer2]].append(pointer2)
                    pointer2+=1

        return max(postfix_dp)

text1="pmjghexybyrgzczy"
text2="hafcdqbgncrcbihkd"
print(Solution.longestCommonSubsequence(None,text1,text2))