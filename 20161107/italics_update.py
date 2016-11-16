# coding=utf-8
""" italics_update.py

"""
import sys, re,codecs
import collections # requires Python 2.7+


class Italics(object):
 def __init__(self,line):
  line = line.rstrip('\r\n')
  self.line=line
  (self.lnum,self.key1,self.linenum,self.itype,self.txt) = line.split('@')
 def key(self):
  return self.linenum + self.txt

def init_italics(filein):
 with codecs.open(filein,"r","utf-8") as f:
  #recs = [Italics(line) for line in f]
  #recs = [Italics(line) for n,line in f.iteritems() if n < 50]
  recs=[]
  n = 0
  for line in f:
   n=n+1
   #if n < 120: # dbg
   # print n
   try:
    recs.append(Italics(line))
   except:
    print "Error at line",n,"of",filein
    print line.encode('utf-8')
   #if n == 50: #dbg
   # break
 print len(recs),"records from",filein
 return recs


def italics_dict(recs):
 """ Generate a dictionary from the array of Italics objects
 """
 d={}
 for rec in recs:
  key = rec.key()
  if key in d:
   #print "italics_dict DUPLICATE KEY:",rec.line.encode('utf-8')
   #exit(1)
   pass
  d[key]=rec
 return d

def update(filein,filein1,fileout):
 fout = codecs.open(fileout,'w','utf-8')
 italics = init_italics(filein)
 updates = init_italics(filein1)
 # dictionary on updates
 dtemp = italics_dict(italics)
 d=italics_dict(updates)
 nupd = 0
 nout = 0
 n = 0
 counter=collections.Counter()
 for rec in italics:
  n=n+1
  key = rec.key()
  if key in d:
   recu = d[key] # updated record. Assume the same except for itype
   rec.itype = recu.itype
   nupd = nupd + 1
  out = '%s@%s@%s@%s@%s' % (rec.lnum,rec.key1,rec.linenum,rec.itype,rec.txt)
  fout.write(out + '\n')
  nout = nout+1
  counter.update([rec.itype])
 fout.close()
 print nout,"records written to",fileout
 print nupd,"records updated"
 keys = counter.keys()
 keys.sort()
 sankeys = ['','hw1','hw2','SAN','SAN1','SAN1A','SAN1B','SAN1C','SAN2']
 print "summary of Sanskrit snippets"
 santot = 0
 for k in keys:
  if k in sankeys:
   print k,counter[k]
   santot = santot + counter[k]
 print "Total Sanskrit snippets:",santot
 print "summary of non-Sanskrit snippets"
 print
 tot = 0
 for k in keys:
  if k not in sankeys:
   print k,counter[k]
   tot = tot + counter[k]
 print "Total non-Sanskrit snippets:",tot
 

if __name__=="__main__":
 filein = sys.argv[1] # italics
 filein1= sys.argv[2] # update file
 fileout = sys.argv[3] # 
 update(filein,filein1,fileout)

