class Solution {
private:
    
    //preorder
    int recursion(std::vector<std::vector<char>>& grid,int index_first,int index_second){
        //std::cout<<"seeing "<<index_first<<"  "<<index_second<<'\n';
        //do self thing here, include set grid 
        if(index_first<0 || index_first>=grid.size() || index_second<0 || index_second>=grid[0].size()){
            //std::cout<<"out\n";
            return 0;
        }
        if(grid[index_first][index_second]=='0'){
            return 0;
        }
        grid[index_first][index_second]='0';
        recursion(grid,index_first-1,index_second);
        recursion(grid,index_first+1,index_second);
        recursion(grid,index_first,index_second-1);
        recursion(grid,index_first,index_second+1);
        return 0;
    }
    //std::unordered_map<std::array<int,2>,int> ever_seen, to_do;
    /*
    void initialize(vector<vector<char>>& grid){
        //1 <= m, n <= 300 
        // at least one line, good, no ram out
        for(int i=0;i<grid.size();++i){
            for(int u=0;u<grid[0].size();++u){
                std::array<int,2> bot;
                bot[0]=i;
                bot[1]=u;
                to_do[bot]=
            }
        }
    }*/
    
public:
    int numIslands(std::vector<std::vector<char>>& grid) {
        //when pass, pass by reference with change value to not binary, so it means we have runed, no more need pass it.
        //or put on to_do, well, we pur on to do would do better
        //option first is best
        int index_of_island=0;
        for(int i=0;i<grid.size();++i){
            for(int u=0;u<grid[0].size();++u){
                if(grid[i][u]=='1'){
                    ++index_of_island;
                    recursion(grid,i,u);
                }
            }
        }
        return index_of_island;
    }
};