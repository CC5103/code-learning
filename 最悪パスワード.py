pin = list(map(int, input()))

safety = "Strong"

if pin[0] == pin[1] == pin[2] == pin[3]:
    safety = "Weak"
elif (pin[0] + 1) % 10 == pin[1] and (pin[1] + 1) % 10 == pin[2] and (pin[2] + 1) % 10 == pin[3]:
    safety = "Weak"
print(safety)

