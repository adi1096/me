str1 = [7,8,9]
str2 = [4,5,6,4,5,6,7]

idx = None
for i in range(len(str1)):
    if idx and i < idx:
        continue
    for j in range(len(str2)):
        if str1[i+j] != str2[j]:
            break
    else:
        idx = i+j