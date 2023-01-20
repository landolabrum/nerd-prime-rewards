from datetime import datetime
from os import system, name
from time import sleep
def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')

    
def prnt(data):
  current = datetime.now().strftime("%H:%M:%S")
  print(f'{current}: {data}                       ', end="\r")
def progress(amount,total=100):
  icon='🏆'
  progress='░░░░░░░░░░░░░░░░░░░░'
  total=20/total
  amount=int(amount * total)
  progress=progress[:amount].replace('░','▓')+icon+progress[amount:]
  clear()
  print("[ TOTAL PROGRESS ]: "+progress)