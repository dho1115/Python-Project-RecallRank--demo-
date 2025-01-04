from time import sleep;
from colorama import init;
from termcolor import colored;
from apis import WordGenerator;

init();

score = 0;

def Greeting():   
   Greeting = "Welcome to Recall Rank!!!"
   Border = "*"*(len(Greeting) + 5);
   print(colored(f"{Border}\n  {Greeting}  \n{Border}", color="light_green", attrs=["bold"]));
   sleep(1);
   print("A word will appear for 1 second...");
   sleep(1);
   print(colored("THEN DISAPPEAR!!!", color='red', attrs=['bold']));
   sleep(1);
   print("You will then be asked to guess what that word is.");

def Game():
   global score;
   word = WordGenerator()[0]
   for i in range(1):
      print(word, end="\r"); #\r returns the cursor to the beginning of the word.
      sleep(1);
      message = colored("WHAT WAS THAT WORD???", color='red', on_color='on_yellow', attrs=['bold']);
      print(message + " "*len(word))
   
   guess = input("ENTER YOUR GUESS HERE (words are case-sensitive)!!! => ");
   if guess == word:
      score+= len(word);
      return f"CORRECT!!! Your score has been INCREASED by {len(word)} and is now {colored(score, color='red' if score<0 else 'light_green', attrs=['bold'])}!!!"
   else:
      score-=len(word);
      return f"WRONG!!! {guess} was NOT the correct word which was, {word}. Your score has been LOWERED by {len(word)} and is now {colored(score, color='red' if score<0 else 'light_green', attrs=['bold'])}!!!"

def PlayAgain(times):
   if int(times) > 0:
      print(f"Number of times remaining:", times);
      print(Game())
      return PlayAgain(int(times)-1)
   return "THAT'S IT... Thanks for Playing!!!"




      


