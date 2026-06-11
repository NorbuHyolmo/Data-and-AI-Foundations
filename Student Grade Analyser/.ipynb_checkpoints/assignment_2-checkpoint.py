def load_expenses(filename):
    expenses = []
    try:
        with open(filename, "r") as f:
            for line in f:
                line = line.strip()
                if line:
                    category, amount = line.split(",")
                    expenses.append((category, amount.strip()))
    except FileNotFoundError:
        print(f"File '{filename}' not found. Starting with empty list.")
    return expenses


def add_expense(filename, category, amount):
    if amount <= 0:
        raise ValueError(f"Amount must be positive, got {amount}")
    with open(filename, "a") as f:
        f.write(f"{category},{amount}\n")


def category_totals(expenses):
    totals = {}
    for category, amount in expenses:
        amount = float(amount)
        totals[category] = totals.get(category, 0) + amount

    print(f"\n{'Category':<15}  Total")
    print("─" * 25)
    for category, total in totals.items():
        print(f"{category:<15}: ${total:.2f}")
    print("─" * 25)

    grand_total = sum(totals.values())
    print(f"{'Grand Total':<15}: ${grand_total:.2f}")


def above_threshold(expenses, limit):
    result = [(category, float(amount)) for category, amount in expenses if float(amount) > limit]
    return result


# --- Main ---
filename = "expenses.txt"

expenses = load_expenses(filename)

category_totals(expenses)

print(f"\nExpenses above $100:")
high_expenses = above_threshold(expenses, 100)
for category, amount in high_expenses:
    print(f"  {category:<15} → ${amount:.2f}")


# --- Add a new expense and reload ---
print("\n--- Adding new expense: Food, 500 ---")
try:
    add_expense(filename, "Food", 500)
    expenses = load_expenses(filename)
    category_totals(expenses)
except ValueError as e:
    print(f"Error: {e}")

# --- Invalid amount test ---
print("\n--- Testing invalid amount ---")
try:
    add_expense(filename, "Food", -50)
except ValueError as e:
    print(f"Caught ValueError → {e}")