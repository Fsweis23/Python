/* 
    Given a string,
    return a new string with the duplicate characters excluded
    Bonus: Keep only the last instance of each character.
*/

const str1 = "abcABCabcABCabcABC";
const expected1 = "abcABC";

const str2 = "helloo";
const expected2 = "helo";

const str3 = "";
const expected3 = "";

const str4 = "aa";
const expected4 = "a";

//bonus
const str5 = "aba"
const expected5 = "ba"

/**
 * De-dupes the given string.
 * - Time: O(?).
 * - Space: O(?).
 * @param {string} str A string that may contain duplicates.
 * @returns {string} The given string with any duplicate characters removed.
 */
    function stringDedupe(str) {
  //Your code here

  // first code
    function stringDedupe(str) {
        var newstr=''
        var dict={}
        for(i of str){
            if(!dict.hasOwnProperty(i)){
                dict[i]=true
                newstr+=i
            }
        }
        return newstr
    }

  // second code
    function stringDedupe(str) {
    var newstr=''
    var dict={}
    for(i of str){
        if(!dict.hasOwnProperty(i)){
            dict[i]=true
            newstr+=i
        }
    }
    return newstr
}
}

console.log(stringDedupe(str1));
console.log(stringDedupe(str2));
console.log(stringDedupe(str3));
console.log(stringDedupe(str4));
console.log(stringDedupe(str5));

/*****************************************************************************/

/* 
    Given a string containing space separated words
    Reverse each word in the string.
    If you need to, use .split to start, then try to do it without.
*/

const strA = "hello";
const expectedA = "olleh";

const strB = "hello world";
const expectedB = "olleh dlrow";

const strC = "abc def ghi";
const expectedC = "cba fed ihg";

/**
 * Reverses the letters in each words in the given space separated
 * string of words. Does NOT reverse the order of the words themselves.
 * - Time: O(?).
 * - Space: O(?).
 * @param {string} str Contains space separated words.
 * @returns {string} The given string with each word's letters reversed.
 */
function reverseWords(str) {
    //Your code here
    function reverseWords(str) {
        // Turn str into an array of strings
        let strArray = str.split(" ");
        // Loop through list of strings
        for (var i = 0; i < strArray.length; i++) {
            // Reverse each string
            let reversed = "";
            for (let char of strArray[i]) {
                reversed = char + reversed
            }
            // Replace word with reversed version
            strArray[i] = reversed;
        }
        // Join list of strings together
        return strArray.join(" "); 
    }
}

console.log(reverseWords(strA)) //expectedA: olleh
console.log(reverseWords(strB)) //expectedB: olleh dlrow
console.log(reverseWords(strC)) //expectedC: cba fed ihg

// function reverseWordsSplit(wordsStr) {
//     const words = wordsStr.split(" ");
//     let wordsReversed = "";

//     for (const word of words) {
//         let reversedWord = "";

//         for (let i = word.length - 1; i >= 0; --i) {
//             reversedWord += word[i];
//         }

//         // add a space in front of word if it's not the first word
//         if (wordsReversed.length > 0) {
//             reversedWord = " " + reversedWord;
//         }
//         wordsReversed += reversedWord;
//     }
//     return wordsReversed;
// }

// function reverseWords(str) {
//     let reversed = "";
//     let temp = ""
//     for (let char of str){
//         if (char === " "){
//             reversed += temp + " "
//             temp = ""
//         } else {
//             temp = char + temp
//         }
//     }
//     //capture last word
//     reversed += temp;
//     return reversed
// }