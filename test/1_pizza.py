
prices = {
        'small': 150,
        'medium': 200,
        'large': 250,
        'pepperoni_small': 20,
        'pepperoni_medium': 30,
        'pepperoni_large':30,
        'extra_cheese': 10}

pizza_size = input("Enter pizza size (small, medium, large): ")
total_cost = prices.get(pizza_size)

if total_cost == 0:
        print("Please enter 'small', 'medium','large'")

pepperoni = input("Do you want pepperoni? (yes/no): ")
if pepperoni == 'yes':
        pepperoni_size=input("Enter pepperoni size (small, medium, large):")
        if pizza_size == 'small':
            total_cost += prices['pepperoni_small']
        elif pizza_size =='medium':
          total_cost += prices['pepperoni_medium']

        else:
            total_cost += prices['pepperoni_large']

extra_cheese = input("Do you want extra cheese? (yes/no): ")
if extra_cheese == 'yes':
        total_cost += prices['extra_cheese']

print("\nTotal Cost: Rs."+ str(total_cost))




