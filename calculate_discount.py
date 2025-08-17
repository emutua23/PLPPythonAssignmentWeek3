# Discount Calculator Assignment
# Demonstrates conditional statements and user input handling

def calculate_discount(price, discount_percent):
    """
    Calculate the final price after applying a discount if applicable.
    
    Args:
        price (float): The original price of the item
        discount_percent (float): The discount percentage to apply
    
    Returns:
        float: The final price after applying discount (if >= 20%) or original price
    """
    # Conditional statement: Apply discount only if 20% or higher
    if discount_percent >= 20:
        # Calculate discount amount
        discount_amount = price * (discount_percent / 100)
        final_price = price - discount_amount
        return final_price
    else:
        # Return original price if discount is less than 20%
        return price

def main():
    """
    Main function to handle user interaction and demonstrate the discount calculator.
    """
    print("=" * 50)
    print("🛒 DISCOUNT CALCULATOR")
    print("=" * 50)
    
    try:
        # Get user input for original price
        original_price = float(input("Enter the original price of the item: $"))
        
        # Validate price input
        if original_price < 0:
            print("❌ Error: Price cannot be negative!")
            return
        
        # Get user input for discount percentage
        discount_percentage = float(input("Enter the discount percentage: "))
        
        # Validate discount percentage
        if discount_percentage < 0:
            print("❌ Error: Discount percentage cannot be negative!")
            return
        
        # Calculate final price using our function
        final_price = calculate_discount(original_price, discount_percentage)
        
        # Display results with appropriate messaging
        print("\n" + "-" * 30)
        print("📊 CALCULATION RESULTS")
        print("-" * 30)
        print(f"Original Price: ${original_price:.2f}")
        print(f"Discount Percentage: {discount_percentage}%")
        
        # Conditional output based on whether discount was applied
        if discount_percentage >= 20:
            discount_amount = original_price - final_price
            print(f"✅ Discount Applied: ${discount_amount:.2f}")
            print(f"💰 Final Price: ${final_price:.2f}")
            print(f"💵 You saved: ${discount_amount:.2f}!")
        else:
            print(f"ℹ️  Discount not applied (minimum 20% required)")
            print(f"💰 Final Price: ${final_price:.2f}")
        
    except ValueError:
        print("❌ Error: Please enter valid numerical values!")
    except Exception as e:
        print(f"❌ An unexpected error occurred: {e}")

# Additional function to demonstrate more conditional logic
def discount_category(discount_percent):
    """
    Categorize discount levels using if-elif-else statements.
    
    Args:
        discount_percent (float): The discount percentage
    
    Returns:
        str: Category description
    """
    if discount_percent >= 50:
        return "🔥 MEGA DISCOUNT"
    elif discount_percent >= 30:
        return "⭐ GREAT DISCOUNT"
    elif discount_percent >= 20:
        return "✅ GOOD DISCOUNT"
    elif discount_percent >= 10:
        return "📝 SMALL DISCOUNT (Not Applied)"
    else:
        return "❌ NO DISCOUNT (Not Applied)"

# Run the program
if __name__ == "__main__":
    main()
    
    # Demonstrate additional conditional logic
    print("\n" + "=" * 50)
    print("🏷️  DISCOUNT CATEGORIES")
    print("=" * 50)
    
    test_discounts = [5, 15, 20, 25, 35, 55]
    for discount in test_discounts:
        category = discount_category(discount)
        print(f"{discount}% → {category}")