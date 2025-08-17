void rotate(int* nums, int numsSize, int k) {
    int copyArr[numsSize];
    memcpy(copyArr, nums, sizeof(int) * numsSize);
    for (int i = 0; i < numsSize; ++i) {
        nums[(i + k) % numsSize] = copyArr[i];
    }
}
