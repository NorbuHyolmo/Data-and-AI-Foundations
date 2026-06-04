def user_input():
    name = str(input("Enter your name: "))
    city = str(input("Enter your city: "))
    height = float(input("Enter your height in cm: "))
    birth_date = {
        "day": int(input("Enter your birth day (1-31): ")),
        "month": int(input("Enter your birth month (1-12): ")),
        "year": int(input("Enter your birth year (e.g., 1990): "))
    }

    hobbies = list()
    print("Enter a hobby (or type 'done' to finish):")
    while True:
        hobby = input()
        if hobby.lower() == 'done':
            break
        hobbies.append(hobby)
    
    languages = set()
    print("Enter a language you speak (or type 'done' to finish):")
    while True:
        language = input()
        if language.lower() == 'done':
            break
        languages.add(language)
    

    return {
        "name": name.capitalize(),
        "city": city.capitalize(),
        "age": 2026 - birth_date["year"],
        "height": height,
        "birth_date": birth_date,
        "hobbies": hobbies,
        "languages": languages
    }


def display_bio_data(bio_data):
    print("\n" + "="*35)
    print("       PERSONAL BIO DATA CARD")
    print("="*35)
    print(f"  Name       : {bio_data['name'][0]}... (private)")
    print(f"  Age        : {bio_data['age']} years")
    print(f"  City       : {bio_data['city']}")
    print(f"  Height     : {bio_data['height']} cm")
    print(f"  Birth Date : {bio_data['birth_date']['day']}/{bio_data['birth_date']['month']}/{bio_data['birth_date']['year']}    (D/M/Y)Format")
    print(f"  Hobbies    : {len(bio_data['hobbies'])} [{type(bio_data['hobbies']).__name__}]")
    print(f"  Languages  : {len(bio_data['languages'])} [{type(bio_data['languages']).__name__}]")
    print("="*35 + "\n")


display_bio_data(user_input())