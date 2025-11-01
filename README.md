## 🛍️ ShopSmart – Smart Purchase Optimizer (Python + JSON)

### 📘 Project Overview

**ShopSmart** is a simple Python-based purchase management system that helps users **record, view, and analyze** their purchases.
It uses a **menu-driven interface** and stores all data in a **JSON file** for easy access and persistence.

---

### 🧩 Features

✅ Add new purchase details (item name, price, quantity)
✅ View all recorded purchases in a clean table format
✅ Analyze spending (highest and average purchase)
✅ Data saved automatically in a `shop_data.json` file
✅ JSON-based data handling — easy to read and modify

---

### 🗂️ Project Structure

```
ShopSmart/
│
├── shopsmart.py        # Main Python program
└── shop_data.json      # JSON data storage file
```

---

### ⚙️ Requirements

* Python 3.8 or above
* Works directly in VS Code terminal or any Python IDE
* No external libraries required (uses only built-in `json` and `os`)

---

### ▶️ How to Run

1. **Clone or download** the project folder.
2. Open the folder in **VS Code**.
3. Ensure both files are in the same directory:

   * `shopsmart.py`
   * `shop_data.json`
4. Run the program using:

   ```bash
   python shopsmart.py
   ```
5. Follow the on-screen menu:

   ```
   === ShopSmart – Smart Purchase Optimizer ===
   1. Add Purchase
   2. View All Purchases
   3. Analyze Spending
   4. Exit
   ```

---

### 🧾 Example JSON Data (`shop_data.json`)

```json
[
    {
        "item": "Rice",
        "price": 60.0,
        "quantity": 5,
        "total": 300.0
    },
    {
        "item": "Milk",
        "price": 50.0,
        "quantity": 3,
        "total": 150.0
    },
    {
        "item": "Apples",
        "price": 100.0,
        "quantity": 2,
        "total": 200.0
    }
]
```

---

### 🧠 How It Works

| Component                        | Description                                        |
| -------------------------------- | -------------------------------------------------- |
| **User**                         | Interacts with the program using a text-based menu |
| **Menu Controller**              | Handles input/output and function navigation       |
| **File/Database Storage (JSON)** | Saves all purchase data                            |
| **Output Display**               | Shows tables and analysis results in console       |

---

### 💡 Future Enhancements

* Add chart visualization (using `matplotlib`)
* Enable CSV export and import
* Integrate database storage (SQLite or MySQL)

---

### 👨‍💻 Author

**k.Laharika**
Built as a mini-project using Python and JSON for data handling.


