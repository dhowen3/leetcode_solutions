#include<math.h>
#include<string.h>

bool isPalindrome(int x){
    char numStr[15];
    sprintf(numStr, "%d", x);
    int strLen = strlen(numStr);
    for (int i = 0; i < strLen / 2; ++i) {
        int lowIndex = i;
        int highIndex = strLen - i - 1;
        if (numStr[lowIndex] != numStr[highIndex]) {
            return false;
        }
    }
    return true;
}
