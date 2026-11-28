class Solution {
public:
    int maxArea(vector<int>& heights) {
        int left = 0; 
        int right = heights.size() - 1; 

        int best = 0; 

        while(left < right){
            int area = min(heights[left], heights[right]) * (right - left); 
            best = max(best, area);

            if(heights[left] > heights[right]){
                right--;
            } 
            else{
                left++; 
            }
        }
        return best; 
    }
};
