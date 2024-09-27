tal = int(input("skriv ett udda tal för att få en triangel: "))

if tal % 2 == 1:
    while tal > 0:
        print("*"*tal)
        tal -= 1
else:
    print("Börja om")