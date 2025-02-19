from itertools import combinations_with_replacement
import pyperclip

def find_minimum_epins(target, epins):
    epins = sorted(epins, reverse=True)
    min_length = float('inf')
    best_combination = None
    max_sum = 0  # Track the highest sum that's still under or equal to target
    
    # Try combinations from smallest to largest length
    for r in range(1, 8):  # Increased max length to handle larger combinations
        for combination in combinations_with_replacement(epins, r):
            sum_combination = sum(combination)
            
            # Only consider combinations that don't exceed the target
            if sum_combination <= target and sum_combination > max_sum:
                max_sum = sum_combination
                min_length = len(combination)
                best_combination = combination
                
                # If we found an exact match, we can stop
                if sum_combination == target:
                    return combination
    
    return best_combination if best_combination else "Eşleşme bulunamadı"

# Available Gpay ePINs
gpay_epins = [
    1, 1.18, 5, 5.9, 10, 11.8, 12, 20, 23.6, 24, 27, 30, 40, 44, 47.2, 48, 50, 
    51, 54, 59, 88, 100, 102, 118, 120, 133, 185, 199, 200, 216, 220, 236, 238, 
    240, 255, 300, 370, 440, 450, 495, 500, 583, 590, 600, 740, 880, 950, 990, 
    1000, 1950, 2200, 3000, 4400, 4750, 5000
]

# Example Usage
while True:
    try:
        target_amount = float(input("Hedef tutarı girin (Çıkmak için Ctrl+C): "))
        result = find_minimum_epins(target_amount, gpay_epins)
        print("En uygun Gpay ePINleri:", result)
        
        if isinstance(result, tuple):
            clipboard_text = "➕".join(str(int(x) if x.is_integer() else x) for x in result)
            pyperclip.copy(clipboard_text)
            print("Panoya kopyalandı:", clipboard_text)
        print("\n")
        
    except ValueError:
        print("Lütfen geçerli bir sayı girin\n")
    except KeyboardInterrupt:
        print("\nProgramdan çıkılıyor...")
        break
