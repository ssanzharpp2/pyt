st = {"a", "b", "c"}
st1 = {"car", "cow", "bow"}
num = {1,2,3,4}
st2 = st.union(st1, num)
print(st2)
st2.clear()
st2 = st | st1 | num
print(st2)
st.update(num)
print(st)
st3 = st.intersection(st1)
print(st3)