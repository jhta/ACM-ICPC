from sys import stdin, stdout

def read_int():
  return int(stdin.readline().strip())

def main():
  n = read_int()

  while n:
    n -= 1
    white = stdin.readline()
    t = read_int()
    s = read_int()

    while t:
      t -= 1
      x1, y1, x2, y2 = [int(x) for x in stdin.readline().strip().split()]
      
      if x1 == x2 and y1 == y2:
        print(0)
      elif abs(y2 - y1) == abs(x2 - x1):
        print(1)
      else:
        pair1 = (x1 + y1) % 2
        pair2 = (x2 + y2) % 2

        if pair1 != pair2:
          print("no move")
        else:
          print(2) 


    


if __name__ == "__main__": 
    main()
