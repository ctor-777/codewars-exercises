
/*-------------------------CODEWARS DOC-------------------------*/
//Complete the method/function so that it converts dash/underscore 
//delimited words into camel casing. The first word within the output 
//should be capitalized only if the original word was capitalized 
//(known as Upper Camel Case, also often referred to as Pascal case).
//Examples:
//  toCamelCase("the-stealth-warrior") // returns "theStealthWarrior"
//  toCamelCase("The_Stealth_Warrior") // returns "TheStealthWarrior"

/*-----------------------SOLUTION COMMENTS-----------------------*/
//here is mine solution, not really too much to add
//in this exercise i decided to not paste any codewars solution, mainly 
//because none have caught my attention

/*-------------------------USEFUL INFO---------------------------*/
//in the definitive edition i've changes some things, first i 
//added a option called pascal_case, if activated the first word 
//will be capitalized if the input is capitalized, when disabled the 
//first word will ever be lower case. I also remodev default values 
//from separators

/*--------------------------SOLUTIONS----------------------------*/

/**
 * transform a string of diferent words to camel case
 * (only is able to handle one seprator per str, but you can 
 *  put as much separators as you want to different strings)
 * @param {string} str           -the string to transform
 * @param {array} separators     -the separatos that differention berween words in the str 
 * @returns {string}
 * @see {link https://www.codewars.com/kata/517abf86da9663f1d2000003/javascript|codewars}
 */
 function toCamelCase_solution(str, separators = ["-", "_"]) {
    var caught = false;
    for (var i = 0; i < separators.length; i++) {
        if (str.includes(separators[i])){
            var splitted_str = str.split(separators[i]);
            caught = true;
            break;
        }
    }
    if (!caught){
        return str;
    }
    
    for (var i = 0; i < splitted_str.length; i++) {
        if (i > 0) {
            splitted_str[i] = splitted_str[i].slice(0,1).toUpperCase() + splitted_str[i].slice(1);
        }
    }
    return splitted_str.join("");
}
/**
 * transform a string of diferent words to camel case
 * (only is able to handle one seprator per str, but you can 
 *  put as much separators as you want to different strings)
 * @param {string} str           -the string to transform
 * @param {array} separators     -the separatos that differention berween words in the str 
 * @param {boolean} pascal_case  -defines if the first word will be or not capitalized
 * @returns {string}
 * @see {link https://www.codewars.com/kata/517abf86da9663f1d2000003/javascript|codewars}
 */
function toCamelCase(str, separators, pascal_case = false) {
    var caught = false;
    for (var i = 0; i < separators.length; i++) {
        if (str.includes(separators[i])){
            var splitted_str = str.split(separators[i]);
            caught = true;
            break;
        }
    }
    if (!caught){
        return str;
    }

    if (!pascal_case) {
        splitted_str[0] = splitted_str[0].slice(0,1).toLowerCase() + splitted_str[0].slice(1);
    }
    for (var i = 0; i < splitted_str.length; i++) {
        if (i > 0) {
            splitted_str[i] = splitted_str[i].slice(0,1).toUpperCase() + splitted_str[i].slice(1);
        }
    }
    return splitted_str.join("");
}

module.exports = toCamelCase;

