start = int(input("Enter the starting number: "))
end = int(input("Enter the ending number: "))
squares = [num ** 2 for num in range(start, end + 1)]
odd_squares = [square for square in squares if square % 2 != 0]
even_squares = [square for square in squares if square % 2 == 0]
print("List of square values:", squares)
print("Odd square values:", odd_squares)
print("Even square values:", even_squares)