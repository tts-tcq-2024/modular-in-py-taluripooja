# main.py

from test_color_utils import run_tests
from color_utils import get_color_from_pair_number, get_pair_number_from_color, color_pair_to_string

# Function to demonstrate color pair functionality
def demonstrate_color_pair_logic():
    print("Color pair for pair number 15:")
    major_color, minor_color = get_color_from_pair_number(15)
    print(color_pair_to_string(major_color, minor_color))
    
    print("\nPair number for color combination 'Red' and 'Green':")
    pair_number = get_pair_number_from_color('Red', 'Green')
    print(f"Pair number: {pair_number}")

# Main entry point
if __name__ == '__main__':
    # Run the test cases first
    run_tests()
    
    # Demonstrate the functionality of the color pair logic
    demonstrate_color_pair_logic()
