import time

def waiting_game():
  print("Your target time is 4 seconds")
  x = input("---Press Enter to Begin--")
  end = 0
  print("x  = " , x)
  if (x != None):
    start = time.time()
    y = input("---Press Enter to Begin--")
    print("start ", start)
    print("x  = " , x)
    if (y != None):
      end = time.time()
      print("end ", end)
      print("Elapsed time: " , abs(round((end - start) *1000) /1000)," seconds")
      if ((end - start) >4):
        s ="seconds too slow"
      else:
        s = "seconds too fast"
      print("(",
             abs(4 - round((end - start) *1000) /1000),
             s," )" )
     
waiting_game()    