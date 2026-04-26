class Solution{
    public: bool isHappy(int n){
        int slow = n, fast = sumofSquares(n); //2 pointers, curr and next

        while(slow != fast){ //if cyclic, eventually slow wil catch up with fast, if acyclic, both will be 1
            fast = sumofSquares(fast);
            fast = sumofSquares(fast);
            slow = sumofSquares(slow);
        }
        return fast == 1; //if noncyclic, fast == slow == 1 return true. if any other value, return false

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