with open("Day1.txt", "r") as input_file:
	masses = tuple(int(mass) for mass in input_file.read().split("\n"))

to_fuel = lambda mass: int(mass/3) - 2  
# x = lambda a : a + 10
# print(x(5))

print(sum(map(to_fuel, masses))) 
# part 1 = 3271095

total_fuel = 0
for mass in masses:
	while mass > 8:
		mass = to_fuel(mass)
		total_fuel += mass
print(total_fuel)  
# part 2 = 4903759
