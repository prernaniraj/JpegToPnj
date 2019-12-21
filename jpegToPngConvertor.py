arr = {"a","v","c"}
print("*".join(arr))

def add(a,*b,**c):
   for subject , mark in c.items():
       print(subject)

add(1,2,4,7,e=2,be=3)
def hihgest_marksheet(marksheet):
    for subject, marks in marksheet.items():
        print(f"{subject}: {marks} ")

hihgest_marksheet({'Hindi' : 98, "Marathi": 95, "Python" :100})
# hihgest_marksheet.sorted(key)
print(hihgest_marksheet)
print(hihgest_marksheet("Hindi"))
name = 'ABFJSKDF'
print(name[len(name):5:-1])