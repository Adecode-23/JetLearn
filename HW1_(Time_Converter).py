print("Time Converter")
print("1. Hours to Minutes")
print("2. Hours to Seconds")
print("3. Minutes to Seconds")
print("4. Seconds to Minutes")

choice = input("Choose an option (1-4): ")

if choice == "1":
    hours = float(input("Enter hours: "))
    print(hours * 60, "minutes")

elif choice == "2":
    hours = float(input("Enter hours: "))
    print(hours * 3600, "seconds")

elif choice == "3":
    minutes = float(input("Enter minutes: "))
    print(minutes * 60, "seconds")

elif choice == "4":
    seconds = float(input("Enter seconds: "))
    print(seconds / 60, "minutes")

else:
    print("Invalid choice. Try again.")