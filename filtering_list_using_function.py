def greater_than_five(x):
 if (x > 5):
  return True
final_list= []
lst=0
lst= [10, 20, 5, 4, 30]
final_list= filter(greater_than_five, lst)
print(list(final_list))
