// https://leetcode.com/problems/convert-the-temperature

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
double* convertTemperature(double celsius, int* returnSize) {
    double kelvin = celsius + 273.15;
    double farh = (1.80 * celsius) + 32.00;
    double * array = malloc(2 * sizeof(double));
    array[0] = kelvin;
    array[1] = farh;
    *returnSize = 2;

    return array;
}