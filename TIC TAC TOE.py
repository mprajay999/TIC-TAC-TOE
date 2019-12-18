bo = [i for i in range(1, 10)]

def print_board(lst):
    print(" ", lst[0], "|", lst[1], "|", lst[2])
    print('-------------')
    print(" ", lst[3], '|', lst[4], '|', lst[5])
    print('-------------')
    print(" ", lst[6], '|', lst[7], '|', lst[8])

def insrt(letter,pos):
      bo[pos-1]=letter       #inserts_letter_into_po

def is_space_free(pos):
      return bo[pos-1]==(pos) #returns_true_if_space_is_free

def player1move():
      run= True
      while run:
            pos = input("USER1 enter value of position X ")
            try:
                  pos=int(pos)
                  if pos>0 or pos<10:
                        if is_space_free(pos):
                              run = False
                              insrt('X',pos)
                        else:
                              print("enter empty value")
                  else:
                        print("enter value betweem 0 and 9")
            except:
                  print("enter an integer")

def player2move():
      run= True
      while run:
            pos = (input("USER2 enter value of position O "))
            try:
                  pos=int(pos)
                  if pos>0 or pos<10:
                        if is_space_free(pos):
                              run = False
                              insrt('O',pos)
                        else:
                              print("enter  empty value")
                  else:
                        print("enter value betweem 0 and 9")
            except:
                  print("enter an integer")

def iswinner(bo,le):
      return(bo[0]==le and bo[1]==le and bo[2]==le
             or bo[3]==le and bo[4]==le and bo[5]==le
             or bo[6]==le and bo[7]==le and bo[8]==le
             or bo[0]==le and bo[3]==le and bo[6]==le
             or bo[1]==le and bo[4]==le and bo[7]==le
             or bo[2]==le and bo[5]==le and bo[8]==le
             or bo[0]==le and bo[4]==le and bo[8]==le
             or bo[2]==le and bo[4]==le and bo[6]==le)  ##returns_ttrue_if_sol_is_found

def isfull(bo):
      if((bo[0]==1) or (bo[1]==2) or (bo[3]==4) or (bo[4]==5)or (bo[5]==6) or (bo[6]==7) or (bo[7]==8) or (bo[8]==9)):
            return False
      else:
            return True

      #returns_false_if_board_is_not_full

def main():
      print("welcome to TIC TAC TOE")
      print_board(bo)
      run=True
      while run:
          player1move()
          print_board(bo)
          if iswinner(bo,'X'):
                print("congrats USER1 you win")
                break
          if isfull(bo):
                print("TIE")
                break


          player2move()
          print_board(bo)
          if iswinner(bo,'O'):
                print("congrats USER2 you win")
                break
          if isfull(bo):
                print("it's a TIE")
                break


while True:
      x=input("DO YOU WANT TO PLAY Y/N")
      if x=='y' or x=='Y':
            main()
      else:
            break
























