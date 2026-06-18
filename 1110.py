import sys
from io import StringIO

_input = """7
19
10
6
0
"""

sys.stdin = StringIO(_input)

while True:
  num = int(input())
  
  if num == 0:
    break
  
  cards = []
  discarded_cards = []
  remaining_card = 0
  
  for i in range(1,num+1):
    cards.append(i)
  
  while len(cards):
    if len(cards) == 1:
      remaining_card = cards[0]
      break
    
    discarded_card = cards.pop(0)
    discarded_cards.append(str(discarded_card))
    
    top_card = cards.pop(0)
    cards.append(top_card)
  
  print(f"Discarded cards: {', '.join(discarded_cards)}")
  print(f"Remaining card: {remaining_card}")