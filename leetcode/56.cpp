class Solution {
private:
    /*array<int,3> binary_search(vector<vector<int>> intervals, int srart, int end){
        array<int,3> result;//index1 index2 is_replace;
        return result;
    }
    void save_data(vector<vector<int>>& it, int index1, int index2,int is_replace, vector<int> ob){
        int a;
    }*/
    int max(int a,int b){
        if(a>=b){
            return a;
        }
        return b;
    }
public:
    vector<vector<int>> merge(vector<vector<int>>& intervals) {
        vector<vector<int>> result;
        //sort
        int now_index=-1;
        int min_pre=-1;
        int min_index=-1;
        for(int bot=0;bot<intervals.size();++bot){
            min_pre=-1;
            for(int i=0;i<intervals.size();++i){
                if(intervals[i][0]==-1){
                    continue;
                }
                if(min_pre==-1||intervals[i][0]<min_pre){
                    min_pre=intervals[i][0];
                    min_index=i;
                }
            }
            //std::cout<<"seeing "<<intervals[min_index][0]<<"  "<<intervals[min_index][1]<<'\n';
            if(now_index==-1){
                //std::cout<<"quick\n";
                result.push_back(intervals[min_index]);
                now_index+=1;
            }else{
                //right here, result one is inside, intervals is new guy
                if(result[now_index][0]<=intervals[min_index][0] && result[now_index][1]>=intervals[min_index][0]){
                    //std::cout<<"cheak, meage\n";
                    result[now_index][1]=max(result[now_index][1],intervals[min_index][1]);
                }else{
                    //std::cout<<"cheak, push back\n";
                    result.push_back(intervals[min_index]);
                    now_index+=1;
                }
            }
            intervals[min_index][0]=-1;
        }
        return result;
    }
};