bool isPalindrome(int x){
    long long reversed = 0;
    int remaining ;
    unsigned original;
    original = x;
    while(x != 0)
    {   
        remaining = x % 10;
        reversed = reversed * 10 + remaining;
        x /=10;
    }
    
    if(original == reversed )
        return 1;
    else
        return 0;
}