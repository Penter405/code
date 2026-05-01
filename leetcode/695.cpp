class Solution {
private:
    int recursion(std::vector<std::vector<int>>& grid,int index_first,int index_second){
        //std::cout<<"seeing "<<index_first<<"  "<<index_second<<'\n';
        //do self thing here, include set grid 
        if(index_first<0 || index_first>=grid.size() || index_second<0 || index_second>=grid[0].size()){
            //std::cout<<"out\n";
            return 0;
        }
        if(grid[index_first][index_second]==0){
            return 0;
        }
        grid[index_first][index_second]=0;
        int a=recursion(grid,index_first-1,index_second);
        int b=recursion(grid,index_first+1,index_second);
        int c=recursion(grid,index_first,index_second-1);
        int d=recursion(grid,index_first,index_second+1);
        return 1+a+b+c+d;
    }
public:
    int maxAreaOfIsland(vector<vector<int>>& grid) {
        int max_size=0;
        for(int i=0;i<grid.size();++i){
            for(int u=0;u<grid[0].size();++u){
                if(grid[i][u]==1){
                    
                    int now=recursion(grid,i,u);
                    std::cout<<now<<'\n';
                    if(now>max_size){
                        max_size=now;
                    }
                }
            }
        }
        return max_size;
    }
};