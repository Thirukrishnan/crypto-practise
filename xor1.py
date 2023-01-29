key1 ="a6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313"
inter1="37dcb292030faa90d07eec17e3b1c6d8daf94c35d4c9191a5e1e"
inter2="c1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1"
final="04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf"
key1=bytes.fromhex(key1)
inter1=bytes.fromhex(inter1)
inter2=bytes.fromhex(inter2)
final=bytes.fromhex(final)
flag=""
for i in range(len(key1)):
  key2=key1[i]^inter1[i]
  key3=key2^inter2[i]
  flag+=chr(key1[i]^key2^key3^final[i])
print(flag)
