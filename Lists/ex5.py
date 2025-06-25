scores = [96, 47, 113, 89, 100, 102]
amount_over_100 = 0

for score in scores:
    if score >= 100:
        amount_over_100 += 1

print(amount_over_100)