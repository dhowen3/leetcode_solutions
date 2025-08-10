int findTargetRowHelper(int **matrix, int lowBound, int highBound, int target) {
    // base case
    if (highBound - lowBound <= 1) {
        return lowBound;
    }
    // recursive case
    int halfOfCurrentRange = (lowBound + highBound) / 2;
    if (target < matrix[halfOfCurrentRange][0]) {
        return findTargetRowHelper(matrix, lowBound, halfOfCurrentRange, target);
    } else {
        return findTargetRowHelper(matrix, halfOfCurrentRange, highBound, target);
    }
}


int findTargetRow(int **matrix, int numRows, int target) {
    int targetRow = findTargetRowHelper(matrix, 0, (numRows), target);
    return targetRow; 
}

bool findTargetInRowHelper(int **matrix, int lowBound, int highBound, int target, int targetRow) {
    // base case
    if (highBound - lowBound <= 1) {
        return matrix[targetRow][lowBound] == target || matrix[targetRow][highBound] == target;
    }
    // recursive case
    int halfOfCurrentRange = (lowBound + highBound) / 2;
    if (target < matrix[targetRow][halfOfCurrentRange]) {
        return findTargetInRowHelper(matrix, lowBound, halfOfCurrentRange, target, targetRow);
    } else {
        return findTargetInRowHelper(matrix, halfOfCurrentRange, highBound, target, targetRow);
    }
}

bool findTargetInRow(int **matrix, int numCols, int targetRow, int target) {
    return findTargetInRowHelper(matrix, 0, numCols - 1, target, targetRow);
}

bool searchMatrix(int** matrix, int matrixSize, int* matrixColSize, int target){
    int numCols = *matrixColSize; 
    int numRows = matrixSize;
    if (numRows * numCols == 0) {
        // return false if either numRows or numCols is 0
        return false;
    }
    if (target < matrix[0][0]) {
        // return false if target is less than first entry of matrix
        return false;
    }
    int targetRow = findTargetRow(matrix, numRows, target);
    printf("target row: %d\n", targetRow);
    bool isInMatrix = findTargetInRow(matrix, numCols, targetRow, target);
    return isInMatrix;
}
