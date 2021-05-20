def player_1():
        global stone
        global name
        global name1
        n=input('\nNumber of stones to be taken:')
        n=int(n)
        if n>=1 and n<=2:
         stone=stone-n
         print('\nBalance stones=',stone,'\n')
         if stone<=1:
          print('\n###',name1,' LOST###\n')
          c=input('Do you want to play again(y/n)')
          if c=='y':
                 stone=20
                 st()
          else:
                 exit()
         print('-------------------------------')
         print(name1,'s turn\n-------------------------------\n')



        n=input('\nNumber of stones to be taken:')
        n=int(n)
        if n>=1 and n<=2:
          stone=stone-n
          print('\nBalance stones=',stone,'\n')
          if stone<=1:
              print('\n###',name,' LOST ###\n')
              c=input('Do you want to play again(y/n)')
              if c=='y':
                  stone=20
                  st()
              else:
                  exit()
          print('-------------------------------')
          print(name,'s turn\n-------------------------------\n')
          player_1()

def start():
  global name
  global name1
  global stone
  name=input("\nEnter the name of player 1:")
  name1=input("\nEnter the name of player 2:")
  print('\nTOTAL NUMBER OF STONES:',stone)
  print('\n',name,'HAS THE FIRST TURN\n')
  player_1()


def player():
     global stone
     n=input('\nNumber of stones to be taken:')
     n=int(n)
     if n>=1 and n<=2:
      stone=stone-n
      print('\nBalance stones=',stone,'\n')
      if stone<=1:
          print('\n### COMPUTER LOST ###\n')
          c=input('Do you want to play again(y/n)')
          if c=='y':
              stone=20
              st()
          else:
              exit()
      print('-------------------------------')
      print('Computer s turn\n-------------------------------\n')
      computer()
     else:
      print("\n**********Invalid input Please enter 1 or 2***********\n\n\n\t\t\tRESTARTING\n\n")
      begin()

def computer():
     global stone
     global name
     if stone==19 or stone==16 or stone==13 or stone==10 or stone==7 or stone==17 or stone==14 or stone==11 or stone==8 or stone==5 or stone==2 or stone==4:
      stone-=1
      time.sleep(1)
      print('Computer took 1 stone\n')
      print('Balance stones=',stone,'\n')
      if stone<=1:
          print('\n###',name,'LOST ###\n\n')
          c=input('Do you want to play again(y/n)')
          if c=='y':
              stone=20
              st()
          else:
              exit()
      print('-------------------------------')
      print( name,'s','turn\n-------------------------------\n')
      player()
     elif stone==18 or stone==15 or stone==12 or stone==9 or stone==6 or stone==3:
      stone-=2
      time.sleep(1)
      print('Computer took 2 stone\n')
      print('Balance stones=',stone,'\n\n')
      if stone<=1:
          print('\n###',name,'LOST ###\n\n')
          c=input('Do you want to play again(y/n)')
          if c=='y':
              stone=20
              st()
          else:
              exit()
      print('-------------------------------')
      print( name,'s','turn\n-------------------------------\n')
      player()
def begin():
   global name
   global stone
   name=input("\nEnter the name of player:")
   print('\nTOTAL NUMBER OF STONES:',stone)
   print('\n',name,'HAS THE FIRST TURN\n')
   player()


import time
stone=20
name=None
name1=None
def st():
 s=input('\t'''' 1.MULTIPLAYER
         2.VS COMPUTER
         3.EXIT

         Select (1/2/3):''')
 s=int(s)
 if s==1:
      start()
 elif s==2:
      begin()
 else:
      exit()
st()
