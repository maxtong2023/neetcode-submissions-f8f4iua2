class Solution {
public:
    vector<int> dailyTemperatures(vector<int>& temperatures) {
        vector<pair<int, int>> stacker; 
        vector<int> result(temperatures.size());

        for(int i =0; i < temperatures.size(); i++){
            
            pair<int, int> curr = {temperatures[i], i};
            int temp = curr.first; 
            int currindex = curr.second;
            if (stacker.empty()) stacker.push_back(curr);
            else if(temp <= stacker.back().first){
                //temperature decreasing so we add it to the end of the stack 
                stacker.push_back(curr);
            }
            else{
                while (!stacker.empty() &&temp > stacker.back().first){
                    int poppedindex = stacker.back().second;
                    result[poppedindex] = currindex - poppedindex;
                    stacker.pop_back();
                }
                stacker.push_back(curr);
            }
        }
        return result; 
    }
};
