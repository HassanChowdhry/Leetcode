// https://leetcode.com/problems/convert-the-temperature

function convertTemperature(celsius) {
    return [celsius + 273.15, (celsius * 1.8) + 32]
}