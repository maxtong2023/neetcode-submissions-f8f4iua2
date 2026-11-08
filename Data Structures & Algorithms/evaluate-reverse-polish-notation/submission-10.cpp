class Solution {
public:
    int evalRPN(vector<string>& tokens) {
        vector<int> stacker; 
        set<string> operators = {"+", "-", "/", "*"};

        for (string token : tokens){
            // can i assume when i reach an operator there will always be 2 element in the stack?
            if (operators.contains(token))
            {
                int second = stacker.back(); 
                stacker.pop_back();
                int first = stacker.back(); 
                stacker.pop_back();
                if(token == "+") stacker.push_back(first + second); 
                else if(token == "-") stacker.push_back(first - second);
                else if(token == "/") stacker.push_back(first / second);
                else stacker.push_back(first * second);
            }
            else{
                stacker.push_back(stoi(token));
            }
        }

        return stacker.back();
    }
};
