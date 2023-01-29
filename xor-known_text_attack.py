enc="0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104"
known="crypto{"
enc=bytes.fromhex(enc)
key=[]
for i in range(7):
  key.append(chr(enc[i]^ord(known[i])))
key="myXORkey"*len(enc)
flag=""
for i in range(len(enc)):
  flag+=chr(enc[i]^ord(key[i]))
print(flag)
