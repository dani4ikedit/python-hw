#10000ზე მეტია, დაუპრინტეთ, გოაში სწავლობდი?
#თუ 1000----10000 -ია , დაუპრინტეთ you are mid.
#თუ 1000-ზე დაბალია, დაუპრინტეთ, შემოსულიყავი გოაში, მატრიცელო!

#client_salary=int(input) ("what is your salary")

#if client_salary >=10000

#print("ხელფასი" + "client_salary"+ "გოაში სწავლობდი?")

#elif client_salary <=1000

#print("ხელფასი" + "client_salary" + "YOU ARE MID." )

#else client_salary >=1000

#print("ხელფასი" + "client_salary" + "შემოსულიყავი გოაში, მატრიცელო!")

#Len=length ითვლის სიაში მყოფ ელემენტებს

#nums = [1, 3, 5, 2, 4, 3, 3, 3]
# print (len(nums))
#   #itvlis siashi myof elementebs

# surname = "keshelava"
# print(len(surname))

#set_of_nums = set(nums)
#print(set_of_nums)

#words = ["Python", "fun"]
#           #0      
# words.insert(1, "is") #amatebs sasurvel elements siis sasurvel poziciaze
#      #სად ჩაჯდეს #რა ჩაჯდეს
# print(words)

#family=[ninuca,chico]


#x = [1, 8, 42, 3]
##print(min(x)) #x-სიის მინიმალური რიცხვი
#print(max(x)) #x-სიის მაქსიმალური რიცხვი

#nums = [4, 5, 6]
#msg = "Numbers: {0} {1} {2}". format(nums[2], nums[3], nums[1])
#print(msg)





x = [2, 4, 6, 2, 4, 7, 2, 9]
  for i in range(2):
    x.remove(4)
print(x)


family=("Ninuca","Chiko","mariami","Danieli")

full_sentence="MY moms name is:{}MY dads name is:{}My sister name is{}My name is:{}".format(family[0],family[1],family[2],family[3])
print(full_sentence)

family_ages=(32,33,9,13)

full_sentence="My moms age is:{}My dads age is:{}My sister age is{}My name is:{}".format(family_ages[0],family_ages[1],family_ages[2],family_ages[3])
print(full_sentence)

family_ages=(32+10,33+10,9+10,13+10)

full_sentence="My moms age after 10 years is:{}My dads age after 10 years is:{}My sister age after 10 years is:{}My age after 10 years is:{}".format(family_ages[0],family_ages[1],family_ages[2],family_ages[3])