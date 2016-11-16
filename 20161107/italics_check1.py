""" italics_check1.py
   check Sanskrit islands in non-Sanskrit
"""

import re,sys
as_max = 10
import codecs, unicodedata

class Italics(object):
 def __init__(self,line):
  line = line.rstrip('\r\n')
  self.line=line
  (self.lnum,self.key1,self.linenum,self.itype,self.txt) = line.split('@')
 def key(self):
  return self.linenum + self.txt
 def is_sanskrit(self):
  santypes = ['','hw1','hw2','SAN','SAN1','SAN1A','SAN1B','SAN1C','SAN2']
  return (self.itype in santypes)

def init_italics(filein):
 with codecs.open(filein,"r","utf-8") as f:
  #recs = [Italics(line) for line in f]
  #recs = [Italics(line) for n,line in f.iteritems() if n < 50]
  recs=[]
  n = 0
  for line in f:
   recs.append(Italics(line))
   n=n+1
   #if n == 50: #dbg
   # break
 print len(recs),"records from",filein
 return recs


def check1(italics,fileout):
 # Process the italics records
 fout = codecs.open(fileout,'w','utf-8')
 nout = 0
 irec = 0
 nitalics = len(italics)
 rec0 = None
 while (irec < nitalics):
  rec = italics[irec]
  recsanflag = rec.is_sanskrit()
  if not recsanflag:
   # Not a sanskrit snippet. Mark it as the previous such non-san
   irec = irec+1
   rec0 = rec
   continue
  if rec0 == None:
   # previous case also Sanskrit
   irec = irec+1
   continue
  # This is a Sanskrit record, with a previous non-san snippet
  if rec0.key1 != rec.key1:
   # we are in different headwords. Reinitialize
   rec0 = None
   irec = irec+1
   continue
  # we are in the same headword
  # If this is a 'SAN' type, that means we have manually set this value.
  # so leave it
  if rec.itype == 'SAN':
   #rec0 = None
   irec = irec+1
   continue
  # if rec is a 'sub headword', treat as if a new key
  if rec.txt.startswith('--') or (rec.itype in ['hw1','hw2']):
   rec0 = None
   irec = irec+1
   continue
  # skip if there are more two lines between rec0 and rec
  iline0 = int(rec0.linenum)
  iline = int(rec.linenum)
  if iline > (iline0+2):
   rec0 = None
   irec = irec+1
   continue
   
  # autochange the type to that of rec0
  rec.itype = rec0.itype + '-IMP'  # IMP means this is implied
  newline = '@'.join([rec.lnum,rec.key1,rec.linenum,rec.itype,rec.txt])
  nout = nout + 1
  fout.write('; ' + rec0.line + '\n')
  fout.write(newline + '\n') 
  irec = irec+1
 fout.close()
 print nout,"records written to",fileout
 
#-----------------------------------------------------
if __name__=="__main__":
 filein = sys.argv[1] # italics4
 fileout = sys.argv[2] # exceptions
 # init dictionary as_roman
 italics = init_italics(filein)

 check1(italics,fileout)
