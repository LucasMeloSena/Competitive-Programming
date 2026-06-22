while True:
  data = [str(item) for item in input().split()]
  
  if data[0] == '0' and data[1] == '0':
    break

  num1 = data[0]
  num2 = data[1]

  carry_operations = 0
  carry = 0
  
  len_num1 = len(num1)
  len_num2 = len(num2)
  _len = max(len_num1, len_num2)

  num1 = num1.zfill(_len)
  num2 = num2.zfill(_len)
  
  for i in range(_len - 1, -1, -1):  
    _sum = int(num1[i]) + int(num2[i]) + carry
    if _sum > 9:
      carry = 1
      carry_operations += 1
    else:
      carry = 0

  if carry_operations == 0:
    print("No carry operation.")
  elif carry_operations == 1:
    print(f"{carry_operations} carry operation.")
  else:
    print(f"{carry_operations} carry operations.")