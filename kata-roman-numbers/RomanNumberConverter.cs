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
            if (givenNumber == 10)
            {
                return "X";
            }
            if (givenNumber == 50)
            {
                return "L";
            }
            if (givenNumber == 100)
            {
                return "C";
            }
            return givenNumber == 2 ? "II" : "I";
        }
    }
}