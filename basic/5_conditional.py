# coding=utf-8

age = int(input('enter the age of your dog: '))
if age < 0:
    print('age should be larger than 0.')
elif age == 1:
    print('equals to a 14 year old human.')
elif age == 2:
    print('equals to a 22 year old human.')
else:
    human = 22 + (age - 2) * 5
    print('equals to a %d year old human.' % human)
