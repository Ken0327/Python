Score = [87,66,90,65,70]
Total_Score = 0
for count in range(5):
    print( 'Number %d student score:%d' %(count+1, Score[count]))
    Total_Score += Score[count]
print('-----------------------')
print('Total score in 5 students:%d' %Total_Score)