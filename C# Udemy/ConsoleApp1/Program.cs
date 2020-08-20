using Microsoft.VisualBasic.CompilerServices;
using System;


namespace ConsoleApp1
{
    class Program
    {
        enum Days
        {
            Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday
        }

        static void Main(string[] args)
        {
            Console.WriteLine(Add2(5, 6));
            Add();
        }

        static void Add()
        {
            Console.WriteLine("Added!");
        }

        static int Add2(int number1, int number2)
        {
            return number1 + number2;
        }
    }
}