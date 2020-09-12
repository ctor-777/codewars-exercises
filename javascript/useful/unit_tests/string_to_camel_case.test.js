var toCamelCase = require("../string_to_camel_case");

const separators = ["-", "_"];
const test_0 = "";
const test_1 = "";
const test_2 = "";
const test_3 = "";
const test_4 = "";
const test_5 = "";

test("the_stealth_warrior is theStealthWarrior", () => {
    expect(toCamelCase("the_stealth_warrior", separators)).toBe("theStealthWarrior");
})

test("the_stealth_warrior is theStealthWarrior when pascal case is true", () => {
    expect(toCamelCase("the_stealth_warrior", separators, true)).toBe("theStealthWarrior");
})

test("The_stealth_warrior is TheStealthWarrior when pascal case is true", () => {
    expect(toCamelCase("The_stealth_warrior", separators, true)).toBe("TheStealthWarrior");
})

test("The_stealth_warrior is theStealthWarrior when pascal case is false (default)", () => {
    expect(toCamelCase("The_stealth_warrior", separators)).toBe("theStealthWarrior");
})



test("the-stealth-warrior is theStealthWarrior", () => {
    expect(toCamelCase("the-stealth-warrior", separators)).toBe("theStealthWarrior");
})

test("the-stealth-warrior is theStealthWarrior when pascal case is true", () => {
    expect(toCamelCase("the-stealth-warrior", separators, true)).toBe("theStealthWarrior");
})

test("The-stealth-warrior is TheStealthWarrior when pascal case is true", () => {
    expect(toCamelCase("The-stealth-warrior", separators, true)).toBe("TheStealthWarrior");
})

test("The-stealth-warrior is theStealthWarrior when pascal case is false (default)", () => {
    expect(toCamelCase("The-stealth-warrior", separators)).toBe("theStealthWarrior");
})



test("handle ampty values", () => {
    expect(toCamelCase("", separators)).toBe("");
})
