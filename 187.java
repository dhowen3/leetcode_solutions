class Solution {
    public int charToInt (char c) {
        if (c == 'A') {
            return 0;
        } else if (c == 'C') {
            return 1;
        } else if (c == 'G') {
            return 2;
        } else if (c == 'T') {
            return 3;
        } else {
            assert(false);
            return -1;
        }
    }

    public int getHashValue(String s) {
        int mask = 0;
        for (int i = 0; i < 10; ++i) {
            mask |= charToInt(s.charAt(i));
            mask <<= 2;
        }
        return mask;
    }

    public List<String> findRepeatedDnaSequences(String s) {
        LinkedList<String> toReturn = new LinkedList<String>();
        HashMap<Integer, Boolean> map = new HashMap<Integer, Boolean>();
        int n = s.length();
        for (int i = 0; i <= n -10; ++i) {
            String substr = s.substring(i, i + 10);
            int hashValue = getHashValue(substr);
            if (map.get(hashValue) == null) {
                map.put(hashValue, false);
            } else if (!map.get(hashValue)) {
                toReturn.add(substr);
                map.put(hashValue, true);
            } // else already added, do nothing 
        } 
        return toReturn;
    }
}
