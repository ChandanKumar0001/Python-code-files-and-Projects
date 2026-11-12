# Type Conversion  -> This is automatically happence by Python that is called Implicit Conversion 

a = 2
b = 4.25

sum = a + b # 2.0 + 4.25 => 6.25
print(sum)

print("-----------------------------------------------")

# Type Casting  -> When we change the data type forcefully that is called Type Casting or Explicit Conversion.

x = float("2")  # Here we convert forcefully string type value to float type value
y = 4.25

print(type(x))
print(x + y)