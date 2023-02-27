// You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer. The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain any leading 0's.

// Increment the large integer by one and return the resulting array of digits.

// Example 1:

// Input: digits = [1,2,3]
// Output: [1,2,4]
// Explanation: The array represents the integer 123.
// Incrementing by one gives 123 + 1 = 124.
// Thus, the result should be [1,2,4].
// Example 2:

// Input: digits = [4,3,2,1]
// Output: [4,3,2,2]
// Explanation: The array represents the integer 4321.
// Incrementing by one gives 4321 + 1 = 4322.
// Thus, the result should be [4,3,2,2].
// Example 3:

// Input: digits = [9]
// Output: [1,0]
// Explanation: The array represents the integer 9.
// Incrementing by one gives 9 + 1 = 10.
// Thus, the result should be [1,0].

// Constraints:

// 1 <= digits.length <= 100
// 0 <= digits[i] <= 9
// digits does not contain any leading 0's.

var plusOne = function(digits) {
    let end = digits.length-1 // let end be the last index of the array of digits
    digits[end] += 1 // increase the digit in the last index by one
    
    while (digits[end] > 9 ){ // loop runs while last digit greater than 9 (ie is 10 and needs to carry over)
        digits[end] = 0; // set current digit to 0
        end--; // move to next digit (in order to "carry the one")
        if (end < 0){ // if end is less than zero, we need to add an index at front with a 1
            return [1, ...digits] // makes a new array with 1 and then everything in digits
        }
        else { //otherwise
            digits[end] += 1 // we carry the one
        }
    }
    return digits
};