#include <unordered_map>
using namespace std; 

class Solution {
public:
    bool isAnagram(string s, string t) {
        unordered_map<char, int> strings;
        unordered_map<char, int> stringt;

        if (s.size() != t.size()){
            return false;
        }
        for (char c : s) strings[c]++;
        for (char c : t) stringt[c]++;

        if (strings == stringt) return true;
        return false;
    }
};
