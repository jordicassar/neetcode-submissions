class Solution {
public:
    vector<int> replaceElements(vector<int>& arr) {
        int max = 0;
        for (int i = 0; i < arr.size() - 1; i++) {
            for (int j = i + 1; j < arr.size(); j++) {
                if (arr[j] > max) max = arr[j];
            }
            arr[i] = max;
            max = 0;
        } 
        arr[arr.size() - 1] = -1;
        return arr;
    }
};