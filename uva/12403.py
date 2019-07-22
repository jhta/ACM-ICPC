from sys import stdin, stdout  
  
def main(): 
    total = 0
    # input via readline method 
    n = stdin.readline()

    for l in range(int(n)):
      # array input similar method 
      arr = stdin.readline().split()
      text = arr[0]

      if (text == 'donate'):
        total += int(arr[1])
      else:
        print(total)
  
# call the main method 
if __name__ == "__main__": 
    main()
