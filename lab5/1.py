import re
txt = "ab, hdh, hdsggch, cabb, abbbb, abbb"
x = re.findall(r"\b\w*ab*\b", txt)
print(x)


import re
txt = "ab, hdh, hdsggch, cabb, abbbb, abbb"
x = re.findall(r"\b\w*ab{2,3}\b", txt)
print(x)



import re
txt = "a_b h_dh hdsgg_ch cab_b abb_bb abbb"
x = re.findall(r"\b[a-z]+_[a-z]+\b", txt)
print(x)


import re
txt = "a, Ndc, jDjd"
x = re.findall(r"[A-Z][a-z]+", txt)
print(x)



import re
txt = "ak dmjf abbbbk kjajgfb allb"
x = re.findall(r"\b\w*a\w*b\b", txt)
print(x)



import re
txt = "hello world.hello, world"
x = re.sub(r"[ ,.]", ":", txt)
print(x)



import re
txt = "snake_case_to_camel_case"
x = re.sub(r"_([a-z])", lambda v: v.group(1).upper(), txt)
print(x)


import re
txt = "HelloWorld BigData"
x = re.findall(r"[A-Z][a-z]*", txt)
print(x)


import re
txt = "HelloWorldBigData"
x = re.sub(r"([A-Z])", r" \1", txt)
print(x)


import re
txt = "camelCaseToSnakeCase"
x = re.sub(r"([A-Z])", r"_\1", txt).lower()
print(x)