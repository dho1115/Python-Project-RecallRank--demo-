if __name__ == "__main__":
   import os;
   from dotenv import load_dotenv
   import sys;

   load_dotenv(); #load environment variables.
   getfolderpath = os.getenv("folderpath"); 
   sys.path.append(getfolderpath); #Adding a path to folder so I can access WordGenerator from apis.py.

   from folder.GameLogic import Greeting, Game, PlayAgain;

   def main():
      try:
         input("Press Any Key To Continue...");
         Greeting();
         print(Game());

         numberoftimes = eval(input("How many more times do you want to play? ")) #recursion

         print(PlayAgain(numberoftimes))

      except Exception:
         print("Sorry... you should have entered a number... GOODBYE!!!");
   
   main()



   
   

