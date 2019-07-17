# import inbuilt standard input output  
from sys import stdin, stdout  
  
# suppose a function called main() and 
# all the operations are performed 
def main():
  # for read and iterate all the lines
	for line in stdin:
		# print with stdout.write method the string parsed line
		stdout.write(str(line)) 
    
  
# call the main method 
if __name__ == "__main__": 
    main()     
		
# ------------------------------------
# Example input:
# Line 1
# Line 2
# Line 3

# Output:
# Line 1
# Line 2
# Line 3
