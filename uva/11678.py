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
      n, m = read_list_int()

      if n == 0 and m == 0:
        break;

      n_list = sorted(set(read_list_int()))
      m_list = sorted(set(read_list_int()))
      
      val1 = len(list(set(n_list) - set(m_list)))
      val2 = len(list(set(m_list) - set(n_list)))
      print(min(val1, val2))
      

# call the main method 
if __name__ == "__main__": 
    main()
    
#10 9
#1 1 2 3 5 7 8 8 9 15
#2 2 2 3 4 6 10 11 11
