class Solution {
        
    public int reverse(int x) {
        boolean negative = false;
        boolean outOfBounds = false;
        String maxInt = String.valueOf(Integer.MAX_VALUE);
        String minInt = String.valueOf(Integer.MIN_VALUE);
        minInt = minInt.substring(1);
        if (x == Integer.MIN_VALUE) {
            return 0;
        }
        if (x < 0) {
            negative = true;
            x = -x;
        }
        String toReturn = "";
        String xStr = String.valueOf(x);
        int strLen = xStr.length();
        if (strLen < maxInt.length()) {
            for (int i = strLen - 1; i >= 0; --i) {
                toReturn += xStr.charAt(i);
            }
        } else {
            String compare = negative ? minInt : maxInt;
            boolean maybeOutOfBounds = true;
            System.out.println(strLen - 1);
            for (int i = strLen - 1; i >= 0; --i) {
                int j = 10 - i -1;//compare.length() - i - 1;
                System.out.println(i + " " + j);
                System.out.println("" + xStr.charAt(i) + "," + compare.charAt(j));
                if (maybeOutOfBounds) {
                    if (xStr.charAt(i) < compare.charAt(j)) {
                        maybeOutOfBounds = false;
                        toReturn += xStr.charAt(i);
                    } else if (xStr.charAt(i) == compare.charAt(j)) {
                        toReturn += xStr.charAt(i);
                    } else {
                        outOfBounds = true;
                        toReturn = "0";
                        break;
                    }
                } else {
                    toReturn += xStr.charAt(i);
                }
            }
        }
        if (negative && !outOfBounds) {
            toReturn = "-" + toReturn;
        }
        return Integer.parseInt(toReturn);
    }
}
