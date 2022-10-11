import time
def console():
  command = input("console: ")
  if(command == "write"):
    write()
  elif(command == "read"):
    read()
  elif(command == "help"):
    print('type "write" to add a new log.\ntype "read" to see all logs.')
    console() 
  elif(command == "exit"):
    exit(1)
  else:
      console()
def write():
  newlog = input("Log: ")
  logs = open("logs.txt","a")
  logs.write("\n"+time.ctime(time.time())+": "+newlog)
  logs.close()
  print(time.ctime(time.time())+": "+newlog)
  console()
def read():
  logs = open("logs.txt","r")
  print(logs.read())
  logs.close()
  console()
def delete():
   print() 
console()
