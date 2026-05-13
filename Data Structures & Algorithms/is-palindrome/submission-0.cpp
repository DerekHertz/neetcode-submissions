class Solution {
public:
    bool isPalindrome(string s) {
        
        int left = 0; //start point
        int right = static_cast<int>(s.length()) - 1; //end pointer

        while (left < right) {
            while (left < right && !std::isalnum(static_cast<unsigned char>(s[left]))) {
                left++;
            }
            while (left < right && !std::isalnum(static_cast<unsigned char>(s[right]))) {
                right--;
            }

            if (std::tolower(static_cast<unsigned char>(s[left])) !=
                std::tolower(static_cast<unsigned char>(s[right]))) {
                    return false;
            }
            left++;
            right--;
        }
        return true;
    }
};
