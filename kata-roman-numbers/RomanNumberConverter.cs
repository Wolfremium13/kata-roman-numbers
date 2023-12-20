using System.Collections.Generic;

namespace kata_roman_numbers
{
    public class RomanNumberConverter
    {
        public static string Convert(int givenNumber)
        {
            if (givenNumber == 0)
            {
                return "";
            }

            if (givenNumber < 4)
            {
                return "I" + Convert(givenNumber - 1);
            }

            if (givenNumber > 5 && givenNumber < 9)
            {
                return "V" + Convert(givenNumber - 5);
            }

            if (givenNumber > 10 && givenNumber < 14)
            {
                return "X" + Convert(givenNumber - 10);
            }

            return GetRomanNumber(givenNumber);
        }

        private static string GetRomanNumber(int givenNumber)
        {
            var romanNumbersMap = new Dictionary<int, string>
            {
                { 1, "I" },
                { 5, "V" },
                { 10, "X" },
                { 50, "L" },
                { 100, "C" },
                { 500, "D" },
                { 1000, "M" }
            };
            return romanNumbersMap.TryGetValue(givenNumber, out var romanNumber) ? romanNumber : "";
        }
    }
}