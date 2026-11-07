class Solution {
public:
    bool isValid(string s) {
    unordered_map<char, char> hasher = {
        {'}', '{'},
        {']', '['},
        {')', '('}
    };

        vector<char> stack; 

        for (int i = 0; i < s.size(); i++){
            char curr = s[i];
            if (hasher.contains(curr)){
                if (stack.empty()) return false; 
                if (stack[stack.size() - 1] == hasher[curr]) stack.pop_back();
                else return false; 
            }
            else stack.push_back(curr);
        }
        if (!stack.empty()) return false;
        return true;
        
    }
};
