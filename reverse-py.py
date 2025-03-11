def reverse_list(start, end):
    # Create a list of numbers from start to end (inclusive)
    num_list = list(range(start, end + 1))
    # Reverse the list
    reversed_list = num_list[::-1]
    return reversed_list

# Example usage
start_digit = int(input("Enter the starting digit: "))
end_digit = int(input("Enter the ending digit: "))

result = reverse_list(start_digit, end_digit)
print("Reversed List:", result)

