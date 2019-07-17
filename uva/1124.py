# import inbuilt standard input output  
from sys import stdin, stdout  
  
# suppose a function called main() and 
# all the operations are performed 
def main(): 
	for line in stdin:
		stdout.write(str(line)) 
    
  
# call the main method 
if __name__ == "__main__": 
    main()     
