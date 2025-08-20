import java.util.ArrayList;

class Solution {
    // this needs fixing . tomorrow ! go to sleep
    public boolean isTransformation(String word1, String word2) {
        int sLength = word1.length();
        int numDiff = 0;
        for (int i = 0; i < sLength; ++i) {
            if (word1.charAt(i) != word2.charAt(i)) {
                ++numDiff;
            }
            if (numDiff > 1) {
                return false;
            }
        }
        return true;
    }

    public HashMap<String, List<String>> initializeAdjMap(List<String> wordList) {
        HashMap<String, List<String>> map = new HashMap<String, List<String>>();
        for (String word: wordList) {
            map.put(word, new ArrayList<String>());
        }
        return map;
    }

    public void fillAdjMap(HashMap<String, List<String>> map, List<String> wordList) {
        for (String word1 : wordList) {
            for (String word2 : wordList) {
                if (!word1.equals(word2) && isTransformation(word1, word2)) {
                    map.get(word1).add(word2);
                }
            }
        }
    }

    public int bfs(String beginWord, String endWord, HashMap<String, List<String>> adjMap) {
        // no connections through bfs will reach end
        if (adjMap.get(endWord).isEmpty()) {
            return 0;
        }

        // set up queue and visited
        LinkedList<String> queue = new LinkedList<String>();
        HashMap<String, Integer> visited = new HashMap<String, Integer>(); // maps word to number of steps it took to reach it.
        visited.put(beginWord, 1);
        queue.add(beginWord);

        // bfs loop
        while (!queue.isEmpty()) {
            String current = queue.pop();
            if (current.equals(endWord)) {
                break;
            }
            for (String neighbor : adjMap.get(current)) {
                if (visited.get(neighbor) == null) {
                    visited.put(neighbor, visited.get(current) + 1);
                    queue.add(neighbor);
                }
            }
        }
        return visited.get(endWord) == null ? 0 : visited.get(endWord);
    } 



    public int ladderLength(String beginWord, String endWord, List<String> wordList) {
        if (!wordList.contains(endWord)) {
            return 0;
        }
        if (!wordList.contains(beginWord)) {
            wordList.add(beginWord);
        }
        HashMap<String, List<String>> adjMap= initializeAdjMap(wordList);
        fillAdjMap(adjMap, wordList);
        return bfs(beginWord, endWord, adjMap);
    }
}
