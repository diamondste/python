#1.Basic - Print all integers from 0 to 150
for x in range(0,151):
    print(x)

#2. Multiples of Five - Print all the multiples of 5 from 5 to 1,000
for x in range(5,1001,5):
    print(x)

#3.Counting, the Dojo Way - Print integers 1 to 100. if divisible by 5, print "Coding" instead. If divisble by 10,
#print "Coding Dojo"
for x in range(1,101):
    if x % 5 == 0:
        if x % 10 == 0:
            print("Coding Dojo")
        else:
            print("Coding")
    else: 
        print(x)

#4.Whoa. That Sucker's Huge - Add odd integers from 0 to 500,000, and print the final sum.
sum = 0
for x in range(1,500001):
    if x % 2 != 0:
        sum = sum + x
print(sum)

#5.Countdown by Fours - Print positive numbers starting at 2018, counting down by fours.
for x in range(2018,0,-4):
    print(x)

#6.Flexible Counter - Set three variables: lowNum, highNum, mult. Starting at lowNum and
#going through highNum, print only the integers that are a multiple of mult.
lowNum = 2
highNum = 9
mult = 3
for count in range(lowNum, highNum + 1):
    if count % mult == 0:
        print(count)