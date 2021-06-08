print("\n \t\t TDMA Solver\n")
print("\nRefer the nTDMA.pdf for the general form of TriDiagonal Matrix Algorithm with n unknowns\n")
n = int(input("\nEnter the number of unknowns (n): "))

# create zeros list/array as per user input
D = [0]*n  # diagonal element
beta = [0]*n  # element to the left of diagonal
alpha = [0]*n  # element to the right of diagonal
c = [0]*n  # value of constant element
A = [0]*n  # intermediate values
C = [0]*n
X = [0]*n  # final answer array

# input element values from user
for i in range(0, n):
    D[i] = float(input("\nEnter Diagonal {} value D{}:    ".format((i+1),(i+1))))

for i in range(0, n-1):
    alpha[i] = float(input("\nEnter \N{GREEK SMALL LETTER ALPHA}{} value:    " .format(i+1)))

for i in range(1, n):
    beta[i] = float(input("\nEnter \N{GREEK SMALL LETTER BETA}{} value:    ".format(i+1)))


# input value of constant from the user
for i in range(0, n):
    c[i] = float(input("\nEnter value of Constant {}:    ".format(i+1)))


beta[0] = 0  # since there is no element to the left of the diagonal so we assign 0 to the first value of beta
alpha[n-1] = 0  # for the last diagonal element there is no element to the right so we assign 0 to the last value of alpha
#also note that the above value is already 0 in program but to show the complete algorithm, above two lines are written

# print the input given by user
print("\n")
for i in range(0, n):
    print("\t D%d = %f \t Beta%d = %f \t Alpha%d = %f \t C%d = %f " % (i+1, D[i], i+1, beta[i], i+1, alpha[i], i+1, c[i]))
    print("\n")

# solution, forward substitution of intermediate terms
for i in range(0, n):
    A[i] = alpha[i]/(D[i] - beta[i]*A[i-1])
    C[i] = (beta[i]*C[i-1] + c[i])/(D[i] - beta[i]*A[i-1])

# print values of intermediate terms
for i in range(0, n):
    print("\tA%d = %f \t\t C'%d = %f" % (i+1, A[i], i+1, C[i]))
    print("\n")

print("\n")


# Calculation of final values to get the solution

X[n-1] = C[n-1]   #equating the last X term for backward substitution
j = n-2
while j >= 0:
    X[j] = A[j] * X[j+1] + C[j]
    j = j-1

print("The X values are:\n")
for i in range(0, n):
    print("\t\t X%d = %f  \n" % (i+1, X[i]))
#to hold output screen
input()