from itertools import combinations

def find_minimum_epins(target, epins):
    epins = sorted(epins, reverse=True)  # Sort in descending order for efficiency
    best_combination = None
    
    for r in range(1, len(epins) + 1):
        for combination in combinations(epins, r):
            if sum(combination) == target:
                if best_combination is None or len(combination) < len(best_combination):
                    best_combination = combination
        
        if best_combination:
            break  # Stop searching once we find the best combination
    
    return best_combination if best_combination else "No exact match found"

# Available Gpay ePINs
gpay_epins = [
    1, 1.18, 5, 5.9, 10, 11.8, 12, 20, 23.6, 24, 27, 30, 40, 44, 47.2, 48, 50, 
    51, 54, 59, 88, 100, 102, 118, 120, 133, 185, 199, 200, 216, 220, 236, 238, 
    240, 255, 300, 370, 440, 450, 495, 500, 583, 590, 600, 740, 880, 950, 990, 
    1000, 1950, 2200, 3000, 4400, 4750, 5000
]

# Example Usage
try:
    target_amount = float(input("Enter the target amount: "))
    result = find_minimum_epins(target_amount, gpay_epins)
    print("Optimal ePINs:", result)
except ValueError:
    print("Please enter a valid number")
