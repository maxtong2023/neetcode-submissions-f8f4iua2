#include <unordered_map>
using namespace std;

class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        unordered_map<int, int> hasher;
        for(int i = 0; i < nums.size(); i++){
            if(hasher.contains(nums[i])){
                return true;

            }
            hasher.insert({nums[i], i});
        }

        return false;
    }
};