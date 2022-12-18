import time



start = time.time()

my_list = []
# Dynamic storage
for num in range(30_000_000):
    my_list.append(num)
end = time.time()
print(f"Seconds: {start - end}")

#Prealocation storage

start = time.time()

my_list2 = [0] * 30_000_000

for num in range(30_000_000):
    my_list2[num] = num

end = time.time()

print(f"Seconds: {start - end}")