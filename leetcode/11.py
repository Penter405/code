#not working version
class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        """
        print(a)  -> <list_iterator object at 0x7f1006f3c5e0>
        and neext(a) cant go to next element
        """

        #short guy be change. and then get. the x must small, if we move high guy, Y axis wont more , but x less. 
        big=-1
        #front=iter(height)
        #back=reversed(height)
        #f = next(front)
        #b=next(back)
        fi=0
        bi=len(height)-1
        #print(f"{f}/{b}")
        #loop :cheak big  move , and while syntax cheak if it legel 
        #i give up, iterator is not good in ramdom access data type
        while bi>fi:
            print(f"{fi}/{bi}")
            
            now=(bi-fi)*min(height[fi],height[bi])
            if now>big:
                big=now
            if (bi-fi)==1:
                return big
            print(f"now is {now}/big is {big}")
            tall=0
            va=-1
            ind=fi
            print(f"getting from {height[fi+1:bi]}")
            for i in height[fi+1:bi]:
                ind+=1
                print(f"index {ind}")
                if i>va:
                    print("got you")
                    va=i
                    tall=ind
            print("cheak who next")
            print(f"tall {tall}/va {va}")
            if tall<fi and tall<bi:
                return big
            if height[fi]<height[bi]:
                fi=tall
            elif height[fi]>height[bi]:
                bi=tall
            else:
                if (tall-fi)<(bi-tall):
                    fi=tall
                elif (tall-fi)>(bi-tall):
                    bi=tall
                else:
                    bi=tall
                    #in this situation, we only care if now bigger. no next;
                #when they equal
            

        return 0
"""
in version 1:
height=[1,2,4,3]

and stdred out:
0/3
now is 3/big is 3
getting from [2, 4]
index 1
got you
index 2
got you
cheak who next
tall 2/va 4
2/3

we miss some possible answer by going to the tallest only.
thats why fail.

and then if both same tall, like row 54, no matter what pointer be moved, the x axis always less, and min(p1,p2) same value. so we can possibly move both pointer to next seat.
"""

#version two below
class Solution:
    def maxArea(self, height: List[int]) -> int:
        front=0
        back=len(height)-1
        big=-1
        while True:
            if back==front:
                return big
            now=(back-front)*min(height[front],height[back])
            if now>big:
                big=now
            if height[front]>height[back]:
                back-=1
            else:
                front+=1
#version 3, different version 2 from (if else) become  (if elif else)
class Solution:
    def maxArea(self, height: List[int]) -> int:
        front=0
        back=len(height)-1
        big=-1
        while True:
            if back<=front:
                return big
            now=(back-front)*min(height[front],height[back])
            if now>big:
                big=now
            if height[front]>height[back]:
                back-=1
            elif height[front]<height[back]:
                front+=1
            else:
                front+=1
                back-=1
#version 4. in version 2 and 3, we dont ramdom access, we can use iterator
class Solution:
    def maxArea(self, height: List[int]) -> int:
        front=iter(height)
        back=reversed(height)
        big=-1
        f=next(front)
        b=next(back)
        size=len(height)-1
        while True:
            if size<1:
                return big
            now=(size)*min(f,b)
            if now>big:
                big=now
            if f>b:
                b=next(back)
                size-=1
            elif f<b:
                f=next(front)
                size-=1
            else:
                f=next(front)
                b=next(back)
                size-=2