from sys import stdin, stdout

def read_list():
  return stdin.readline().strip().split()

def read_list_int():
  return [int(x) for x in stdin.readline().split()] 

# suppose a function called main() and 
# all the operations are performed 
def main(): 
    while True:
      b, n = read_list_int()
      if b == 0 and n == 0:
        break
      
      banks = read_list_int()
      # bank_map = { el: 0 for el in l }

      for i in range(n):
        d, c, v = read_list_int()
        banks[c - 1] = banks[c - 1] + v
        banks[d - 1] = banks[d - 1] - v
      
      flag = False
      for el in banks:
        if el < 0:
          flag = True
          break

      print("N" if flag == True else "S")
        
# call the main method 
if __name__ == "__main__": 
    main()
    
