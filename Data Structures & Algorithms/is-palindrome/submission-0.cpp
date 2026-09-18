class Solution {
public:
    bool isPalindrome(string s) {
        erase_if(s, [](unsigned char c){return !isalnum(c);});
        int len = s.size();
        for (int i = 0; i <len / 2; i++) {
            if (tolower(s[i]) != tolower(s[len-1-i])) {
                return false;
            }
        }
        return true;
    }
};
