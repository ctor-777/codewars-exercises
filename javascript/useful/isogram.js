/*-------------------------CODEWARS DOC-------------------------*/

//An isogram is a word that has no repeating letters, consecutive or 
//non-consecutive. Implement a function that determines whether a string 
//that contains only letters is an isogram. Assume the empty string is an 
//isogram. Ignore letter case.

//isIsogram("Dermatoglyphics") == true
//isIsogram("aba") == false
//isIsogram("moOse") == false // -- ignore letter case

/*-----------------------SOLUTION COMMENTS-----------------------*/

//mine solution (isIsogram) makes the work, bit is imporvable.
//the codewars solution (isIsogram_codewars) is cleaner than mine, 
//in this solution set makes all the hard work, it stores only the non
//repeated valued, this why if the quantity of non repeated values is 
//equal to the quantity of values we know that there isn't repeated values.

/*--------------------------SOLUTIONS----------------------------*/

/**
 * determines if an input string is or not and isogram (old)
 * @param {string} str               -the string to determine
 * @param {boolean} ignoreUpperCase  -ignores upper and lower case
 * @returns {boolean} 
 */
function isIsogram(str, ignoreUpperCase = true) {
    if (ignoreUpperCase){
        str = str.toLowerCase();
    }
    var past_letters = [];
    for (i = 0; i < str.length; i++) {
        if (past_letters.includes(str[i])) {
            return false;
        } 
        past_letters.push(str[i]);
    }
    return true;
}



/**
 * determines if an input string is or not and isogram
 * @param {string} str               -the string to determine
 * @param {boolean} ignoreUpperCase  -ignores upper and lower case
 * @returns {boolean} 
 */
function isIsogram_2(str, ignoreUpperCase = true) {
    if (ignoreUpperCase){
        str = str.toLowerCase();
    }
    var unrepeated = new Set(str);
    return unrepeated.size == str.length;
}

/**
 * determines if an input string is or not and isogram (codewars solution)
 * @param {string} str               -the string to determine
 * @param {boolean} ignoreUpperCase  -ignores upper and lower case
 * @returns {boolean} 
 */
function isIsogram_codewars(str){
    return new Set(str.toUpperCase()).size == str.length;;
}

module.exports = isIsogram_2;