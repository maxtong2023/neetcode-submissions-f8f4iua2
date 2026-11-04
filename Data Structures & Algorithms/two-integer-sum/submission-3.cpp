#include <unordered_map>
using namespace std;

class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> hasher;

        for (int i = 0; i < nums.size(); i++){
            if (hasher.contains(nums[i])){
                return {hasher[nums[i]], i};
            }
            hasher[target - nums[i]] = i;
        }
    }
};
