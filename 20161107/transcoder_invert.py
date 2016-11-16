"""transcoder_invert.py
   Nov 13, 2016
   Read a transcoder file, and
   change all <in>X</in> <out>Y</out> to 
    <in>Y</in> <out>X</out>
"""
import re
import sys,codecs

def traninvert(filein,fileout):
 """ Treat filein as a text document, rather than xml document
  Assume the strings to change are all within a line
 """
 f = codecs.open(filein,encoding='utf-8',mode='r')
 fout = codecs.open(fileout,'w','utf-8')
 for line in f:
  line1 = re.sub(r'<in>(.*?)</in> *<out>(.*?)</out>',r'<in>\2</in> <out>\1</out>',line)
  fout.write(line1)

if __name__=="__main__":
 filein = sys.argv[1] 
 fileout = sys.argv[2]
 traninvert(filein,fileout)

