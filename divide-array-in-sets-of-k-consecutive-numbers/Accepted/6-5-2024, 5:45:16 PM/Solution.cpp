// https://leetcode.com/problems/divide-array-in-sets-of-k-consecutive-numbers

#pragma GCC optimize("03,unroll-loops")
class Solution {
public:
    bool isPossibleDivide(vector<int>& nums, int k) {
        int N = nums.size();
        if (N % k) return false;
        if (k == 1) return true;
        
        std::priority_queue<int, std::vector<int>, std::greater<int> > minheap;
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

            for (int i = peek; i < peek + k; ++i) {
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