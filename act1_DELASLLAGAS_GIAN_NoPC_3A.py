def fibonacci(n):
    # base cases
    # the values of the first two terms is always 1, e.g[F(1) = 1 and F(2) = 1] therefore when "n" value is 1 or 2, the program will just return 1 and stop the sequence
    if n <= 2:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)

def main():
    try:
        n = int(input("Enter the value of N: "))
        # if the input is LESS THAN 1 or LESS THAN OR EQUAL TO 0 then it raises an error that will throw it to the except below
        if n <= 0:
            raise ValueError
        else:
            # assigns a variable "outputFile" for the file output.out
            outputFile = "act1_output.out"
            # creates/opens the file in write-mode "w" and assigns a variable named f
            with open(outputFile, "w") as f:
                # writes the Output line with the value of n
                f.write(f"Output [n=({n})]:\n")
                # the "1" in range ensures that the recursion will STOP at 1, anything below (0, -1, -2, etc) will not be part of the sequence
                for i in range(1, n + 1):
                    # writes every recursion
                    f.write(f"F({i}) = {fibonacci(i)}\n")
                print(f"Output saved to '{outputFile}'")
    except ValueError:
        print("Invalid input. Please enter a valid positive integer.")

if __name__ == "__main__":
    main()