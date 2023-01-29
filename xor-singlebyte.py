enc="73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d"
known="crypto{"
enc=bytes.fromhex(enc)
for j in range(256):
  k=0
  for i in enc:
    if chr(i^j)==known[k]:
      k+=1
      if k==7:
        print(j)
        break
flag=""
for i in enc:
  flag+=chr(i^16)
print(flag)
