from sys import stdin, stdout

VAL = {
  'C': 10,
  'D': 100,
  'S': 1000,
  'H': 10000,
  'A': 14,
  'K': 13,
  'Q': 12,
  'J': 11,
  'T': 10,
  '9': 9,
  '8': 8,
  '7': 7,
  '6': 6,
  '5': 5,
  '4': 4,
  '3': 3,
  '2': 2
}

def sort_and_print(cards, letter):
  cards = custom_sort(cards)
  v = " ".join(cards)
  print('{}: {}'.format(letter.upper(), v))
  



def sort_func(card): 
    return VAL[card[0]] * VAL[card[1]]
  
L = [15, 3, 11, 7] 
def custom_sort(cards):
  return sorted(cards, key = sort_func)
  
# 50 5 3 14
# suppose a function called main() and 
# all the operations are performed 
def main(): 
    while True:
      side = input().lower()

      if side == "#":
        break;

      next_g = { 'e': 's', 's': 'w', 'w': 'n', 'n': 'e'}
      pos_g = { 'e': [], 's': [], 'w': [], 'n': []}
           
      part_1 = stdin.readline().strip()
      part_2 = stdin.readline().strip()
      game = part_1 + part_2

      next_side = next_g[side]
      for i in range(0, len(game) - 1, 2):
        card = game[i] + game[i + 1]
        pos_g[next_side].append(card)
        next_side = next_g[next_side]
      

      sort_and_print(pos_g['s'], 's')
      sort_and_print(pos_g['w'], 'w')
      sort_and_print(pos_g['n'], 'n')
      sort_and_print(pos_g['e'], 'e')


# call the main method 
if __name__ == "__main__": 
    main()
    
# N
# CQDTC4D8S7HTDAH7D2S3D6C6S6D9S4SAD7H2CKH5D3CTS8C9H3C3
# DQS9SQDJH8HAS2SKD4H4S5C7SJC8DKC5C2CAHQCJSTH6HKH9D5HJ
