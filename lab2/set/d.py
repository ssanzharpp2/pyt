st = {"a", "b", "c", True, False, 0,1,2}
st.remove("a")
print(st)
st.discard("b")
print(st)
x = st.pop()
print(st)
st.clear()
print(st)
del st