class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        //i think i should store all these as tuples. 

        //requires sorting and two pointer. 

        // One idea that I have is to loop through every possible combination and make a tuple with the values added together, the first index, and the second index. 

        // wait but storing tuples will require linear space. 
        sort(nums.begin(), nums.end()); 
        //what changes now that things are sorted? 
        // i can do the same idea as before where I check the element from the rightmost point.

        // ok... i do not need tuples. 

        vector<vector<int>> result; 
        int temp;
        //issue is that I don't want duplicates. 
        for(int i = 0; i < nums.size(); i++){
            if(i >= 1 && nums[i -1] == nums[i]){
                continue;
            }
            int target = -nums[i]; //what the two numbers must sum to

            int left = i + 1; 
            int right = nums.size() - 1; 

            while(left < right){
                int sum = nums[left] + nums[right]; 
                if(sum == target){
                    if((left > i + 1 && nums[left - 1] == nums[left]) || (right < nums.size() -1 && nums[right + 1] == nums[right])){
                        left++;
                        right--;
                        continue;
                    }
                    vector<int> curr = {nums[i], nums[left], nums[right]}; 
                    result.push_back(curr); 
                    left++; 
                    right--;
                }
                else if (sum > target){
                    right--; 
                }
                else{
                    left++; 
                }
            }
        }
        return result;
    }
};
