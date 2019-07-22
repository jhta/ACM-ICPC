from sys import stdin, stdout

def rec_calc(val):
  if len(val) == 1:
    return val
  
  total = 0
  for char in val:
      total += int(char)
  return rec_calc(str(total))
  
def main(): 
    while True:
      val = stdin.readline().strip()
      if val == "0":
        break
      
      print(rec_calc(val))
        
if __name__ == "__main__": 
    main()
    
