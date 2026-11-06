#include <unordered_map>
#include <set>
class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        // you could iterate through the vector once and store the value + 1

        //then iterate through that map and keep the longest sequence?
        // does this not just work

        set<int> hasher; 
        for(int num: nums) hasher.insert(num); 
        int best = 0;

        for (const auto& val: hasher){
            
            if(hasher.contains(val - 1)) continue; // don't check for this because it is not a start of a sequence 
            int count = 0;
            int curr = val;
            while (hasher.contains(curr)){
                curr++;
                count++; 
                best = max(best, count);
            }

        } 
        return best;  
   
    }
};
