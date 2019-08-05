from sys import stdin, stdout
import math

def get_row(n):
  return (math.floor(n / 8)) + 1

def get_col(n):
  return (n - (get_row(n) - 1) * 8) + 1

def validate_position(position):
	return position >= 0 and position <= 63

def main(): 
    for line in stdin:
      k, q, m = [int(x) for x in line.strip().split()] 

      if q == k or not validate_position(q) or not validate_position(k):
        print("Illegal state")
        continue
      
      if q == m:
        print("Illegal move")
        continue
      k_row = get_row(k)
      k_col = get_col(k)

      q_row = get_row(q)
      q_col = get_col(q)

      m_row = get_row(m)
      m_col = get_col(m)

      # print("k row", k_row)
      # print("k col", k_col)

      # print("q row", q_row)
      # print("q col", q_col)


      # print("m row", m_row)
      # print("m col", m_col)
    
      if q_row == m_row and q_col == m_col:
        print("Illegal move")
        continue

      if q_row != m_row and m_col != q_col:
        print("Illegal move")
        continue
      
      else:
        block = 0
        if k_row - 1 <= 0 or k_row - 1 == m_row:
          block += 1
        if k_row + 1 > 8 or k_row + 1 == m_row:
          block += 1
        if k_col - 1 <= 0 or k_col - 1 == m_col:
          block += 1
        if k_col + 1 > 8 or k_col + 1 == m_col:
          block += 1
        
        if block == 4:
          print("Stop")
          continue
        else:
          if q_row == m_row:
            if q_row == k_row:
              if q_col < k_col:
                if m_col == k_col - 1:
                  print("Move not allowed")
                  continue
                elif m_col > k_col - 1:
                  
                  print("Illegal move")
                  continue
                else:
                  print(validate_allowed(k, k_row, k_col, m))
                  # print("Continue")
                  continue
              else:
                if m_col == k_col + 1:
                  print("Move not allowed")
                  continue
                elif m_col < k_col + 1:
                  print("Illegal move")
                  continue
                else:
                  print(validate_allowed(k, k_row, k_col, m))
                  # print("Continue")
                  continue
            else:
              print(validate_allowed(k, k_row, k_col, m))
              continue
          if q_col == m_col:
            if q_col == k_col:
              if q_row < k_row:
                if m_row == k_row - 1:
                  print("Move not allowed")
                  continue
                elif m_row > k_row - 1:
                  print("Illegal move")
                  continue
                else:
                  print(validate_allowed(k, k_row, k_col, m))
                  # print("Continue")
                  continue
              else:
                if m_row == k_row + 1:
                    print("Move not allowed")
                    continue
                if m_row < k_row + 1:
                    print("Illegal move")
                    continue
                else:
                  print(validate_allowed(k, k_row, k_col, m))
                  # print("Continue")
                  continue
            else:
              print(validate_allowed(k, k_row, k_col, m))
              continue


def validate_allowed(k, k_row, k_col, m):
  k_not_allowed = get_n_allowed(k, k_row, k_col)
  not_allowed = False

  for pos in k_not_allowed:
    if m == pos:
      not_allowed = True
      break
    
  return "Move not allowed" if not_allowed else "Continue" 

def get_n_allowed(n, row, col):
  left = n if (col % 8) - 1 < 0 else -1
  right = n if (col % 8) + 1 > 7 else -1
  top = n - 8 if n - 8 >= 0 else -1
  bottom = n + 8 if n + 8 <= 63 else -1

  return [left, right, top, bottom]

# call the main method 
if __name__ == "__main__": 
    main()
    
# N
# CQDTC4D8S7HTDAH7D2S3D6C6S6D9S4SAD7H2CKH5D3CTS8C9H3C3
# DQS9SQDJH8HAS2SKD4H4S5C7SJC8DKC5C2CAHQCJSTH6HKH9D5HJ
