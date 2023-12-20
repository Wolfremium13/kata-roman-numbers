namespace kata_roman_numbers
{
    public class RomanNumberConverter
    {
        public static string Convert(int givenNumber)
        {
            if (givenNumber == 5)
            {
                return "V";
            }
            return givenNumber == 2 ? "II" : "I";
        }
    }
}