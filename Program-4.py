dic1={1:11, 2:8}
dic2={3:4, 4:4}
dic3={5:3 ,6:2}
dic4={7:0 ,8:1,9:1}
for d in (dic1, dic2, dic3): dic4.update(d)
print(dic4)
