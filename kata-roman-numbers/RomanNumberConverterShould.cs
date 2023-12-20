using NUnit.Framework;

namespace kata_roman_numbers
{
    [TestFixture]
    public class RomanNumberConverterShould
    {
        [TestCase(0, "")]
        [TestCase(1, "I")]
        [TestCase(5, "V")]
        [TestCase(10, "X")]
        [TestCase(50, "L")]
        [TestCase(100, "C")]
        [TestCase(500, "D")]
        [TestCase(1000, "M")]
        public void convert_decimal_to_roman_directly(int givenNumber, string expectedRomanNumber)
        {
            Assert.That(RomanNumberConverter.Convert(givenNumber), Is.EqualTo(expectedRomanNumber));
        }

        [TestCase(3, "III")]
        [TestCase(13, "XIII")]
        [TestCase(30, "XXX")]
        [TestCase(80, "LXXX")]
        public void support_adding_until_three_repetitions_for_x_and_i(int givenNumber, string expectedRomanNumber)
        {
            Assert.That(RomanNumberConverter.Convert(givenNumber), Is.EqualTo(expectedRomanNumber));
        }
        
        [TestCase(4, "IV")]
        [TestCase(9, "IX")]
        [TestCase(14, "XIV")]
        [TestCase(19, "XIX")]
        [TestCase(40, "XL")]
        [TestCase(90, "XC")]
        [TestCase(400, "CD")]
        [TestCase(900, "CM")]
        [TestCase(1999, "MCMXCIX")]
        public void support_subtracting_until_one_repetition_from_base_one_direct_previous_unit(int givenNumber, string expectedRomanNumber)
        {
            Assert.That(RomanNumberConverter.Convert(givenNumber), Is.EqualTo(expectedRomanNumber));
        }
        
        [TestCase(555, "DLV")]
        public void cannot_repeat_base_five_symbols(int givenNumber, string expectedRomanNumber)
        {
            Assert.That(RomanNumberConverter.Convert(givenNumber), Is.EqualTo(expectedRomanNumber));
        }
    }
}