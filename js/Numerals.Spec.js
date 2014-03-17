describe("converts roman numerals to integer", function () {

    all("conerts standalone numerals", [ 
	    	["I", 1],
	    	["II", 2],
	    	["III",3],
	    	["V", 5],
	    	["X", 10],
	    	["L", 50],
	    	["C", 100],
	    	["D", 500],
	    	["M", 1000],

	    	], function (romanNumeral, expectedValue) {

    	var output = convertFromRomanNumeral(romanNumeral);
        expect(output).toBe(expectedValue);
    });

    all("converts simple repetitions to additions", [ 
	    	["I", 1],
	    	["II", 2],
	    	["III", 3],
	    	["XX", 20],
	    	["XXX", 30],
	    	["CC", 200],
	    	["CCC", 300],
	    	["MM", 2000],
	    	["MMM", 3000]

	    	], function (romanNumeral, expectedValue) {

    	var output = convertFromRomanNumeral(romanNumeral);
        expect(output).toBe(expectedValue);
    });

    all("repetitions up to next value throws error",
    		["IIIII", "VV", "XXXXX", "LL", "CCCCC", "DD" ]
    	, function (romanNumeral){
    		expect(function() {convertFromRomanNumeral(romanNumeral)})
    			.toThrow(new Error("Invalid"));
    	});

    all("subsequent lower values are added", [ 
	    	["VI", 6],
	    	["VII", 7],
	    	["XI", 11],
	    	["XVI", 16],
	
	    	], function (romanNumeral, expectedValue) {

    	var output = convertFromRomanNumeral(romanNumeral);
        expect(output).toBe(expectedValue);
    });

    all("handles subtractive notation", [ 
	    	["IV", 4],
	    	["IX", 9],
	    	["XL", 40],
	    	["XC", 90],
	    	["XD", 490],
	    	["CM", 900],
	
	    	], function (romanNumeral, expectedValue) {

    	var output = convertFromRomanNumeral(romanNumeral);
        expect(output).toBe(expectedValue);
    });

    all("examples", [
	    	["XIV", 14],
	    	["MCM", 1900],
	
	    	], function (romanNumeral, expectedValue) {

    	var output = convertFromRomanNumeral(romanNumeral);
        expect(output).toBe(expectedValue);
    });
});
