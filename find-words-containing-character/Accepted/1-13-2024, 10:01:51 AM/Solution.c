// https://leetcode.com/problems/find-words-containing-character

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* findWordsContaining(char** words, int wordsSize, char x, int* returnSize) {
    int* res = (int*) malloc(wordsSize * sizeof(int));
    int currSize = 0;

    for (int i = 0; i < wordsSize; ++i) {
        for (int j = 0; j < strlen(words[i]); ++j) {
            if (words[i][j] == x) {
                res[currSize] = i;
                currSize++;
                break;
            }
        }
    }

    *returnSize = currSize;
    return res;
}