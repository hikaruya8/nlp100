motion = 'stressed'
print(motion[::-1])

police_car = 'パトカー'
taxi = 'タクシー'

result = ''
for a, b in zip(police_car, taxi):
  result += a + b

print(result)

