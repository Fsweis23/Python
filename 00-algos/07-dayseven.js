/* 
    Given an array of strings
    return the number of times each string occurs (a frequency / hash table)
*/

const arr1 = ["a", "a", "a"];
const expected1 = {
    a: 3,
};

const arr2 = ["a", "b", "a", "c", "B", "c", "c", "d"];
const expected2 = {
    a: 2,
    b: 1,
    c: 3,
    B: 1,
    d: 1,
};

const arr3 = [];
const expected3 = {};

/**
 * Builds a frequency table based on the given array.
 * - Time: O(?).
 * - Space: O(?).
 * @param {Array<string>} arr
 * @returns {Object<string, number>} A frequency table where the keys are items
 *    from the given arr and the values are the amnt of times that item occurs.
 *  Possible hint: .hasOwnProperty() <- Don't know it? Google it as a group!
 */
    function makeFrequencyTable(arr) {
    //Your code here
}

function makeFrequencyTable(arr) {
    let freq = {};
    for (let elem of arr){
        freq.hasOwnProperty(elem) ? freq[elem]++ : freq[elem] = 1;
        //  condition             ?  if true     :    if false
        /*
        if (freq.hasOwnProperty(elem)){
            freq[elem]++
        } else {
            freq[elem] = 1
        }
        */
    }
    return freq;
}


function oddOccurrencesInArray(nums) {
    //Your code here
    let freq = makeFrequencyTable(nums);
    for (let key in freq){
        if (freq[key] % 2 !== 0){
            return parseInt(key);
        }
    }
    return false;
}

console.log(makeFrequencyTable(arr1)) 
console.log("Expected: ", expected1);
console.log(makeFrequencyTable(arr2)) 
console.log("Expected: ", expected2);
console.log(makeFrequencyTable(arr3))
console.log("Expected: ", expected3);

/* 
Given a non-empty array of odd length containing ints where every int but one
has a matching pair (another int that is the same)
return the only int that has no matching pair.
*/

const numsA = [1];
const expectedA = 1;

const numsB = [5, 4, 5];
const expectedB = 4;

const numsC = [5, 4, 3, 4, 3, 4, 5];
const expectedC = 4; // there is a pair of 4s but one 4 has no pair.

const numsD = [5, 2, 6, 2, 3, 1, 6, 3, 2, 5, 2];
const expectedD = 1;

function oddOccurrencesInArray(nums) {
    //Your code here
}

function makeFrequencyTable(arr) { 
    let table = {}
    for (let elem of arr){
      // if (table.hasOwnProperty(elem)){
      //   table[elem]+= 1
      // } else {
      //   table[elem] = 1
      // }
    table.hasOwnProperty(elem) ? table[elem]++ : table[elem] = 1
      // condition               ?  if true      : if false
    }
    return table
}

function oddOccurrencesInArray(nums) {
    // Initialize frequency table object
    let object = makeFrequencyTable(nums);
    // Iterate through frequency table
    for (var key in object) {
        // Check if value is odd number
        if (object[key] % 2 != 0) {
            // Return key
            return key;
        }
    }
}

console.log(oddOccurrencesInArray(numsA), "should equal", expectedA);
console.log(oddOccurrencesInArray(numsB), "should equal", expectedB);
console.log(oddOccurrencesInArray(numsC), "should equal", expectedC);
console.log(oddOccurrencesInArray(numsD), "should equal", expectedD);