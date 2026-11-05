class Solution {
public:

    string encode(vector<string>& strs) {
        // so basically you want to turn this into a string, and 

        //have a way to remember how to get it back into list form. 
        //im thinking you can have some sort of sentinel value followed
        //by the length of the string.

        // so what if you turned Hello World into "Hello#World"
        string result; 
        int len; 
        for(int i = 0; i < strs.size(); i++){
            len = strs[i].size(); 
            result+= to_string(len) + "#" + strs[i]; 
            
        }
        return result;
    }

    vector<string> decode(string s) {
        vector<string> result;
        int index = 0; 
        int end = 0; 
        string len; 
        while (index < s.size()){
            if (s[index] != '#'){
                len+= s[index];
                index++;
            } 
            else{
                int intlen = stoi(len); 
                len = ""; 
                result.push_back(s.substr(index + 1,intlen));
                index = index + 1 + intlen; 
            }
        }   
        return result;
    }
};
