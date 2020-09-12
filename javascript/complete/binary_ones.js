/*-------------------------CODEWARS DOC-------------------------*/

//Write a function that takes an integer as input, and 
//returns the number of bits that are equal to one in 
//the binary representation of that number. You can 
//guarantee that input is non-negative.

//Example: 
//  The binary representation of 1234 is 10011010010, 
//  so the function should return 5 in this case

function frequency(arr) {
    var values = {}
    for (var i = 0; i < arr.length; i++) {
        if (values[arr[i]] == undefined) {
            values[arr[i]] = 0;
        } 
        values[arr[i]] += 1;
    }

    return values;
}

function countBits(n) {
    n = Math.abs(n)
    var binari_arr = n.toString(2).split("");
    return frequency(binari_arr)["1"];
}

function countBits_solution1(n) {
    var binari_arr = n.toString(2);
    var number_of_ones = 0;
    for (var i = 0; i < binari_arr.length; i++) {
        if (binari_arr[i] == 1) {
            number_of_ones += 1;
        }
    }

    return number_of_ones;
}

function countBits_solution2(n) {
    var binari_arr = n.toString(2);
    var number_of_ones = 0;
    for (var i = 0; i < binari_arr.length; i++) {
        number_of_ones += parseInt(binari_arr[i])
    }

    return number_of_ones;
}

function countBits_solution_codewars(n) {
    return n.toString(2).split("0").join("").length
}