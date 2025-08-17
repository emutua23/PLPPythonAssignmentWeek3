# PLPPythonAssignmentWeek3
# Discount Calculator Assignment

## 📋 Project Description
This assignment demonstrates the practical application of Python conditional statements through a discount calculator program. The project implements decision-making logic to determine whether to apply discounts based on specified criteria.

## 🎯 Learning Objectives
- Master conditional statements (if, elif, else)
- Implement user input validation and error handling  
- Create reusable functions with clear documentation
- Apply boolean expressions in real-world scenarios
- Practice proper code structure and commenting

## 🔧 Technical Requirements
- Python 3.6 or higher
- Understanding of basic Python data types (float, string)
- Knowledge of user input functions and exception handling

## 📦 Features
✅ **Smart Discount Logic**: Applies discounts only when >= 20%
✅ **Input Validation**: Handles invalid inputs gracefully
✅ **User-Friendly Interface**: Clear prompts and formatted output
✅ **Error Handling**: Comprehensive try-catch implementation
✅ **Code Documentation**: Detailed docstrings and comments
✅ **Extensible Design**: Additional functions for discount categorization

## 🚀 How to Run
1. Save the code as `discount_calculator.py`
2. Open terminal/command prompt
3. Navigate to the file location
4. Run: `python discount_calculator.py`
5. Follow the interactive prompts

## 💡 Key Concepts Demonstrated

### Conditional Statements
The program uses if-else logic to make decisions:
```python
if discount_percent >= 20:
    # Apply discount
    final_price = price - (price * discount_percent / 100)
else:
    # Keep original price
    final_price = price
```

### Boolean Expressions  
Multiple boolean conditions are evaluated:
- `discount_percent >= 20` (threshold check)
- `price < 0` (validation check)
- `discount_percentage < 0` (validation check)

### Function Design
Clean, reusable functions with clear parameters:
- `calculate_discount(price, discount_percent)` - Core logic
- `discount_category(discount_percent)` - Classification logic
- `main()` - User interaction handler

## 📊 Test Cases
The program handles various scenarios:
- Discount >= 20%: Applied successfully
- Discount < 20%: Original price returned
- Negative values: Error handling activated
- Invalid input: Exception management triggered

## 🔍 Code Structure
```
discount_calculator.py
├── calculate_discount()     # Main discount calculation
├── discount_category()      # Discount classification  
├── main()                  # User interaction handler
└── __main__ execution      # Program entry point
```

## 🏆 Assignment Completion Criteria
✅ Function accepts price and discount_percent parameters
✅ Conditional logic checks if discount >= 20%
✅ Returns discounted price or original price appropriately
✅ User input prompts implemented
✅ Final price displayed with appropriate messaging
✅ Code includes proper documentation and error handling

## 📚 Related Coursework Concepts
This assignment reinforces the following concepts from the conditional statements lesson:
- Boolean variables and expressions as building blocks
- Decision-making processes in programming
- if, elif, else statement structures
- Practical application of relational operators (>=, <, ==)
- Real-world problem solving with conditional logic

Sample Output:

PS C:\Users\HP\Desktop\PLP\python\assignments\week3\PLPPythonAssignmentWeek3> & C:/Python313/python.exe c:/Users/HP/Desktop/PLP/python/assignments/week3/PLPPythonAssignmentWeek3/calculate_discount.py
==================================================
🛒 DISCOUNT CALCULATOR
==================================================
Enter the original price of the item: $120
Enter the discount percentage: 35

------------------------------
📊 CALCULATION RESULTS
------------------------------
Original Price: $120.00
Discount Percentage: 35.0%
✅ Discount Applied: $42.00
💰 Final Price: $78.00
💵 You saved: $42.00!

==================================================
🏷️  DISCOUNT CATEGORIES
==================================================
5% → ❌ NO DISCOUNT (Not Applied)
15% → 📝 SMALL DISCOUNT (Not Applied)
20% → ✅ GOOD DISCOUNT
25% → ✅ GOOD DISCOUNT
35% → ⭐ GREAT DISCOUNT
55% → 🔥 MEGA DISCOUNT
PS C:\Users\HP\Desktop\PLP\python\assignments\week3\PLPPythonAssignmentWeek3> 