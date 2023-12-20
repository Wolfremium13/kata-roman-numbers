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
            if (givenNumber == 5)
                return "V";
            if (givenNumber == 10)
                return "X";
            if (givenNumber == 50)
                return "L";
            if (givenNumber == 100)
                return "C";
            if (givenNumber == 500)
                return "D";
            if (givenNumber == 1000)
                return "M";
            return "";
        }
    }
}