def celsius_to_fahrenheit(c):
    f_temp = (c * 9/5) + 32
    return f_temp

def fahrenheit_to_celsius(f):
    c_temp = (f - 32) * 5/9
    return c_temp

print(f"The temp is {celsius_to_fahrenheit(56):.1f} °F ")
print(f"The temp is {fahrenheit_to_celsius(87):.1f} °C ")
print(f"The temp is {fahrenheit_to_celsius(65):.1f} °C ")
print(f"The temp is {celsius_to_fahrenheit(16):.1f} °F ")