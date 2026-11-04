#include <unordered_map>
using namespace std;


class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
       // you can sort every string, but this becomes mlogm * n
       // you ideally want some way to iterate through each string
       // check their counts, and create a new list when the counts are
       // different than the existing counts, or add to a list of 
       // existing strs with that count. It sounds like a hashmap 
       // with the counts as the key and the list of strs as the value. 
       // except strings are mutable.

       unordered_map<string, vector<string>> groups{};

       array<int, 26> counts{};
       for (string s : strs){
        //reset counts back to [0,0,0etc.]
        counts = {};
        for (char c : s){
            counts[c - 'a']++;
        }
        string key(counts.begin(), counts.end());
        groups[key].push_back(s);
        }
    
    //return the array
    vector<vector<string>> result; 

    for(auto& [key, group]: groups) result.push_back(group);
    return result;


    }
};
