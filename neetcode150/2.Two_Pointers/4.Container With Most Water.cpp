class Solution {
private:
    int min(int a,int b){
        if(a>b){
            return b;
        }
        return a;
    }
    int max(int a,int b){
        if(a>b){
            return a;
        }
        return b;
    }
public:
    int maxArea(vector<int>& heights) {
        /*
        for front back pointers solution, as the width get less, we need to let low one side get up until they
        more than the other pointer value
        */
        //int result;
        int size_width=heights.size()-1;
        int front=0;
        int back=heights.size()-1;
        int result=min(heights[front],heights[back])*size_width;
        while(front!=back && size_width!=0){
            result=max(result,min(heights[front],heights[back])*size_width);
            if(heights[front]>heights[back]){
                back-=1;
            }
            else{
                front+=1;
            }
            size_width-=1;
        }
        return result;
    }
};
