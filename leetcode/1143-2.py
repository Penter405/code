from collections import defaultdict,deque
"""
find out equation
my_max=me+ a before me's max

"""
#text1="pmjghexybyrgzczy"
#           4   8 0  3
#text2="hafcdqbgncrcbihkd"
#       0     6   01
#4
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        def update_postfix(kindex:int, value):
            #index is included
            for index in range(kindex,len(text1)):
                prefix_dp[index]=max(prefix_dp[index],value)

        dp=[0 for _ in range(len(text1))]# letter:letter's max
        size1=len(text1)
        size2=len(text2)
        if size1<size2:
            text1=text1+"1"*(size2-size1)
        elif size1>size2:
            text2=text2+"1"*(size1-size2)
        place_of_2=defaultdict(list)
        prefix_dp=[0]*len(text1)
        for index in range(len(text2)):
            place_of_2[text2[index]].append(index)
        for index in range(len(text1)):
            new_here=0
            for matched_index_of_2 in place_of_2[text1[index]]:
                print(text1[index],"match 2 in index",matched_index_of_2)
                new_here=max(new_here,prefix_dp[matched_index_of_2]+1)
                update_postfix(matched_index_of_2,new_here)
        return max(prefix_dp)
                


        return 0
text1="pmjghexybyrgzczy"
text2="hafcdqbgncrcbihkd"
print(Solution.longestCommonSubsequence(None,text1,text2))