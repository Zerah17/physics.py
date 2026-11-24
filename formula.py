
# PHYSICS CALCULATOR

# 1. Force Function
def force():
    mass = float(input("Enter mass (kg): "))
    acceleration = float(input("Enter acceleration (m/s^2): "))

    result = mass * acceleration
    print("Force =", result, "Newtons")


# 2. Potential Energy Function
def potential_energy():
    mass = float(input("Enter mass (kg): "))
    gravity = 9.8
    height = float(input("Enter height (m): "))

    result = mass * gravity * height
    print("Potential Energy =", result, "Joules")


# 3. Kinetic Energy Function
def kinetic_energy():
    mass = float(input("Enter mass (kg): "))
    velocity = float(input("Enter velocity (m/s): "))

    result = 0.5 * mass * velocity ** 2
    print("Kinetic Energy =", result, "Joules")


# 4. Velocity Function
def velocity():
    displacement = float(input("Enter displacement (m): "))
    time = float(input("Enter time (seconds): "))

    if time == 0:
        print("Time cannot be zero!")
    else:
        result = displacement / time
        print("Velocity =", result, "m/s")


# MAIN PROGRAM
while True:

    print("\n===== PHYSICS CALCULATOR =====")
    print("1. Force")
    print("2. Potential Energy")
    print("3. Kinetic Energy")
    print("4. Velocity")

    choice = input("Choose an operation (1-4): ")

    if choice == "1":
        force()

    elif choice == "2":
        potential_energy()

    elif choice == "3":
        kinetic_energy()

    elif choice == "4":
        velocity()

    else:
        print("Invalid choice!")

    again = input("\nDo you want to continue? (yes/no): ").lower()

    if again != "yes":
        print("Thank you for using the Physics Calculator!")
        break
