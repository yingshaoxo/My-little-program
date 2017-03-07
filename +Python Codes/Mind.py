group = ['A', 'B', 'C']
student = ['jia', 'yi']

same = 0
diff = 0

for student[0] in group:
    for student[1] in group:
        if student[0] == student[1]:
            same += 1
        else:
            diff +=1

print(same/(same+diff))