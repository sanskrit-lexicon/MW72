# coding=utf-8
""" etymology1.py  Nov 12, 2016
  Classify the etymology sections.
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
   n=n+1
   #if n < 120: # dbg
   # print n
   try:
    recs.append(Italics(line))
   except err:
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

class Etymology(object):
 def __init__(self,ibeg,iend,ibegoffset,iendoffset):
  self.ibeg = ibeg  # index (0-based) into mw72.txt
  self.iend = iend
  self.ibegoffset=ibegoffset # offset in line ilinebeg for '[cf.'
  self.iendoffset=iendoffset # offset in line ilineend for balancing ']'
  self.ilinebeg = ibeg+1
  self.ilineend = iend+1
  self.italics=[] # list of Italics objects in this range
  self.status = 'TODO' # NOT Used
  self.type=None # set in classify_etymologies

 def set_status(self,inlines):
  # unused in etymology1
  sanitalics = [rec for rec in self.italics if rec.itype=='']
  if len(sanitalics) == 0:
   self.status = "COMPLETE"
   return
  #if len(self.italics) > 1:
  # self.status = "TODO"
  # return
  if (self.ibeg == self.iend) and (len(sanitalics) == 1):
   # one-line etymologies. We try to 'AUTO-COMPLETE'
   inline = inlines[self.ibeg]
   rec = self.italics[0]
   status = self.trysanskrit1(inline,rec)
   if status != None:
    self.status = status
    return 
  if  (len(sanitalics) > 1):
   inline = inlines[self.ibeg]
   if '[cf. {%' in inline:
    #n = 0
    for rec in self.italics:
     if rec.itype == '':
      rec.itype = 'SAN3'
      rec.line = rec.line.replace('@@','@SAN3@')
      #n = n + 1
     else:
      break
    sanitalics = [rec for rec in self.italics if rec.itype=='']
    if len(sanitalics) == 0:
     self.status = 'SAN3'
     return
  if (self.ibeg+1 == self.iend) and (len(sanitalics) == 1):
   # a 2-liner, with 1 italics 
   # first line ends with [cf.
   # second line starts with <>{%
   inline = inlines[self.ibeg].rstrip()
   inline1 = inlines[self.iend]
   if inline.endswith('[cf.'):
    if inline1.startswith('<>{%'):
     self.status = 'SAN2'
     rec = self.italics[0]
     rec.line = rec.line.replace('@@','@SAN2@')
     return
   
  # default status
  self.status = "TODO"

 def trysanskrit1(self,inline,rec):
  # if the underlying line is of form [cf. {%X%}]
  snippet = '[cf. {%' + rec.txt + '%}]'
  if inline.find(snippet)!=-1:
   rec.line = rec.line.replace('@@','@SAN1@')
   return 'SAN1'
  snippet = '[cf. {%' + rec.txt
  if inline.find(snippet)!=-1:
   rec.line = rec.line.replace('@@','@SAN1A@')
   return 'SAN1A'
  snippet = '[cf. rt'
  if inline.find(snippet)!=-1:
   rec.line = rec.line.replace('@@','@SAN1B@')
   return 'SAN1B'
  if re.search(r'\[cf[.] [1-9][.] {%' + rec.txt,inline):
   rec.line = rec.line.replace('@@','@SAN1C@')
   return 'SAN1C'
  return None

def find_etymologies(inlines):
 """ return a list of etymology objects
 """
 ans = [] # list of 2-tuples
 # inflag is true when a prior line had '[cf.'
 ibeg = -1
 for idx in xrange(0,len(inlines)):
  inline = inlines[idx]
  #inline = re.sub(r'\[Page.*?\]','',inline)
  starts = [(m.start(),m.group(1),m.group(2)) for m in re.finditer(r'(\[cf[.])|(\])',inline)]
  if len(starts)==0:
   continue
  # found some strings
  for (start,m1,m2) in starts:
   if m1!=None:
    # its '[cf.'
    if ibeg!=-1:
     print "find_etymologies ERROR 1 at line",idx+1, ibeg+1
     print inline.encode('utf-8')
     ibeg = -1 
     continue
    ibeg = idx
    ibegoffset = start
   else:  # 
    # its ']'
    ipage = inline.find('[Page')
    if (ipage!=-1) and (start > ipage): 
     # the ']' must be closing of [Page...], so ignore
     continue
    if ibeg == -1:
     print "find_etymologies WARNING 2 at line",idx+1
     print inline.encode('utf-8')
     continue
    iend = idx
    iendoffset = start
    ety = Etymology(ibeg,iend,ibegoffset,iendoffset)
    ans.append(ety)
    ibeg = -1
    # 
 return ans

def update_etymologies(etymologies,italics,inlines):
 """
 # find italics in etymology sections
 # modifies etymology objects
 """
 d = {}
 for rec in italics:
  key = rec.key()
  if key in d:
   print "italics key Occurs twice:",rec.line.encode('utf-8')
  d[key]=rec
  
 iety = 0 # last used index in etymologies
 nety = len(etymologies)
 for ety in etymologies:
  ibeg = ety.ibeg
  iend = ety.iend
  ibegoffset = ety.ibegoffset
  iendoffset = ety.iendoffset
  for idx in xrange(ibeg,iend+1):
   inline = inlines[idx]
   for m in re.finditer(r'(<nsi>.*?</nsi>)|({%+.*?%})',inline):
    if m.group(1)!=None:
     txt = m.group(1)
     txt = re.sub(r'</?nsi>','',txt)
     itype='nsan'
    else:
     txt = m.group(2)
     txt = re.sub(r'({%)|(%})','',txt)
     itype='san'
    start = m.start()
    if (idx == ibeg) and (start < ibegoffset):
     continue
    if (idx == iend) and (start > iendoffset):
     continue
    linenum = str(idx+1) 
    key = linenum + txt # same as Italics.key()
    if key not in d:
     print "Cannot find key",key.encode('utf-8'),"in italics"
     print inline.encode('utf-8')
     continue
    rec = d[key] # italics record
    ety.italics.append(rec)
 return

def classify_etymologies(etymologies):
 """ add type field to etymologies
  values: EMPTY
          SAN
          NONSAN
          MIXED
 """
 for ety in etymologies:
  italics = ety.italics
  nitalics=len(italics)
  if nitalics==0:
   ety.type = 'EMPTY'
   continue
  sanrecs = [rec for rec in italics if rec.is_sanskrit()]
  nsan = len(sanrecs)
  if nsan == nitalics:
   ety.type = 'SAN'
  elif nsan == 0:
   ety.type = 'NONSAN'
  else:
   ety.type = 'MIXED'

def etymology1(filein,filein1,fileout):
 italics = init_italics(filein)
 # dictionary on updates
 #dtemp = italics_dict(italics)
 # slurp digitization txt file into list of lines
 with codecs.open(filein1,encoding='utf-8',mode='r') as f:
  inlines = f.readlines()
 etymologies = find_etymologies(inlines)
 print len(etymologies),"etymology sections"

 # find italics in etymology sections
 # logic assumes both italics array and etymologies array are in increasing 
 # order by line number of mw72
 update_etymologies(etymologies,italics,inlines)
 print "done with update etymologies"
 classify_etymologies(etymologies)

 # set the status of each etymology object
 #for ety in etymologies:
 # ety.set_status(inlines)

 # sort etymologies by type.  The line-order should be
 # preserved as Python sorting routines are 'stable'
 etymologies.sort(key = lambda ety: ety.type)
 # generate output
 fout = codecs.open(fileout,'w','utf-8')
 ntodo = 0
 counter = collections.Counter()
 for i in xrange(0,len(etymologies)):
  ety = etymologies[i]
  status = ety.type
  counter.update([status])
  fout.write('; -------------------------------------------------\n')
  fout.write('; Case %04d %s:  %s,%s-%s,%s\n' % \
    (i+1,status,ety.ilinebeg,ety.ibegoffset+1,
                ety.ilineend,ety.iendoffset+1))
  for rec in ety.italics:
   fout.write(rec.line + '\n')

 keys = counter.keys()
 keys.sort()
 for status in keys:
  print counter[status],"etymologies have type",status

 fout.close()
 
if __name__=="__main__":
 filein = sys.argv[1] # italics
 filein1= sys.argv[2] # X.txt
 fileout = sys.argv[3] # 
 etymology1(filein,filein1,fileout)

