from sys import stdin, stdout  

D = dict(
	one=1,
	two=2,
	three=3
)

def main(): 

  # input via readline method 
  n = int(stdin.readline())
  
  for l in range(n):
    s = stdin.readline().strip()
    
    for num, val in D.items():
      if len(num) == len(s):
        counter = 0
        for n1, s1 in zip(num, s):
          if n1 != s1:
            counter+= 1
        if counter <= 1:
          print(val)
          break
      
# call the main method 
if __name__ == "__main__": 
    main()
