uint32_t reverseBits(uint32_t n) {
    uint32_t toReturn = 0;
    for (int i = 0; i < 32; ++i) {
        toReturn = toReturn << 1; 
        toReturn = toReturn | (n & 0b1);
        n = n >> 1;
    }
    return toReturn;
}
