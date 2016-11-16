""" check_as1.py 
   and check the extended ascii therein.
   Summarizes results for sanskrit snippets and non-sanskrit snippets.
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

def init_as_roman(filein):
 "generates and returns a map(dict) from as_roman.txt"
 f = codecs.open(filein,encoding='utf-8',mode='r')
 n = 0
 ans = {}
 for line in f:
  line = line.rstrip()
  try:
   (key,val) = re.split(r' := ',line)
   ans[key] = val
  except:
   out = "init_as_roman ERROR: Cannot unpack: %s" % line
   print out.encode('utf-8')
  
 f.close()
 return ans

def check_as(italics,as_roman,fileout,sancode=True):
 # set up regex callback 'repl' with access to dictionary asdict
 asdict = {}
 as_instance = ''
 def repl(m):
  x = m.group(0)
  if (x in asdict):
   asobj = asdict[x]
  else:
   asobj = As(x,as_max)
   asdict[x] = asobj
  asobj.update(as_instance)
 # Process the italics records
 n = 0
 for rec in italics:
  n = n + 1
  nstr = "%s" % n
  as_instance = (nstr,rec.line)
  # Only consider snippets agreeing with sancode
  # Only consider those snippets classified as Sanskrit:
  recsanflag = rec.is_sanskrit()
  if sancode and recsanflag:
   # sanskrit snippets
   dummy = re.sub(r'[a-zA-Z][0-9]+',repl,rec.txt)
  elif (not sancode) and (not recsanflag):
   # nonsanskrit snippets
   dummy = re.sub(r'[a-zA-Z][0-9]+',repl,rec.txt)
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
 fileroman = sys.argv[2] # as_roman.txt
 fileout1 = sys.argv[3]  # Sanskrit snippets
 fileout2 = sys.argv[4]  # non-Sanskrit snippets
 # init dictionary as_roman
 as_roman = init_as_roman(fileroman)
 italics = init_italics(filein)

 check_as(italics,as_roman,fileout1,sancode=True)
 check_as(italics,as_roman,fileout2,sancode=False)
