class Solution {
public:
    vector<int> spiralOrder(vector<vector<int>>& matrix) {
        //std::cout<<3%2;
        int x=matrix[0].size(), y=matrix.size(),min_x=-1,min_y=-1;
        //std::cout<<y<<"   "<<x<<"\n";
        vector<int> result;
        int now_y=0, now_x=0;
        int walked=0;
        int facing=0;
        std::array<std::array<int,2>,4> way={{{0,1},{1,0},{0,-1},{-1,0}}};
        for(int i=0;i<(matrix[0].size()*matrix.size());++i){
            //std::cout<<now_y<<"   "<<now_x<<"  "<<min_y<<"  "<<min_x<<"  "<<y<<"  "<<x<<"\n";
            result.push_back(matrix[now_y][now_x]);
            if((facing==0 && now_x+way[facing][1]==x) || (facing==1 && now_y+way[facing][0]==y)|| (facing==2 && now_x+way[facing][1]==min_x) || (facing==3 && now_y+way[facing][0]==min_y)){
                //std::cout<<facing<<"\n";
                facing=(facing+1)%4;
                //std::cout<<facing<<"\n";
                walked+=1;
                if(walked==1){
                    min_y+=1;
                }else if(walked==2){
                    x-=1;
                }else if(walked==3){
                    y-=1;
                }else if(walked==4){
                    min_x+=1;
                    walked=0;
                }
            }
            //facing correct, now move
            now_y+=way[facing][0];
            now_x+=way[facing][1];
        }
        return result;
    }
};