function SolveEuler17() {
	return AllNumberNames(1000);
}

function AllNumberNames(N) {
	let numberString = "";
	for (let i = 1; i <= N; i++) {
		numberString += NumberName(i) + ", ";
	}
	let modifiedNumberString = numberString.replace(/-/g, "");
	modifiedNumberString = modifiedNumberString.replace(/,/g, "");
	modifiedNumberString = modifiedNumberString.replace(/ /g, "");
	modifiedNumberString.trim();
	return modifiedNumberString.length;
}

function NumberName(N) {
	let digits = [];
	let numberString = "";
	digits = SplitNumber(N);
	if (N <= 19) {
		numberString = SingleDigits(N);
	} else if (N < 100) {
		numberString = DoubleDigits(digits[0]) + " ";
		if (digits[1] > 0) {
			numberString += SingleDigits(digits[1]);
		}
	} else if (N < 1000) {
		numberString += TrippleDigits(digits[0]);
		if (TwoDigitsToNumber(digits[1], digits[2]) > 0) {
			numberString += " and ";
			if (TwoDigitsToNumber(digits[1], digits[2]) > 19) {
				numberString += DoubleDigits(digits[1]);
				if (digits[2] > 0) {
					numberString += " ";
					numberString += SingleDigits(digits[2]);
				}
			} else {
				numberString += SingleDigits(
					TwoDigitsToNumber(digits[1], digits[2])
				);
			}
		}
	} else if (N == 1000) {
		return "thousand";
	}

	return numberString;
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
		case 13:
			return "thirteen";
		case 14:
			return "fourteen";
		case 15:
			return "fifteen";
		case 16:
			return "sixteen";
		case 17:
			return "seventeen";
		case 18:
			return "eighteen";
		case 19:
			return "nineteen";
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

console.log(NumberName(1));
console.log(AllNumberNames(5));
console.log(SolveEuler17());

//Below this line javascript code is irrelevant to the assignment
//The code is only used to enhance the website

const numberInput = document.querySelector(".numberInput");
const numberName = document.querySelector(".NumberName");
const allNumberNames = document.querySelector(".AllNumberNames");
const solveEuler = document.querySelector(".SolveEuler17");

numberInput.addEventListener("input", (e) => {
	numberName.value = NumberName(parseInt(numberInput.value));
	allNumberNames.value = AllNumberNames(parseInt(numberInput.value));
	solveEuler.value = SolveEuler17();
});
