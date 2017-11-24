#Mission #14 https://www.youtube.com/watch?v=T2unHs55Shs
#Description [PL] www.bartekzoltowski.pl/programowanie/Gyn_Misja_014
from Crypto.Cipher import AES
from Crypto.Hash import MD5
import os
files = os.listdir('/bin')

for fil in files:
  loc = "/bin/"+fil
  with open(loc, 'rb') as f:
    md5 = MD5.new()
    md5.update(f.read())
  aes_e = AES.new(md5.digest(), AES.MODE_CBC, 'ThisIsRandomLOL!')
  ciphertxt = "489917cd3093786a6f1eb81645373a51dc1594cad896b2352f3be3c2dacbef00f9621542cda23826b1e77719207b53e9"
  print aes_e.decrypt(ciphertxt.decode("hex"))
  
