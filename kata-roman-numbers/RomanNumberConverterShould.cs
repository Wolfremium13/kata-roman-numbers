using NUnit.Framework;

namespace kata_roman_numbers
{
    [TestFixture]
    public class RomanNumberConverterShould
    {
        [Test]
        public void convert_decimal_to_roman()
        {
            Assert.That(RomanNumberConverter.Convert(1), Is.EqualTo("I"));
            Assert.That(RomanNumberConverter.Convert(2), Is.EqualTo("II"));
            Assert.That(RomanNumberConverter.Convert(5), Is.EqualTo("V"));
        }
    }
}