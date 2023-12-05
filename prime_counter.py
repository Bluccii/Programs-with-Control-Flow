import stdio
import sys

# Accept n (int) as command-line argument.
...

# Set count (number of primes <= n) to 0
...

for i in range(..., ...):
    # for each i from [2, n]...

    # Set j (potential divisor of i) to 2.
    ...

    while ...:
        # As long as j is less than or equal to i / j...

        if ...:
            # If j divides i, break (i is not a prime).
            ...

        # Increment j by 1.
        ...

    # If you got here by exhausting the while loop, i is a prime, so increment count by 1.
    if ...:
        ...

# Write count to standard output.
...
