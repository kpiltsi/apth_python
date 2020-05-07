s = input('Πληκτρολογήστε όνομα \n')
adict = {}
if len(s) == 1:
    print('Μήκος = 1')
    exit(1)
length = len(s)/2.0
for i in range(0, int(length)):
    if s[i] == s[len(s)-1-2*i]:
        continue
    else:
        print('Δεν είναι παλίνδρομο')
        exit(1)
adict = {s: len(s)}
alist = list(s)
print(adict)
print(alist)

