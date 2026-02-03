class Solution {
private:
    int lowest(std::vector me){
        int iter=0;result=0, size=me.size(),big=0;

        for(;iter<size;++iter){
            if(me[result]>big){
                result=iter
                big=me[result];
            }
        }
        return result;
    }
public:
    long long minimumCost(vector<int>& old_nums, int k, int dist) {
        std::std::forward_list<int> nums(old_nums.begin(), old_nums.end());
        int result=nums[0];

    }
};
//first element of subarray <=dist
//disjoint contiguous, if the element was taken by other sub array, it cant be take again.
//(first element of second sub array)-(first element of Kth sub array)<=dist=a-b
//first second third fourth fifth sixth seventh ...  Kth
//multiple trees question
//if find a better tree, use it.
//BFS searching
//return sum of first elements most min.
//question, is the source array sorted? no
//sub array is from index a to index b of source array.
//can i change order of sub array from source order?
//in any position, cant change order, all from source order.
//because of its count sum of first element of sub array , and all element are positive. we need most few sub string
//a can place after 0 index(1,2,3,4...last), b can be place after k-1

/*
two pointer,
0----second sub array------k array(zero sub array need after, we can know k sub array is the lastest sub array of source array)
*/


//if k is 5, we need k,first of source, and k-2 top less element
//{1,2,3,4,5|,6,7,1}
//find least of source array
//int size is 2* 10^10
//should i change vector nums to forward_list? i would remove element and i dont need random access.