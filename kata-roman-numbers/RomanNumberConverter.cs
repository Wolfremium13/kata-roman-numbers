namespace kata_roman_numbers
{
    public class RomanNumberConverter
    {
        public static string Convert(int givenNumber)
        {
            return givenNumber == 2 ? "II" : "I";
        }
    }
}