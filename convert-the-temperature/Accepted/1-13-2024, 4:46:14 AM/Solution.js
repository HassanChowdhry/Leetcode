// https://leetcode.com/problems/convert-the-temperature

const results={};
function convertTemperature(celsius) {
    if (!results[celsius]) {
        results[celsius] = [celsius + 273.15, celsius * 1.8 + 32.0];
    }
    return results[celsius];
};