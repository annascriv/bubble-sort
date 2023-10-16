sequence = [4, 3, 5, 0, 1]
swaps = 0

swapped = bool

while swapped:
    swapped = False
    for i in range(len(sequence)-1):
        if sequence[i]>sequence[i+1]:
            temp = sequence[i]
            sequence[i]=sequence[i+1]
            sequence[i+1]=temp
            swapped=True
            swaps+=1
result = sequence



print(f"Final result: {result}")
print(f"Swaps: {swaps}")
