"""transcoder_invert.py
   Nov 13, 2016
   Read a transcoder file, and
   remove lines which are 'no-ops':  <in>X</in> <out>X<out>
"""
import re
import sys,codecs

def trantidy(filein,fileout):
 """ Treat filein as a text document, rather than xml document
 """
 f = codecs.open(filein,encoding='utf-8',mode='r')
 fout = codecs.open(fileout,'w','utf-8')
 for line in f:
  m = re.search(r'<in>(.*?)</in> *<out>(.*?)</out>',line)
  if m:
   if m.group(1) == m.group(2):
    # skip this line
    continue
  fout.write(line)

if __name__=="__main__":
 filein = sys.argv[1] 
 fileout = sys.argv[2]
 trantidy(filein,fileout)

 
