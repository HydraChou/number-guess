import random

r = random.randint (1, 100) # random是函式
count = 0
while True:
	count = count + 1 #等同於 count += 1
    num = input ('請輸入一個1-100之間的整數:')
    num = int (num) #型別轉換
    if num < r:
      print ('數字太小了喔')
    elif num > r:
      print ('數字超過了啦')
    else: 
      print ('終於猜對了')
      print ('這是你猜的第', count, '次') 
      break
    print ('這是你猜的第', count, '次')