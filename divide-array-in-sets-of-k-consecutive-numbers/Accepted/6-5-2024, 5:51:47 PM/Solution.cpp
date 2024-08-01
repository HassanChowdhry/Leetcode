// https://leetcode.com/problems/divide-array-in-sets-of-k-consecutive-numbers

// #pragma GCC optimize("O3,unroll-loops")
int ed[100001];
int speedup = []{ios::sync_with_stdio(0); cin.tie(0); return 0;}();

class Solution {
public:
    bool isPossibleDivide(vector<int>& nums, int k) {
        int N = nums.size();
        if (N % k) return false;
        if (k == 1) return true;
        
        std::priority_queue<int> minheap;
        std::map<int, int> frq;

        for (int num: nums) {
            if (!frq.contains(num)) {
                frq[num] = 0;
                minheap.push(num);
            }
            frq[num] += 1;
        }
        
        while (minheap.size()) {
            int peek = minheap.top();

            for (int i = peek; i >= abs(peek-k+1); --i) {
                if (!frq.contains(i)) {
                    return false;
                } 
                frq[i]-=1;
                if (frq[i] == 0) {
                    frq.erase(i);
                    if (i == minheap.top()) minheap.pop();
                }
            }
        }
        return true;
    }
};