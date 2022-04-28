import random

random.seed(102)

# Month 1: +89, 1 centre
print(random.randrange(50, 101))

print(random.randrange(0, 51))

centre_1 = 13
waiting_list = 89 - 13

# Month 2: +79, 1 centre
print(random.randrange(50, 100))

print(random.randrange(0, 51))
print(random.randrange(0, 51))

centre_1 += 32
centre_2 = 45

waiting_list -= 32
waiting_list -= 45
waiting_list += 79


# Month 3: +80, 2 centres
print(random.randrange(50, 101))

print(random.randrange(0, 51))
print(random.randrange(0, 51))

centre_1 += 45
centre_2 += 33

waiting_list -= 45
waiting_list -= 33
waiting_list += 80

print(centre_1, centre_2, waiting_list)

random.seed()