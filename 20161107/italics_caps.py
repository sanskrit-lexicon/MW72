""" italics_caps.py
   check capital letters in Sanskrit snippets
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

class As(object):
 def __init__(self,key,m):
  self.key = key
  self.m = m
  self.n = 0
  self.instances = [] # only m of these
 def update(self,instance):
  if (self.n < self.m):
   self.instances.append(instance)
  self.n = self.n + 1


def check_caps(italics,fileout):
 # Process the italics records
 fout = codecs.open(fileout,'w','utf-8')
 n = 0
 nout = 0
 for rec in italics:
  n = n + 1
  nstr = "%s" % n
  as_instance = (nstr,rec.line)
  # Only consider snippets agreeing with sancode
  # Only consider those snippets classified as Sanskrit:
  recsanflag = rec.is_sanskrit()
  if not recsanflag:
   continue
  # The expected position of a capital letter (if any) within rec.txt
  # is either 
  # (a) as the first character of the string, or
  # (b) as the first character After an initial '--'
  #   NOTE: There are many (approx. 2500) cases where a capital letter
  #   occurs after '--', BUT NOT AT the beginning of the snippet.
  #   These should probably be considered markup errors. But for now,
  #   We decide not to change the digitization, but rather to ignore
  #   these cases as exceptions.  
  txt = rec.txt
  if re.search(r'^[A-Z]',txt):
   rest = txt[1:]
  elif re.search(r'^--[A-Z]',txt):
   rest = txt[3:]
  else:
    m =   re.search(r'^[^A-Z]+--[A-Z](.*)$',txt)
    if m:
     rest = m.group(1)
    else:
     rest = txt
  if not re.search(r'[A-Z]',rest):
   # capital letters occur only as expected. 
   continue
  # This snippet has a capital letter in an unexpected spot
  fout.write(rec.line + '\n')
  nout = nout + 1
 fout.close()
 print nout,"records written to",fileout
 exit(0)
 #write asdict to fileout
 #fout = open(fileout,'w')
 fout = codecs.open(fileout,'w','utf-8')
 keys = asdict.keys()
 keys = sorted(keys,cmp=lambda x,y: cmp(x.lower(),y.lower()))
 # generate  outlines_common arrays of lines to output
 m = as_max
 nkey = 0
 outlines_common = []
 notfound = 0
 nfound = 0
 for key in keys:
  nkey = nkey + 1
  asobj = asdict[key]
  outlines = []  # the lines for this key
  if key in as_roman:
   descr = as_roman[key]
   nfound = nfound + 1
  else:
   descr = 'NO DESCRIPTION'
   notfound = notfound + 1
  out = "%s %5d := %s" %(key,asobj.n,descr)
  outlines.append(out)
  #outlines_common.append(outlines)
  out_instances=[]
  for as_instance in asobj.instances:
   #out_instances.append(' :: '.join(as_instance))
   out_instances.append(as_instance[1])  # the line
  if (asobj.n < m):
   outlines=outlines+out_instances
  outlines_common.append(outlines)
  #else:
  # outlines_common.append(outlines)
 print "description found for %s AS codes" % nfound
 print "NO DESCRIPTION found for %s AS codes" % notfound
 # write header 
 fout.write("input file = %s\n" % filein)
 fout.write("*******************************\n")
 fout.write("%s  'AS' codes follow, with instances\n" % len(outlines_common))
 fout.write("Each instances shows: page,headword,line number in %s\n" % filein)
 fout.write("*******************************\n")
 k = 0
 for outlines in outlines_common:
  k = k + 1
  # fout.write("# %s --------------------------------------------------\n" % k);
  j = 0
  for out in outlines:
   j = j + 1
   if j == 1:
    out = '# %02d %s' %(k,out)
   fout.write("%s\n" % out)
   if (j > 1):
    #fout.write("ejf: \n")
    #fout.write("tm: \n")
    #fout.write(".....\n")
    pass
 fout.close()
#-----------------------------------------------------
if __name__=="__main__":
 filein = sys.argv[1] # italics4
 fileout = sys.argv[2] # exceptions
 # init dictionary as_roman
 italics = init_italics(filein)

 check_caps(italics,fileout)
