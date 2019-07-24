from sys import stdin, stdout

def read_list():
  return stdin.readline().strip().split()

def read_list_int():
  return [int(x) for x in stdin.readline().strip().split()] 
# 50 5 3 14
# suppose a function called main() and 
# all the operations are performed 
def main(): 
    while True:
      h, u, d, f = read_list_int()
      if h == 0:
        break
      fa = float(u * f /100)
      sum = 0
      days = 1

      while True:
        sum += u

        if u > 0:
          u -= fa
        
        if sum > h:
          break
        
        sum -= d
        if sum < 0:
          break;
        
        days += 1
      
      print("failure on day" if sum < 0 else "success on day", days)


# call the main method 
if __name__ == "__main__": 
    main()
    
