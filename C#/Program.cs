using System;

namespace HelloWorld
{
  class Program
    {
/*        static void Main(string[] args)
        {   
            string[] price = {"5 gold",       "10 gold",     "13 gold", "17 gold", "20 gold"};
            string[] items = {{"Short sword ", "Long sword ", "Mace ",   "Flail ",  "Waraxe "},{"5 gold", "10 gold", "13 gold", "17 gold", "20 gold"}};


            foreach (string name in items){
                Console.WriteLine(name);
            }
        }*/
// Short sword                    5 gold
// Long sword                    10 gold
// Mace                          13 gold
// Flail                         17 gold
// Waraxe                        20 gold
/*        static void Main(string[] args)
        {
            string[] row1 = {"0", "0", "0"};
            string[] row2 = {"0", "0", "0"};
            string[] row3 = {"0", "0", "0"};
            Console.WriteLine($"{row1[0]} {row1[1]} {row1[2]}");
            Console.WriteLine($"{row2[0]} {row2[1]} {row2[2]}");
            Console.WriteLine($"{row3[0]} {row3[1]} {row3[2]}");
            Console.WriteLine("Which position would you like to change?");
            Console.WriteLine("Input column number");
            int x = Convert.ToInt32(Console.ReadLine()) - 1;
            Console.WriteLine("Input row number");
            int y = Convert.ToInt32(Console.ReadLine());
            Console.WriteLine("Input the new content");
            switch (y)
            {
                case 1:
                    row1[x] = Console.ReadLine();
                    break;
                case 2:
                    row2[x] = Console.ReadLine();
                    break;
                case 3:
                    row3[x] = Console.ReadLine();
                    break;
            }
            Console.WriteLine($"{row1[0]} {row1[1]} {row1[2]}");
            Console.WriteLine($"{row2[0]} {row2[1]} {row2[2]}");
            Console.WriteLine($"{row3[0]} {row3[1]} {row3[2]}");*/
/*        static void Main(string[] args)
        {
            Random rnd = new Random();
            int ai_choice = rnd.Next(0,3);
            string ai_choicestr = "x";
            int your_choice = 0;
            string your_choicestr = "x";

            Console.WriteLine("Make your choice by typing in \"1\" for rock, \"2\" for paper or \"3\" for scissors");
            your_choice = Console.ReadLine();
            
            if (ai_choice == 0){
                ai_choicestr = "rock";
                }
            else if (ai_choice == 1){
                ai_choicestr = "paper";
            }
            else {
                ai_choicestr = "scissors";
            }
            if (your_choice == 0){
                your_choicestr = "rock";
                }
            else if (your_choice == 1){
                your_choicestr = "paper";
            }
            else {
                your_choicestr = "scissors";
            }
            
            Console.WriteLine($"You chose {your_choicestr}");
            Console.WriteLine($"Your opponent chose {ai_choicestr}");
            if (your_choice == ai_choicestr){
                Console.WriteLine("You draw");
            }
            if (your_choice == 0){
                if (ai_choice == 1){
                    Console.WriteLine("You Lose");
                }
                else if (ai_choice == 2){
                    Console.WriteLine("You Win");
                }
            if (your_choice == 1){
                if (ai_choice == 2){
                    Console.WriteLine("You Lose");
                }
                else if (ai_choice == 0){
                    Console.WriteLine("You Win");
                }
            }
            if (your_choice == 2){
                if (ai_choice == 0){
                    Console.WriteLine("You Lose");
                }
                else if (ai_choice == 1){
                    Console.WriteLine("You Win");
                }
            }
            }
        }*/
        static void Main(string[] args){

            Console.WriteLine("am working");
            
        }
    }
}