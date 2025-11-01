import json
import os

# File path for JSON storage
FILE_PATH = "shop_data.json"

# --- File/Database Storage ---
def load_data():
    """Load existing purchase data from JSON file"""
    if os.path.exists(FILE_PATH):
        with open(FILE_PATH, "r") as f:
            return json.load(f)
    return []  # return empty list if file doesn't exist


def save_data(data):
    """Save purchase data to JSON file"""
    with open(FILE_PATH, "w") as f:
        json.dump(data, f, indent=4)
    print("✅ Data saved successfully!\n")


# --- Menu Controller ---
def add_purchase(data):
    """Add a new purchase entry"""
    item = input("Enter item name: ")
    price = float(input("Enter item price (₹): "))
    qty = int(input("Enter quantity: "))
    total = price * qty

    entry = {
        "item": item,
        "price": price,
        "quantity": qty,
        "total": total
    }

    data.append(entry)
    save_data(data)
    print(f"🛒 Added: {item} — Total ₹{total}\n")


def view_purchases(data):
    """Display purchase records"""
    if not data:
        print("No purchases recorded yet.\n")
        return

    print("\n🧾 Purchase Summary:")
    print("-" * 45)
    print(f"{'Item':<15}{'Qty':<8}{'Price':<10}{'Total':<10}")
    print("-" * 45)

    total_sum = 0
    for p in data:
        print(f"{p['item']:<15}{p['quantity']:<8}{p['price']:<10}{p['total']:<10}")
        total_sum += p['total']

    print("-" * 45)
    print(f"Total Spent: ₹{total_sum:.2f}\n")


def analyze_data(data):
    """Display highest and average spending"""
    if not data:
        print("No data for analysis.\n")
        return

    highest = max(data, key=lambda x: x["total"])
    avg_spend = sum(p["total"] for p in data) / len(data)

    print("\n📊 Spending Analysis:")
    print(f"Highest Purchase: {highest['item']} (₹{highest['total']:.2f})")
    print(f"Average Spending per Item: ₹{avg_spend:.2f}\n")


# --- Main Menu ---
def main_menu():
    """Main menu-driven interface"""
    data = load_data()

    while True:
        print("=== ShopSmart – Smart Purchase Optimizer ===")
        print("1. Add Purchase")
        print("2. View All Purchases")
        print("3. Analyze Spending")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            add_purchase(data)
        elif choice == "2":
            view_purchases(data)
        elif choice == "3":
            analyze_data(data)
        elif choice == "4":
            print("👋 Exiting ShopSmart. Goodbye!")
            break
        else:
            print("❌ Invalid choice. Try again.\n")


# --- Run Program ---
if __name__ == "__main__":
    main_menu()
