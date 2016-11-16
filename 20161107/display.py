# coding=utf-8
""" display.py
 Read file like italics.txt and display a neighborhood of lines from
   mwadj.txt for each instance.

"""
import sys, re,codecs
import collections # requires Python 2.7+


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

def tokenize(s0):
 """
 """
 # Use only letters and numbers and '-'
 s = re.sub(r'[^a-zA-Z0-9-]',' ',s0)
 # Split on sequences of space characters
 tokens = re.split(r' +',s)
 tokens = [t for t in tokens if t!='']
 if False:
  out = ' :: '.join(tokens)
  out = '%s => %s => %s' %(s0,s,tokens)
  print out.encode('utf-8')
 return tokens

def init_tokendict(recs):
 d = {}
 for rec in recs:
  txt = rec.txt
  words = tokenize(rec.txt)
  key = ' '.join(words)
  if key not in d:
   d[key] = []
  d[key].append(rec)
 return d

def display(filein,inlines,fileout):
 italics = init_italics(filein)
 tokendict = init_tokendict(italics)

 #keys = sorted(tokendict.keys(),key = lambda x: x.lower())
 keys0 = [(x,len(tokendict[x])) for x in tokendict.keys()]
 keys = sorted(keys0,key=lambda x:(-x[1],x[0]))
 fout = codecs.open(fileout,'w','utf-8')
 nout = 0
 n=0
 icase = 0
 for (key,l) in keys:
  recs = tokendict[key]
  recs = sorted(recs,key=lambda x: int(x.linenum))
  icase = icase + 1
  outarr=[]
  if icase != 1:
   outarr.append('')
   outarr.append('-'*60)
  out = 'Case %03d. key=%s, %s subcases' %(icase,key,len(recs))
  outarr.append(out)

  isubcase = 0
  for rec in recs:
   isubcase = isubcase + 1
   out ='Subcase %03d.%02d: hw=%s, L=%s, lnum=%s: txt=%s' %(icase,isubcase,rec.key1,rec.lnum,rec.linenum,rec.txt)
   outarr.append('')
   outarr.append(out)
   ilinenum = int(rec.linenum)
   idx0 = ilinenum - 1
   idx1 = idx0 - 1
   idx2 = idx0 + 2
   # Add a line for editing
   # We want to autoadjust for the word 'tum', since this is actually
   # almost always the Sanskrit Infinitive ending.
   # We check several conditions indicating this 'infinitive' sense of 'tum',
   # and mark it as such if these conditions are met
   line1 = inlines[idx1].rstrip()  # previous line
   line0 = inlines[idx0] # current line
   if line1.startswith('<P>') and line1.endswith('-%%}') and\
      line0.startswith('<>{%%tum'):
    # it surely is infinitive
    pfx = '#INF '
   else:
    pfx = '# '
   # Change the 'type' to empty string
   line = rec.line.replace('@Eng1@','@@')
   if False and (icase == 1) and (isubcase == 2): # debug
    print line1
    print line0
    print pfx
    print line1.startswith('<P>')
    print line1.endswith('-%%}')
    print line0.startswith('<>{%%tum')
    exit(1)
   outarr.append(pfx + line)
   for idx in xrange(idx1,idx2):
    line = inlines[idx]
    line = line.rstrip('\r\n')
    out = '%06d %s' %(idx+1,line)
    outarr.append(out)
   #outarr.append('')
  for out in outarr:
   fout.write(out + '\n')
   nout = nout + 1
 fout.close()
 print nout,"records written to",fileout

if __name__=="__main__":
 filein = sys.argv[1] # file like italics.txt
 filein1 = sys.argv[2] # mw72adj
 fileout = sys.argv[3] # 
 # slurp digitization txt file into list of lines
 with codecs.open(filein1,encoding='utf-8',mode='r') as f:
    inlines = f.readlines()

 display(filein,inlines,fileout)

