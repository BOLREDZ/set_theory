from matplotlib import pyplot as plt
from matplotlib_venn import venn3

# Given Data
total_cars = 25
A = 15
R = 12
W = 11
A_W = 5
A_R = 9
R_W = 4
A_R_W = 3

# Creating the Venn Diagram
venn3(subsets=(A, R, A_R, W, A_W, R_W, A_R_W),set_labels=('Air Conditioner', 'Radio', 'Power Windows'))
plt.title("Popular Car Options")
plt.show()

# Calculating number of cars with Air Conditioners only
A_only = A - A_W - A_R + A_R_W

# Calculating number of cars with Radio only
R_only = R - A_R - R_W + A_R_W

# Calculating number of cars with Power Windows only
W_only = W - A_W - R_W + A_R_W

# Calculating number of cars with both a radio and power window but no air conditioner
R_W_only = R_W - A_R_W

# Calculating number of cars with both an air conditioner and radio but no power window
A_R_only = A_R - A_R_W

# Calculating number of cars with only one of the options
one_of_the_options = A_only + R_only + W_only

# Calculating number of cars with at least one of the options
at_least_one = A + R + W - A_W - A_R - R_W + A_R_W

# Calculating number of cars with none of the options
none_of_options = total_cars - at_least_one

print("Number of cars with only Air Conditioners", A_only)
print("Number of cars with only Radio", R_only)
print("Number of cars with only Power Windows", W_only)
print("Number of cars with both a radio and power window but no air conditioner", R_W_only)
print("Number of cars with both an air condition and radio but no power window", A_R_only)
print("Number of cars with only one of the options", one_of_the_options)
print("Number of cars with at least one of the options", at_least_one)
print("Number of cars with none of the options", none_of_options)