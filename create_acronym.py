user_input = str(input("Enter a phrase: "))

acronym = ""
for i in user_input.split():
    acronym = acronym+i[0].upper()
print(acronym)
