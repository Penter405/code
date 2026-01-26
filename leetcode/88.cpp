#include <iostream>
#include <vector>
class Solution {
public:
    void merge(std::vector<int>& nums1, int m, std::vector<int>& nums2, int n) {
        std::vector<int> result, nums3;
        
        //if the data of array both are sorted from small to big, we can use two pointer
        using std::cout;
        using std::cin;
        int pointer_1=0;
        int pointer_2=0;
        while(pointer_1<m || pointer_2<n){
            if(pointer_1>=m){
                nums3.push_back(nums2[pointer_2]);
                pointer_2++;
            }else if(pointer_2>=n){
                nums3.push_back(nums1[pointer_1]);
                pointer_1++;
            }else if(nums1[pointer_1]>nums2[pointer_2]){
                nums3.push_back(nums2[pointer_2]);
                pointer_2++;
            }else if(nums1[pointer_1]<nums2[pointer_2]){
                nums3.push_back(nums1[pointer_1]);
                pointer_1++;
            }else{
                nums3.push_back(nums1[pointer_1]);
                pointer_1++;
                nums3.push_back(nums2[pointer_2]);
                pointer_2++;
            }
        }
        nums1=nums3;
    }
};