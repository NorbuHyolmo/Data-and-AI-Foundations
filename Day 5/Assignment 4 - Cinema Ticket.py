def user_input():
    age = int(input("Please enter your age: "))
    day = input("Please enter the day of the week (example: Monday, Tuesday, etc.): ")
    member = input("Are you a member of the cinema club? (yes/no): ").lower()

    return {
        "age": age,
        "day": day,
        "member": True if member == "yes" else False
    }

def age_discount(age):
    category = ""
    if age < 5:
        category = "Child (Under 5)"
        discount = 1.0
    elif 5 <= age <= 18:
        category = "Minor"
        discount = 0.5
    elif age >= 60:
        category = "Senior"
        discount = 0.3
    else:
        category = "Adult"
        discount = 0.0
    return [discount, category]


def calculate_ticket_price(user_info):
    age = user_info["age"]
    day = user_info["day"].lower()
    member = user_info["member"]
    discount, category = age_discount(age)
    weekdays = {'monday', 'tuesday', 'wednesday', 'thursday', 'friday'}
    base_price = 400

    # apply age-based discount
    price = base_price - (base_price * discount)

    # extra 10% off for members on weekdays
    member_discount = False
    if member and day in weekdays:
        price *= 0.9
        member_discount = True

    # Total discount
    total_discount = ((base_price - price) / base_price) * 100

    # popcorn offer
    if member:
        popcorn = "Free large popcorn"
    else:
        popcorn = "Free small popcorn" if age < 5 else "No popcorn offer"

    # closing message using ternary
    message = "Free entry!" if price == 0 else "Enjoy the show!"

    # summary with aligned colons
    spacing = 18
    print("\n" + "=" * 35)
    print(f"{'Category':<{spacing}}: {category}")
    print(f"{'Day':<{spacing}}: {day.capitalize()}")
    print(f"{'Member':<{spacing}}: {'Yes' if member else 'No'}")
    print(f"{'Member discount':<{spacing}}: {'10% off (weekday)' if member_discount else 'None'}")
    print(f"{'Total discount':<{spacing}}: {total_discount:.0f}%")
    print(f"{'Popcorn offer':<{spacing}}: {popcorn}")
    print(f"{'Final price':<{spacing}}: Rs. {price:.2f}")
    print(f"{'Message':<{spacing}}: {message}")
    print("=" * 35)

    
calculate_ticket_price(user_input())