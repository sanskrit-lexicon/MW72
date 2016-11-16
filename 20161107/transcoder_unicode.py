"""transcoder_invert.py
   Nov 13, 2016
   Read a transcoder file, and
   change all \uxxxx  to the corresponding Unicode character.
   Such strings are the JSON form, so 
"""
import re
import sys,codecs
import json

def tranunicode(filein,fileout):
 """ Treat filein as a text document, rather than xml document
 """
 f = codecs.open(filein,encoding='utf-8',mode='r')
 fout = codecs.open(fileout,'w','utf-8')
 def transform(m):
  s = m.group(0)
  #print "s=",s
  s = '"%s"' % s  #  add double-quotes so it is a JSON string
  t = json.loads(s)
  return t
 for line in f:
  line1 = re.sub(r'\\u....',transform,line)
  fout.write(line1)

if __name__=="__main__":
 filein = sys.argv[1] 
 fileout = sys.argv[2]
 #t= json.loads('"\u0101"')
 #print t.encode('utf-8')
 #exit(0)
 tranunicode(filein,fileout)

 
