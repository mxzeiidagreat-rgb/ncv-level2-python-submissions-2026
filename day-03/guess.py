raw = " nomsa DLAMINI "
name = raw.strip().title()
parts = name.split()
print("Name: ", parts[0])
print("Surname: ", parts[-1].title())

if parts[0].isdigit():
    print("Accepted")
else:
    print("rejected")
    
salary = 23400.56
print(f"R{salary:.2f}")
print(f"R___{salary:<60}___")
print(f"R___{salary:>60.2f}___")
