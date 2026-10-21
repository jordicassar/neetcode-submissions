class MinStack {
public:
        stack<int> stac;
        stack<int> min;
    MinStack() {
        
    }
    
    void push(int val) {
        stac.push(val);
        if (min.empty()) {
            min.push(val);
        }
        else if (min.top() < val) {
            min.push(min.top());
        }
        else {
            min.push(val);
        }
    }
    
    void pop() {
        stac.pop();
        min.pop();
    }
    
    int top() {
        return stac.top();
    }
    
    int getMin() {
        return min.top();
    }
};
