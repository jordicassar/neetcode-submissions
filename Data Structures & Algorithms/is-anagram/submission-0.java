
class Solution {
    public boolean isAnagram(String s, String t) {
        HashSet <Integer> set = new HashSet<>();

    // Handles different lengths
        if(s.length != t.length){
            return false;
        }
    // Handles sames length
    if(s.length == t.length){
        for(int i = 0; i < s.length; i++){
            for(int j = 0; j < t.length; j++){
                if(s[i] == t[j]){
                    return true;
                }
            }
        }
    }

    }
}
