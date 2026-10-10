list = [10, 5, 10, 8, 3]
freq = {}

for num in list:
    freq[num] = freq.get(num,0) + 1

