using System.Collections.Generic;

namespace kata_roman_numbers
{
    public class RomanNumberConverter
    {
        private static readonly Dictionary<int, string> DecimalToRoman = new Dictionary<int, string>
        {
            { 1000, "M" },
            { 900, "CM" },
            { 500, "D" },
            { 400, "CD" },
            { 100, "C" },
            { 90, "XC" },
            { 50, "L" },
            { 40, "XL" },
            { 10, "X" },
            { 9, "IX" },
            { 5, "V" },
            { 4, "IV" },
            { 1, "I" },
        };

        public static string Convert(int givenNumber)
        {
            var romanNumber = string.Empty;
            var enumerator = DecimalToRoman.GetEnumerator();
            while (enumerator.MoveNext())
            {
                var roman = enumerator.Current.Value;
                while (givenNumber >= enumerator.Current.Key)
                {
                    romanNumber += roman;
                    givenNumber -= enumerator.Current.Key;
                }
            }

            return romanNumber;
        }
    }
}