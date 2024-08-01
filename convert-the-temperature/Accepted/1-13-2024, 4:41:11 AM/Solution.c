// https://leetcode.com/problems/convert-the-temperature

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
double* convertTemperature(double celsius, int* returnSize) {
    double * array = malloc(2 * sizeof(double));
    array[0] = celsius + 273.15;
    array[1] = (1.80 * celsius) + 32.00;
    *returnSize = 2;

    return array;
}