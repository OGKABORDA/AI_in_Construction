numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

# TODO заменить значение пропущенного элемента средним арифметическим
sum = 0
count = 1
for i in range(len(numbers)):
    if numbers[i] == None:
        pass
    else:
        sum += numbers[i]
        count += 1
avg = sum/count
for i in range(len(numbers)):
    if numbers[i] == None:
        numbers[i] = avg
print("Измененный список:", numbers)
