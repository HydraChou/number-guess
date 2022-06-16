import random

r = random.randint (1, 100) # random是函式

while True:
    num = input ('請輸入一個1-100之間的整數: ') #input會把所有東西存成字串
    num = int(num) #型別轉換
    if num < r:
      print ('數字太小了喔')
    elif num > r:
      print ('數字超過了啦')
    else: 
      print ('終於猜對了')
      break