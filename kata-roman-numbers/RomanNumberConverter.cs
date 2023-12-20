using System.Collections.Generic;

namespace kata_roman_numbers
{
    public class RomanNumberConverter
    {
        private static readonly Dictionary<int, string> DecimalToRoman = new Dictionary<int, string>
        {
            { 1000, "M" },
            { 500, "D" },
            { 100, "C" },
            { 50, "L" },
            { 10, "X" },
            { 5, "V" },
            { 1, "I" }
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