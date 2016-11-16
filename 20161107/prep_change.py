""" prep_change.py
  Read a file like italics.txt,
  and, for each line, retrieve the full line from the
  digitization, and write prototype of correction record for
  the line.
"""

import re,sys
as_max = 10
import codecs, unicodedata

class Italics(object):
 def __init__(self,line):
  line = line.rstrip('\r\n')
  self.line=line
  parts = line.split('@')
  if len(parts) == 5:
   (self.lnum,self.key1,self.linenum,self.itype,self.txt) = parts
   self.ok = True
  else:
   self.ok = False

def init_italics(filein):
 with codecs.open(filein,"r","utf-8") as f:
  #recs = [Italics(line) for line in f]
  #recs = [Italics(line) for n,line in f.iteritems() if n < 50]
  recs=[]
  n = 0
  for line in f:
   rec = Italics(line)
   if rec.ok:
    recs.append(rec)
   n=n+1
   #if n == 50: #dbg
   # break
 print len(recs),"records from",filein
 return recs

def prepare(filein,filedig,fileout):
 italics = init_italics(filein)
 # slurp txt file into list of lines
 with codecs.open(filedig,encoding='utf-8',mode='r') as f:
    inlines = f.readlines()
 fout = codecs.open(fileout,'w','utf-8')
 # Process the italics records
 n = 0
 for rec in italics:
  n = n + 1
  linenum = int(rec.linenum)
  idx = linenum - 1
  line = inlines[idx].rstrip('\r\n')
  L = rec.lnum
  key1 = rec.key1
  chg = " %s -> %s" %(rec.txt,rec.txt)
  fout.write(';' + '\n')
  out = "; L=%s, hw=%s, chg=%s" %(L,key1,chg)
  fout.write(out+'\n')
  out = "%s old %s" %(linenum,line)
  fout.write(out+'\n')
  out = "%s new %s" %(linenum,line)
  fout.write(out+'\n')
 fout.close()
#-----------------------------------------------------
if __name__=="__main__":
 filein = sys.argv[1] # italics.txt format
 filedig = sys.argv[2] # X.txt
 fileout = sys.argv[3]
 prepare(filein,filedig,fileout)
