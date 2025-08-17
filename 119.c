int binomialCoeff(int upper, int lower) {
    long toReturn = 1;
    int lowerMax = upper - lower >= lower ? upper - lower : lower;
    int lowerMin = upper - lower < lower ? upper - lower : lower;
    for (int i = upper; i > lowerMax; --i) {
        toReturn *= i;
        int divisorIndex = upper - i;
        if (divisorIndex < lowerMin) {
            int divisor = divisorIndex + 1;
            toReturn /= divisor;
        }
    }
    /*
    for (int i = 1; i <= lowerMin; ++i) {
        toReturn /= i;
    }
    */
    return toReturn;
}

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* getRow(int rowIndex, int* returnSize){
    *returnSize = rowIndex + 1;
    int* toReturn = malloc(sizeof(int) * (*returnSize));
    // useful to know binomial coeffieicnts' relationship to pascal's triangle
    // shoutout to professor terwilliger who taught introduction to combinatorics
    for (int i = 0; i <= rowIndex; ++i) {
        toReturn[i] = binomialCoeff(rowIndex, i);
    }
    return toReturn;
}
