class Solution {
public:
    bool isValid(string s) {
       std::stack<char> stack;
       std::unordered_map<char, char> closeToOpen = {{')', '('}, {']', '['}, {'}', '{'}};
       for (char c : s) {
            if (c == ')' || c == '}' || c == ']') {
                if (!stack.empty() && stack.top() == closeToOpen[c]) {
                    stack.pop();
                }
                else {
                    return false;
                }
            }
            else {
            stack.push(c);
            }
       }
       return stack.empty();
    }
};
