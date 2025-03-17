import random 
from matplotlib import pyplot as plt
from collections import Counter


num_friends = [100,49,41,40,25,60,62,32,44,32,11,44,49,52,10,7,91,40,32,10,32,50,32,32,40]
friend_counts = Counter(num_friends)
xs = range(101) 
print(str(xs))
ys = [friend_counts[x] for x in xs]
print(ys)
most_common = friend_counts.most_common(1)[0]
plt.bar(xs, ys)
plt.axis([0, 101, 0,most_common[1]+3])
plt.title("Histogram of Friend Counts")
plt.xlabel("# of friends")
plt.ylabel("# of people")
plt.show()
xs= [1.0,2.0,3.0,4.0,5.0]
def mean(xs: list[float]) -> float:
    return sum(xs) / len(xs)

def mediana(xs:list[float])->float:
    xs.sort()
    tamano=len(xs)
    #if tamano%2==0:
    
    #else:
        
    return xs

print("cantidad de puntos:",len(num_friends))
print("cantidad maxima:",max(num_friends))
print("cantidad minima:",min(num_friends))
print(mean(num_friends))
print("prueba de medianan",mediana(num_friends))






