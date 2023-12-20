namespace kata_roman_numbers
{
    public class RomanNumberConverter
    {
        public static string Convert(int givenNumber)
        {
            switch (givenNumber)
            {
                case 1:
                    return "I";
                case 2:
                    return "II";
                case 3:
                    return "III";
                case 5:
                    return "V";
                case 10:
                    return "X";
                case 50:
                    return "L";
                case 100:
                    return "C";
                case 500:
                    return "D";
                case 1000:
                    return "M";
                default:
                    return "";
            }
        }
    }
}