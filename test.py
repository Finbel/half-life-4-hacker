
like_vector = [3,3,5,2,1,0]
likes = [0,1,2,3,4]
print(likes)
l = len(like_vector)
print(l)
print(like_vector.count(3))
print(sum([(l-like_vector.count(e))/l for e in likes]))