function NumberName(N) {
	let digits = [];
	digits = SplitNumber(N);
	if (N <= 12) {
		return SingleDigits(N);
	} else if (N < 100) {
		return DoubleDigits(digits[0]) + " " + SingleDigits(digits[1]);
	} else if (N < 1000) {
		if (TwoDigitsToNumber(digits[1], digits[2]) > 12) {
			return (
				TrippleDigits(digits[0]) +
				" and " +
				DoubleDigits(digits[1]) +
				" " +
				SingleDigits(digits[2])
			);
		} else {
			return (
				TrippleDigits(digits[0]) +
				" and " +
				SingleDigits(TwoDigitsToNumber(digits[1], digits[2]))
			);
		}
	} else if (N == 1000) {
		return "thousand";
	}
}

function TwoDigitsToNumber(one, two) {
	return parseInt(String(one).concat(two));
}

//Split number into an array of digits
function SplitNumber(inputNumber) {
	output = [];
	number = inputNumber.toString();
	for (var i = 0, len = number.length; i < len; i += 1) {
		output.push(+number.charAt(i));
	}
	return output;
}

function SingleDigits(N) {
	switch (N) {
		case 0:
			return "zero";
		case 1:
			return "one";
		case 2:
			return "two";
		case 3:
			return "three";
		case 4:
			return "four";
		case 5:
			return "five";
		case 6:
			return "six";
		case 7:
			return "seven";
		case 8:
			return "eight";
		case 9:
			return "nine";
		case 10:
			return "ten";
		case 11:
			return "eleven";
		case 12:
			return "twelve";
		default:
			return "error";
	}
}

function DoubleDigits(N) {
	switch (N) {
		case 2:
			return "twenty";
		case 3:
			return "thirty";
		case 4:
			return "fourty";
		case 5:
			return "fifty";
		case 6:
			return "sixty";
		case 7:
			return "seventy";
		case 8:
			return "eighty";
		case 9:
			return "ninety";
	}
}

function TrippleDigits(N) {
	return SingleDigits(N) + "-hundred";
}

console.log(NumberName(112));
