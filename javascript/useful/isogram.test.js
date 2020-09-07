var isIsogram = require("./isogram");
const { exportAllDeclaration } = require("@babel/types");

const test_0 = "isogram";
const test_1 = "aba";
const test_2 = "hello";
const test_3 = "moOse";
const test_4 = "";

test('isogram is a isogram, should return true', () => {
    expect(isIsogram(test_0)).toBe(true);
});

test('aba is not a isogram, should return false', () => {
    expect(isIsogram(test_1)).toBe(false);
});

test('hello is not a isogram, should return false', () => {
    expect(isIsogram(test_2)).toBe(false);
});

test('shouldn\'t differentiate between upper and lower when is not defined', () => {
    expect(isIsogram(test_3)).toBe(false);
});

test('should differentiate between upper and lower when is defined', () => {
    expect(isIsogram(test_3, false)).toBe(true);
});

test('an empty array is an acceptable isogram', () => {
    expect(isIsogram(test_4)).toBe(true);
});
