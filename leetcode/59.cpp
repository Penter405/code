class Solution {
public:
    vector<vector<int>> generateMatrix(int n) {
        std::vector<vector<int>> result;
        for(int i=0;i<n;++i){
            std::vector<int> ob2;
            result.push_back(ob2);
            for(int z=0;z<n;++z){
                result[i].push_back(0);
            }
        }
        // init done
        //int rs=0;
        int lag=n;
        int went=0;
        std::array<array<int,2>,4> facing ={{{0,1},{1,0},{0,-1},{-1,0}}};//ob , unob
        int ob=0, unob=0;
        int faced=0;
        for(int i=0;i<(n*n);++i){
            std::cout<<ob<<"  "<<unob<<"  "<<((ob<=n)&&(unob<=n))<<"  "<<faced<<"\n";
            result[ob][unob]=i;
            
            if(went==lag){
                faced+=1;
                if(faced==4){
                    faced=0;
                }
                went=0;
            }
            ob+=facing[faced][0];
            unob+=facing[faced][1];
            went+=1;
        }
        return result;
    }
};