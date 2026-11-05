#include <unordered_map>

class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        //i think the idea here is to just create buckets. 
        // at most you can have size nums elements of one integer. 


        vector<vector<int>> buckets(nums.size() + 1);
        unordered_map<int, int> mapping{};

        for (int num : nums) mapping[num]++; 
        for (auto& [key, value]: mapping) buckets[value].push_back(key);
        vector<int> result{}; 
        int count = 0; 
        int index = buckets.size() - 1; 
        while (count != k){
            for (int i : buckets[index]){
                result.push_back(i);
                count++; 
                if (count == k) return result;
            }
            index--;
        }

        return result;
    }
};
