


# 1. Force
def force():
    mass = float(input("Enter mass (kg): "))
    acceleration = float(input("Enter acceleration (m/s^2): "))

    result = mass * acceleration
    print("Force =", result, "Newtons (N)")


# 2. Potential Energy
def potential_energy():
    mass = float(input("Enter mass (kg): "))
    gravity = 9.8
    height = float(input("Enter height (m): "))

    result = mass * gravity * height
    print("Potential Energy =", result, "Joules (J)")


# 3. Kinetic Energy
def kinetic_energy():
    mass = float(input("Enter mass (kg): "))
    velocity = float(input("Enter velocity (m/s): "))

    result = 0.5 * mass * velocity ** 2
    print("Kinetic Energy =", result, "Joules (J)")


# 4. Velocity
def velocity():
    displacement = float(input("Enter displacement (m): "))
    time = float(input("Enter time (seconds): "))

    if time == 0:
        print("Time cannot be zero!")
    else:
        result = displacement / time
        print("Velocity =", result, "m/s")


# 5. Acceleration
def acceleration():
    final_velocity = float(input("Enter final velocity (m/s): "))
    initial_velocity = float(input("Enter initial velocity (m/s): "))
    time = float(input("Enter time (seconds): "))

    if time == 0:
        print("Time cannot be zero!")
    else:
        result = (final_velocity - initial_velocity) / time
        print("Acceleration =", result, "m/s^2")


# MAIN PROGRAM
while True:

 1. Force
2. Potential Energy
3. Kinetic Energy
4. Velocity
5. Acceleration
Choose an operation (1-5):
    print("1. Force")
    print("2. Potential Energy")
    print("3. Kinetic Energy")
    print("4. Velocity")
    print("5. Acceleration")

    choice = input("Choose an operation (1-5): ")

    if choice == "1":
        force()

    elif choice == "2":
        potential_energy()

    elif choice == "3":
        kinetic_energy()

    elif choice == "4":
        velocity()

    elif choice == "5":
        acceleration()

    else:
        print("Invalid choice!")

    again = input("\nDo you want to continue? (yes/no): ").lower()

    if again != "yes":
        print("Thank you for using the Physics Calculator!")
        break
