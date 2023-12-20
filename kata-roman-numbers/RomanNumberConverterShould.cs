﻿using NUnit.Framework;

namespace kata_roman_numbers
{
    [TestFixture]
    public class RomanNumberConverterShould
    {
        [Test]
        public void convert_decimal_to_roman()
        {
            Assert.That(RomanNumberConverter.Convert(0), Is.EqualTo(""));
            Assert.That(RomanNumberConverter.Convert(1), Is.EqualTo("I"));
            Assert.That(RomanNumberConverter.Convert(5), Is.EqualTo("V"));
            Assert.That(RomanNumberConverter.Convert(10), Is.EqualTo("X"));
            Assert.That(RomanNumberConverter.Convert(50), Is.EqualTo("L"));
            Assert.That(RomanNumberConverter.Convert(100), Is.EqualTo("C"));
            Assert.That(RomanNumberConverter.Convert(500), Is.EqualTo("D"));
            Assert.That(RomanNumberConverter.Convert(1000), Is.EqualTo("M"));
        }
        
        [Test]
        public void support_adding_until_three_repetitions()
        {
            Assert.That(RomanNumberConverter.Convert(2), Is.EqualTo("II"));
            Assert.That(RomanNumberConverter.Convert(3), Is.EqualTo("III"));
            Assert.That(RomanNumberConverter.Convert(6), Is.EqualTo("VI"));
            Assert.That(RomanNumberConverter.Convert(7), Is.EqualTo("VII"));
            Assert.That(RomanNumberConverter.Convert(8), Is.EqualTo("VIII"));
            Assert.That(RomanNumberConverter.Convert(11), Is.EqualTo("XI"));
            Assert.That(RomanNumberConverter.Convert(12), Is.EqualTo("XII"));
            Assert.That(RomanNumberConverter.Convert(13), Is.EqualTo("XIII"));
            Assert.That(RomanNumberConverter.Convert(80), Is.EqualTo("LXXX"));
        }
    }
}