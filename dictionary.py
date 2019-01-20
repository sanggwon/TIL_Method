#딕셔너리 메소드
a = {"a":"b","c":"d"}
print(a["c"],a.pop("a"))
print(a.pop("e","웅?"))
a.update(e="f")
print(a)
print(a.get("g"))
print(a.get("g","웅?"))

b = [1,2,3]
print("".join(map(str,b)))

a = ["a","b","c"]
b = [1,2,3]
print(dict(zip(a,b)))

def even(x):
    if x%2==1 :
        return False
    else :
        return True
print(list(filter(even,b)))