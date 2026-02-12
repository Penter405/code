//same versuion in neetcode150/1.arrays&hashing/8.Valid Sudoku.cpp
#include <array>
#include <unordered_set>
#include <vector>
using namespace std;

class Solution {
private:
    std::array<std::unordered_set<char>,9> ob,unob;//wheather hashset data in same
    std::array<std::array<std::unordered_set<char>,3>,3> sqare;
    bool go_set(char guy,int y,int x){
        if(ob[x].find(guy)!=ob[x].end()){
            return false;
        }
        ob[x].insert(guy);
        if(unob[y].find(guy)!=unob[y].end()){
            return false;
        }
        unob[y].insert(guy);
        if(sqare[y/3][x/3].find(guy)!=sqare[y/3][x/3].end()){
            return false;
        }
        sqare[y/3][x/3].insert(guy);
        return true;
    }
public:
    bool isValidSudoku(vector<vector<char>>& board) {
        for(int y=0;y<9;++y){
            for(int x=0;x<9;++x){
                //std::cout<<board[y][x]<<" "<<y<<"   "<<x<<"\n";
                if(board[y][x]!='.' && not go_set(board[y][x],y,x)){
                    return false;
                }
            }
        }
        return true;
    }
};
