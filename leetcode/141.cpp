/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 **/
#include <iostream>
#include <unordered_set>


//version1-- tried , but i maped the value, not object address. fail
class Solution {
public:
    bool hasCycle(ListNode *head) {
        std::unordered_set<int> seem;
        while(head!=nullptr){
            if(seem.find((*head).val)!=seem.end()){
                return true;
            }
            seem.insert((*head).val);
            ++head;
        }
        return false;
    }
};

//version2-- the wrong using pointer version.
class Solution {
public:
    bool hasCycle(ListNode *head) {
        std::unordered_set<ListNode*> seem;
        while(head!=nullptr){
            if(seem.find((*head).val)!=seem.end()){
                return true;
            }
            seem.insert((*head).val);
            head=(*head).next;
        }
        return false;
    }
};

//version3-- it seems i dont really get how pointer work when change name from int to another. so i debuged several time.
class Solution {
public:
    bool hasCycle(ListNode *head) {
        std::unordered_set<ListNode*> seem;
        while(head!=nullptr){
            if(seem.find((*head).next)!=seem.end()){
                return true;
            }
            seem.insert((*head).next);
            head=(*head).next;
        }
        return false;
    }
};