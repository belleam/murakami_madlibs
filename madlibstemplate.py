## Prompt the user for input

first_name = input("Please enter a first name:")
second_name = input("Please enter a last name:")
full_name = first_name + " " + second_name
object_1 = input("Please enter a noun:")
adjective = input("Please enter an adjective:")
animal = input("Please enter an animal:")
object_2 = input("Please enter a noun:")
opinion = input("Please enter an opinion you feel strongly about:")
monster = input("Please enter a monster:")
place = input("Please enter a place:")

## Combine inputs into a story and print

madlibs = f"{full_name} is feeling melancholy after being left by their {object_1}. The future seems {adjective}. After meeting a talking {animal}, they set out on an adventure to find a {object_2}. On {first_name}'s travels, they reflect on whether {opinion}. Suddenly, a {monster} attacks them and they are thrown back to a {place}. {first_name} wakes up dazed and confused but finds the {object_2}."

print(madlibs)