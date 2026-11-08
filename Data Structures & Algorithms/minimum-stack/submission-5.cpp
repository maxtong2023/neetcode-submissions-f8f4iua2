#include <utility>

class MinStack {
public:

    // i think that getmin is going to be the bottleneck. 

    // other operations make sense, they are easy to get constant time. 
    // bit you need something to keep track of the min element 
    vector<pair<int, int>> stacker;
    int smallest; 
    // you could keep another stack in descending order? sounds like a heap...
    // which wouldn't work.

    //i really think the idea is to have another stack?
    // when you pop, should automatically update the next smallest value. 
    // you could add tuples into the stack? The tuple can be the value you want to add first and the second is the minimum element before it got inserted? 
    MinStack() {
        smallest = INT_MAX; 
    }
    
    void push(int val) {
        
        stacker.push_back({val, smallest});
        smallest = min(smallest, val); 
    }
    
    void pop() {
        int temp = stacker[stacker.size() - 1].second; 
        stacker.pop_back();
        // set smallest back to the shit before
        smallest = temp; 
    }
    
    int top() {
        return stacker[stacker.size() - 1].first;
    }
    
    int getMin() {
        return smallest; 
    }
};
