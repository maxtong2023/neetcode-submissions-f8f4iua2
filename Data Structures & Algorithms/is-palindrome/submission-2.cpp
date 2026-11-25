class Solution {
public:
    bool isPalindrome(string s) {
         
        int left = 0; 
        //need to filter for only alphanumeric
        erase_if(s, [](unsigned char c){
            return !isalnum(c);
        });

        int right = s.size() - 1;



        while (left < right){
            if(tolower(s[right]) != tolower(s[left])){
                return false; 

            }
            left++; 
            right--; 
        }
        return true; 
    }
};
