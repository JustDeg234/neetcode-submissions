class Solution{
    public: bool isHappy(int n){
        std::unordered_set<int> visit; // allows to identify duplicates (cycles) in constant time O(1)
        //through each iteration of sumofSquares(), n is replaced by either 1 or not
        while(visit.find(n) == visit.end()){ //default checker to populate set
            visit.insert(n);
            n = sumofSquares(n); //returns 1 or not, set keeps track of duplicates, if encountered then cycle is detected and false is returned 
            if(n == 1) return true;
        }
        return false;
    }
    private: int sumofSquares(int n){
        int sum = 0; //initial global function var

        while(n>0){ //n will be split digit by digit until floor division handles fractions
            int ones = n % 10; 
            ones *= ones; //squared
            sum += ones; //sum
            n = n/10; //next digit up
        }
        return sum;
    }
};