// https://leetcode.com/problems/minimum-number-of-moves-to-seat-everyone

#pragma GCC optimize("O3, unroll-loops")
class Solution {
public:
    int minMovesToSeat(vector<int>& s1, vector<int>& s2) {
        sort(s1.begin(), s1.end());
        sort(s2.begin(), s2.end());

        int N = s1.size();

        int res = 0;
        
        for (int i = 0; i < N; ++i) {
            res += abs(s1[i] - s2[i]);
        }

        return res;
    }
};