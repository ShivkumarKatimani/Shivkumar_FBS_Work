#1. pass :neglect exepected indentation error

#for i in range (1,10)
#   pass

#2.  break : for terminating the loop 
#for i  in range (1,10):
 # if(i == 4):
  #  break
  #print(i) 

#3. continue : to stop perticulor iteration

#for i  in range (1,10):
 #   if(1==4):
   #     continue
    #print(i)

#4. else will execute when loop excuted successfully
for i in range (1,10):
    if(i == 4):
        continue
    print(i)
else:
    print("else block will excuted")