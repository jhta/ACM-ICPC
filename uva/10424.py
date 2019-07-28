from sys import stdin, stdout
import string

ABC = list(string.ascii_lowercase)
ABC_dict = { ABC[i]: i for i in range(0, len(ABC) ) }

def get_sum(val):
  if val > 9:
    sum = 0
    for c in str(val):
      sum += int(c)
    return get_sum(sum)
  return val


def parse_val(line):
  total = 0
  for c in line:
    ca = c.lower()
    if ca in ABC_dict:
      val = ABC_dict[ca]
      total += int(val) + 1
  
  if total > 9:
    return get_sum(total)
  
  return total

def main(): 
  for line in stdin:
    l1 = line.strip()
    l2 = stdin.readline().strip()
    val1 = parse_val(l1)
    val2 = parse_val(l2)

  
    maxi = max(val1, val2)
    mini = min(val1, val2)

    dec = ((1 / maxi) * mini) * 100
    calc  = round((dec), 2)
    print("{:.2f} %".format(calc))


# call the main method 
if __name__ == "__main__": 
    main()
    
