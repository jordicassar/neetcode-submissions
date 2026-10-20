class Solution {
public:
    int calPoints(vector<string>& operations) {
        std::vector<int> ops;
        for (int i = 0; i < operations.size(); i++) {
            if (operations[i] == "+") {
                ops.push_back(ops.back() + ops[ops.size() - 2]);
            }
            else if (operations[i] == "D") {
                int x = ops.back() * 2;
                ops.push_back(x);
            }
            else if (operations[i] == "C") {
                ops.pop_back();
            }
            else {
                int y = std::stoi(operations[i]);
                ops.push_back(y);
            }
            
        }
        int total = 0;
        for (int i = 0; i < ops.size(); i++) {
            total += ops[i];
        }
        return total;
    }
};