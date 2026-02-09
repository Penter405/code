#include <vector>
class Solution {
public:
    std::vector<int> twoSum(std::vector<int>& numbers, int target) {
        int front=0,back=numbers.size()-1;
        std::vector<int> result;
        while(numbers[front]+numbers[back]!=target){
            //std::cout<<front<<"  "<<back<<"\n";
            if(numbers[front]+numbers[back]>target){
                --back;
            }else{
                ++front;
            }
        }
        result.push_back(front+1);
        result.push_back(back+1);
        return result;
    }
};