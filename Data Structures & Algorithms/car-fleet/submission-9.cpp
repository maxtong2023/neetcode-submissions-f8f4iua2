class Solution {
public:
    int carFleet(int target, vector<int>& position, vector<int>& speed) {
       vector<pair<int, int>> mapping; 

       for(int i = 0; i < position.size(); i++){
        pair<int, int> curr = {position[i], speed[i]}; 
        mapping.push_back(curr); 
       }    
       sort(mapping.begin(), mapping.end(), greater<>()); 

       //now the elements are all in reverse order, from greatest position to least position.
        vector<double> stacker; 
        //int fleets; 
       for(auto& [p, s] : mapping){
        //p and s are the current car's position and speed
        double steps = (double)(target - p) / s; //how many steps it takes to reach the destination

        if(stacker.empty()){
            stacker.push_back(steps); 
        }
        // we need to keep a monotonically increasing stack. this means that cars with less position take more steps to get to the destination so they never merge with the car in front of it.
        else if (stacker.back() < steps){
            stacker.push_back(steps); 
        }
       }

       return stacker.size();
    }
};
