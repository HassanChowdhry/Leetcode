// https://leetcode.com/problems/minimum-number-of-moves-to-seat-everyone

// #pragma GCC optimize("O3, unroll-loops")
#pragma GCC optimize("Ofast,unroll-loops")
#pragma GCC target("avx2,tune=native")
class Solution {
public:
    int minMovesToSeat(vector<int>& s1, vector<int>& s2) {
        sort(s1.begin(), s1.end());
        sort(s2.begin(), s2.end());
        int res = 0;
        for (int i = 0; i < s1.size(); ++i) {
            res += abs(s1[i] - s2[i]);
        }
        return res;
    }
};