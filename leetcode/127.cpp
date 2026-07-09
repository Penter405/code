struct queue{
    std::string value;
    *queue next;
};


class Solution {
private:
    std::unordered_map<std::string, int> depth;
    std::unordered_set<std::string> words;
    std::unordered_set<std::string> walked;
    std::string target;
    std::queue seeing, last;
    std::final_ans=-1;
    int is_near(string a, string b){
        if(a.size()!=b.size()){
            return 0;
        }
        wrong_count=0;
        for(int x=0;x<a.size();++x){
            if(wrong>1){
                return 0;
            }
            if(a[x]!=b[x]){
                wrong++;
            }
        }
        if(wrong>1 || wrong==0){
                return 0;
            }
        return 1;
    }
    int init(vector<string>& wordList,string b){
        for(auto it:wordList){
            words.insert(it);
        }
        target=b;
        return 0;
    }
    int add(queue last,string new_one){
        queue a_node;
        a_node.value=new_one;
        last.next=a_node;
        last=a_node;
    }
    int bfs(string a){
        if(final_ans!=-1){
            return 0;
        }
        seeing.value=a;
        depth[]
        result=-1;
        while(final_ans!=-1){
            for(auto it:words){
                if(is_near(node.value,it)){

                }
            }

            if(node->next==nullptr){
                return 0;
            }
            node=node->next;
        }
        /*
        for(auto it:words){
            if(walked.find(it)==walked.end() && is_near(a,it)){
                bfs();
            }
        }
        */
    }
public:
    int ladderLength(string beginWord, string endWord, vector<string>& wordList) {
        init(wordList, endWord);
        bfs(beginWord);
    }
};