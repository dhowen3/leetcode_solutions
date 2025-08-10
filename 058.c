int lengthOfLastWord(char * s){
    int strLen = strlen(s);
    int toReturn = 0;
    for (int i = strLen - 1; i >= 0; --i) {
        if (s[i] != ' ') {
            for (int j = i; j >= 0; --j) {
                if (s[j] == ' ') {
                    return toReturn;
                } else {
                    ++toReturn;
                    if (j == 0) {
                        return toReturn;
                    }
                }
            }
        }
    }
    return toReturn;
}
