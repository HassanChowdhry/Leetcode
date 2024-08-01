// https://leetcode.com/problems/fizz-buzz

class Solution {
    public List<String> fizzBuzz(int n) {
        List<String> res = new ArrayList<String>();
        for (int i = 1; i <= n; i++) {
            boolean isDivisibleBy3 = i % 3 == 0;
            boolean isDivisibleBy5 = i % 5 == 0;
            if (isDivisibleBy3 && isDivisibleBy5) {
                res.add("FizzBuzz");
            } else if (isDivisibleBy3) {
                res.add("Fizz");
            } else if (isDivisibleBy5) {
                res.add("Buzz");
            } else res.add(String.valueOf(i));
        }
        return res;
    }
}