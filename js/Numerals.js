var values = new Array();
values["M"] = 1000;
values["D"] = 500;
values["C"] = 100;
values["L"] = 50;
values["X"] = 10;
values["V"] = 5;
values["I"] = 1;

var convertFromRomanNumeral = function (roman) {
	var total = 0;
	var lastValue = 0;
	var repeatcount = 0;

	for (var i = 0; i < roman.length; i++) {
		var thisValue = values[roman[i]];
		var maxRepeatCount = getMaxRepeatCount(thisValue);

		if (thisValue === lastValue) repeatcount++;
		else repeatcount = 1;
		if (repeatcount > maxRepeatCount) throw new Error("Invalid")

		total += thisValue;
		if (thisValue > lastValue)
			total -= (2 * lastValue);

		lastValue = thisValue;
	};
	return total;
};

var getMaxRepeatCount = function(value) {
	if ((value === 5) || (value === 50) || (value === 500))
		return 1;
	return 4;
};
