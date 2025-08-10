#define UPPER_RANGE 2147483647  
#define LOWER_RANGE -2147483648 

void ignoreWhitespace(char* s, size_t* index, size_t strLen) {
    while (*index < strLen && s[*index] == ' ') {
        *index = *index + 1;
    }
}

void ignoreZeros(char* s, size_t* index, size_t strLen) {
    while (*index < strLen && s[*index] == '0') { 
        ++(*index);
    }
}

bool isDigit(char c) {
    return c >= '0' && c <= '9';
}

/*
 * if current char in s is '-', return true and increment current index by 1.
 * else return false.
 */
bool isNegative(char* s, size_t* index, size_t strLen) {
    bool toReturn = false;
    assert(!toReturn); // think bool in c is set to false by default but double check
                       // this assumption.
    if (*index < strLen && s[*index] == '-') {
        toReturn = true;
        ++(*index);
    } else if(*index < strLen && s[*index] == '+') {
        ++(*index);
    }
    return toReturn;
}

int roundIfNecessary(bool negative, long toReturn, bool outOfRange) {
    if (outOfRange) {
        return (int)toReturn;
    }
    int intVal;
    if (negative && toReturn > -LOWER_RANGE) {
        intVal = LOWER_RANGE;
    } else if (negative) {
        toReturn = -toReturn;
        intVal = (int)toReturn;
    } else if (toReturn > UPPER_RANGE) {
        intVal = UPPER_RANGE;
    } else {
        intVal = (int)toReturn;
    }
    return intVal;
}

int charToInt(char c) {
    return (int)(c - '0');
}

bool checkIfLenImpliesOOB(size_t startIndex, size_t endIndex) {
    return endIndex - startIndex > 10;
}

long getVal(char* s, size_t startIndex, size_t endIndex) {
    long toReturn = 0;
    long tensPower = 1;
    for (int i = endIndex - 1; i >= startIndex && i >= 0; i--) {
        printf("i: %d\n", i);
        toReturn += charToInt(s[i]) * tensPower;
        tensPower *= 10;
    }
    return toReturn;
}

int myAtoi(char* s) {
    bool negative, outOfRange;
    size_t index, strLen, startIndex, endIndex;
    long currentVal;
    int toReturn;

    index = 0;
    strLen = strlen(s);
    outOfRange = false;

    ignoreWhitespace(s, &index, strLen);
    printf("post whitespace - index is %d.\n", index);
    negative = isNegative(s, &index, strLen);
    printf("%d\n", negative);
    ignoreZeros(s, &index, strLen);
    printf("post zeros - index is %d.\n", index);
    startIndex = index;
    endIndex = index;
    while (index < strLen && isDigit(s[index])) {
        endIndex = ++index;
    }
    printf("startIndex : %d, endIndex : %d\n", startIndex, endIndex);
    if (checkIfLenImpliesOOB(startIndex, endIndex)) {
        currentVal = negative ? LOWER_RANGE : UPPER_RANGE;
        outOfRange = true;
    } else if (endIndex == startIndex) {
        return 0;
    } else {
        currentVal = getVal(s, startIndex, endIndex);
    }
    printf("currentVal : %d\n", currentVal);
    toReturn = roundIfNecessary(negative, currentVal, outOfRange);
    printf("%d\n", LOWER_RANGE);
    return toReturn;
}
