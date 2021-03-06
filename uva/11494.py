from sys import stdin, stdout

def main():
  while True:
    x1, y1, x2, y2 = [int(x) for x in stdin.readline().strip().split()]
    
    if x1 == 0 and y1 == 0 and x2 == 0 and y2 == 0:
      break

    if x1 == x2 and y1 == y2:
      print(0)
    elif (x1 == x2) or (y1 == y2):
      print(1)
    else:
      if abs(y2 - y1) == abs(x2 - x1):
        print(1)
      else:
        print(2)



if __name__ == "__main__": 
    main()
