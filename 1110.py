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
  discardedCards = []
  remainingCard = 0
  
  for i in range(1,num+1):
    cards.append(i)
  
  while len(cards):
    if len(cards) == 1:
      remainingCard = cards[0]
      break
    
    discardedCard = cards.pop(0)
    discardedCards.append(str(discardedCard))
    
    topCard = cards.pop(0)
    cards.append(topCard)
  
  print(f"Discarded cards: {', '.join(discardedCards)}")
  print(f"Remaining card: {remainingCard}")