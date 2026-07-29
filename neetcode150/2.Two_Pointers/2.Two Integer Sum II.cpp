class Solution {
public:
    vector<int> twoSum(vector<int>& numbers, int target) {
        std::vector<int> result;
        int front_index=0;
        int back_index=numbers.size()-1;
        //std::cout<<numbers[0];
        //std::cout<<numbers[front_index];
        while(true){
            //std::cout<<front_index<<" is "<<numbers[front_index]<<' '<<back_index<<" is "<<numbers[back_index]<<'\n';
            if(back_index<=front_index){
                return result;
            }
            if(numbers[front_index]!=numbers[back_index] && numbers[front_index]+numbers[back_index]==target){
                result.push_back(front_index+1);
                result.push_back(back_index+1);
                return result;
            }
            if(numbers[front_index]+numbers[back_index]>target){
                back_index-=1;
            }else if(numbers[front_index]+numbers[back_index]<target){
                front_index+=1;
            }
        }
        return result;
    }
};
