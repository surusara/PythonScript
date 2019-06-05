for i in range(99, -1, -1):
    if i > 2:
        print ('{} bottles of beer on the wall!\n{} bottles of beer!\nTake one down\nAnd pass it around\n{} bottles of beer on the wall!\n\n'.format (i,i,i-1))
    elif i == 2:
        print ('{} bottles of beer on the wall!\n{} bottles of beer!\nTake one down\nAnd pass it around\n1 more bottle of beer on the wall!\n\n'.format (i,i,))
    elif i == 1:
        print ('1 bottle of beer on the wall!\n1 bottle of beer!\nTake it down\nAnd pass it around\nNo more bottles of beer on the wall!')
print()