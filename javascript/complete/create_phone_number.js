//Write a function that accepts an array of 10 
//integers (between 0 and 9), that returns a 
//string of those numbers in the form of a phone 
//number.
//Example:
//  createPhoneNumber([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]) 
//  returns "(123) 456-7890"
//first problem completed in javascript, this is 
//mine function, the efficiency is linear as long 
//as we will have the same number of numbers to 
//compute.
//O(10)
function createPhoneNumber(numbers) {
    if (numbers.length != 10) {
        throw new Error("the quantity of numbers have to be 10");
    }
    var phoneNumber = ""
    for (i = 0; i < numbers.length; i++) {
        if (i == 0) {
            phoneNumber += "(";
        }
        if (i == 3) {
            phoneNumber += ") ";
        }
        if (i == 6) {
            phoneNumber += "-";
        }
        if (typeof numbers[i] != "number") {
            throw new Error("all element in the array have to be numbers,\n the element at the position " + i + " is not a number");
        }
        phoneNumber += numbers[i];
    }
    return phoneNumber;
}
example = [1,2,3,4,5,6,7,8,9,0]
console.log(createPhoneNumber_codewars1(example))
/* ---other cool solutions from codewars--- */
//this is my fovourite, so intelligent
function createPhoneNumber(numbers){
    var format = "(xxx) xxx-xxxx";
    
    for(var i = 0; i < numbers.length; i++)
    {
      format = format.replace('x', numbers[i]);
    }
    
    return format;
}
//another good solution (better than mine unu)
function createPhoneNumber_codewars2(numbers){
    numbers = numbers.join('');
    return '(' + numbers.substring(0, 3) + ') ' 
        + numbers.substring(3, 6) 
        + '-' 
        + numbers.substring(6);
}
