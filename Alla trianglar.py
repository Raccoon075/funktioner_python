while True:
    try:
        tal = int(input("skriv ett udda tal för att få en triangel: "))
        if tal % 2 and tal>0:
            break
        else:
            print("börja om")
    except ValueError:
        print("inga bokstäver eller decimaler tack!")


for i in range(tal,0,-1):
    print(f"{"¤"*i:<{tal}}")

for i in range(tal,0,-2):
    print(f"{"¤"*i:^{tal}}")

for i in range(tal,0,-1):
    print(f"{"¤"*i:>{tal}}")

    
