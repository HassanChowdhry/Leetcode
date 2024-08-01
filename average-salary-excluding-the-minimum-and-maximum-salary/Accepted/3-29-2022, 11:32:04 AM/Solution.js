// https://leetcode.com/problems/average-salary-excluding-the-minimum-and-maximum-salary

/**
 * @param {number[]} salary
 * @return {number}
 */
var average = function(salary) {
   let max = salary[0];
  let min = salary[0];
  let totalSalary = 0;
  let numOfEmployees = salary.length - 2;

  for (let i = 0; i < salary.length; i++) {
    
    totalSalary += salary[i];
    max = Math.max(max, salary[i]);
    min = Math.min(min, salary[i]);
  }

  totalSalary -= (max + min);
  let avg = (totalSalary / numOfEmployees);

  return avg;
}
