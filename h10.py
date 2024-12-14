#завдання1

#with open("numbers.txt", "w") as file:
#    file.write("50\n")
#    file.write("20\n")
#    file.write("31\n")
#    file.write("40\n")

#with open("numbers.txt", "r") as file:
#    numbers = file.readlines()


#total = sum(int(num.strip()) for num in numbers)
#print("Загальна сума чисел:", total)



#завдання2

#with open("text.txt", "w") as file:
#    file.write("This is the first line.\n")
#    file.write("Here is another line of text.\n")
#    file.write("Python is great!\n")


#with open("text.txt", "r") as file:
#    content = file.read()


#uppercase_content = content.upper()

#with open("uppercase_text.txt", "w") as file:
#    file.write(uppercase_content)

#print("Текст перетворено та збережено у файлі 'uppercase_text.txt'")

#завдання3

#with open("lines.txt", "w") as file:
#    file.write("Hello\n")
#    file.write("Python\n")
#    file.write("Programming\n")

#with open("lines.txt", "r") as file:
#    lines = file.readlines()

#print("Вміст файлу:")
#for line in lines:
#    print(line.strip())


#with open("reversed_lines.txt", "w") as file:
#    for line in lines:
#        file.write(line.strip()[::-1] + "\n")
