class Solution {

    public static String formatRepeating(String decimal, long repeatingStart) {
        return decimal.substring(0, (int)repeatingStart) + "(" 
                + decimal.substring((int)repeatingStart, decimal.length()) + ")";  
    }

    public static long remainderListContains(ArrayList<long[]> remainderList, long remainder) {
        long digitsPlace = -1;
        for (long [] elt : remainderList) {
            if (elt[0] == remainder) {
                digitsPlace = elt[1];
            }
        }
        return digitsPlace;
    }

    public static String[] getBaseDecimal(long numerator, long denominator) {
        // decls
        String base = "", decimal = "", numString = "" + numerator;
        long remainder, repeatingStart = -1, digitsPlace = 0;
        ArrayList<long[]> remainderList = new ArrayList<long[]>();

        // set num, denom to non-neg. negativity for final program retval handled in main().
        numerator = Math.abs(numerator);
        denominator = Math.abs(denominator);

        // first find base
        base = "" + (long) numerator / denominator; 
        remainder = numerator % denominator;

        // loops to find decimal
        while (true) {
            long containsIndex = remainderListContains(remainderList, remainder);
            if (containsIndex != -1) {
                repeatingStart = containsIndex; 
                break;
            } else if (remainder == 0 && digitsPlace == 0) {
                decimal = "0";
                break;
            } else if (remainder == 0) {
                break;
            } else {
                remainderList.add(new long[] {remainder, digitsPlace});
            }
            boolean addingZeros = false;
            while (remainder < denominator) {
                remainder *= 10;
                if (!addingZeros) {
                    addingZeros = true;
                } else {
                    decimal += "0";
                }
                digitsPlace += 1;
                // add remainders to remainderList here?
            }
            decimal += (long) remainder / denominator;
            remainder = remainder % denominator;

        }

        // add parentheses if repeating
        if (repeatingStart != -1) {
            decimal = formatRepeating(decimal, repeatingStart);
        }

        // return
        return new String[] {base, decimal};
    }

    public static String formatAnswer(String base, String decimal, boolean negative) {
        String toReturn = "";
        if (negative) {
            toReturn += "-";
        }
        toReturn += base;
        if (!decimal.equals("0")) {
            toReturn += ".";
            toReturn += decimal;
        }
        return toReturn;
    }


    public String fractionToDecimal(long numerator, long denominator) {
        if (numerator == 0) {
            return "0";
        }
        boolean negative = (numerator < 0) ^ (denominator < 0); // retval is negative
        String[] baseDecimal = getBaseDecimal(numerator, denominator);
        String answer =  formatAnswer(baseDecimal[0], baseDecimal[1], negative);
        return answer;
    }
}
