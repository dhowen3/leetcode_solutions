class Solution {
    public int romanToInt(String s) {
        char[] numerals = {'I', 'V', 'X', 'L', 'C', 'D', 'M'};
        int[] numeralValues = {1, 5, 10, 50, 100, 500, 1000};
        int sum = 0;
        int previousValue = 0;
        for (int i = s.length() - 1 ; i >= 0; --i) {
            // it is defined that a valid numeral will be passed as input
            // goal - read string right to left - search through 
            // chars array. pass the index in chars array to numeralValues
            Character currentChar = s.charAt(i);
            int currentValue = getNumeralValue(currentChar);
            if (currentValue >= previousValue) {
                sum += currentValue;
            } else {
                sum -= currentValue;
            }
            previousValue = currentValue;
            
            
            
        }
        return sum;
    }
    
    public int getNumeralValue(char numeral) {
        switch (numeral) {
            case 'I': 
                return 1;
            case 'V': 
                return 5;
            case 'X': 
                return 10;
            case 'L':
                return 50;
            case 'C':
                return 100;
            case 'D':
                return 500;
            case 'M':
                return 1000;
        }
        return -1;
    }
}
