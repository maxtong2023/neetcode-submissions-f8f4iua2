#include <unordered_map>
#include <set>
class Solution {
public:

    int box(int r, int c){
        //I want to find out which box the element is in.
        return (r / 3) * 3 + (c / 3);


    }
    bool isValidSudoku(vector<vector<char>>& board) {
        // maybe you can have numbers mapped to 

        unordered_map<int, set<char>> rows; 
        unordered_map<int, set<char>> cols; 
        unordered_map<int, set<char>> boxes; 

        for(int row = 0; row < board.size(); row++){

            for (int col = 0; col < board.size(); col++){
                char cell = board[row][col]; 
                if(cell == '.') continue;
                if(rows[row].contains(cell) || cols[col].contains(cell)||boxes[box(row, col)].contains(cell)){
                    return false;
                }
                //does not exist so insert in
                rows[row].insert(cell);
                cols[col].insert(cell);
                boxes[box(row, col)].insert(cell);


            }
        }
        return true;


    }
};
