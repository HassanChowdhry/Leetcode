// https://leetcode.com/problems/convert-the-temperature

const convertTemperature = function(celsius) {
    return [celsius + 273.15, (celsius * 1.8) + 32]
}