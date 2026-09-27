
class Solution {
    public boolean isAnagram(String s, String t) {
        HashSet <Integer> set = new HashSet<>();

    // Handles different lengths
        if(s.length() != t.length()){
            return false;
        }
    
    // converts Strings in to Character Arrays
    char[] sSort = s.toCharArray();
    char[] tSort = t.toCharArray();

    // Sorts these arrays in alphabetical order
    Arrays.sort(sSort);
    Arrays.sort(tSort);

    // Returns if they're equal
    return Arrays.equals(sSort, tSort);

    

    }
}
