# coding=utf-8
""" etymology.py  Nov 8, 2016

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
 def __init__(self,ibeg,iend):
  self.ibeg = ibeg  # index (0-based) into mw72.txt
  self.iend = iend
  self.ilinebeg = ibeg+1
  self.ilineend = iend+1
  self.italics=[] # list of Italics objects in this range
  self.status = 'TODO' # set later

 def set_status(self,inlines):
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
 ans = [] # list of 2-tuples
 inflag=False
 for idx in xrange(0,len(inlines)):
  inline = inlines[idx]
  inline = re.sub(r'\[Page.*?\]','',inline)
  if inflag:
   if ']' in inline:
    iend = idx
    ans.append(Etymology(ibeg,iend))
    inflag = False
   elif ('[cf.' in inline):
    print "Unexpected cf at line#",idx+1
  elif ('[cf.' in inline):
   inflag = True
   ibeg = idx
   if ']' in inline: # a one-liner: [cf. xxx]
    iend = idx
    ans.append(Etymology(ibeg,iend))
    inflag = False
 assert not inflag,"find_etymologies"
 return ans


def update_etymologies(etymologies,italics,inlines):
 """
 # find italics in etymology sections
 # logic assumes both italics array and etymologies array are in increasing 
 # order by line number of mw72
 """
 iety = 0 # last used index in etymologies
 nety = len(etymologies)
 irec = 0
 dbg = False
 for rec in italics:
  irec = irec+1
  ilinenum = int(rec.linenum)
  if ilinenum == 65825:
   print "BEGIN line",ilinenum,"iety=",iety,"rec.line=",rec.line.encode('utf-8')
  if dbg and (irec>3000):
   print "DEBUG BREAK"
   break
  for i in xrange(iety,nety):
   ety = etymologies[i]
   ilinebeg = ety.ilinebeg
   ilineend = ety.ilineend
   if ilinenum == 65825:
    print "etymology lines=",ilinebeg,ilineend
   if ilinenum < ilinebeg:
    #continue
    break
   if ilineend < ilinenum:
    #iety = iety + 1
    #break
    continue
   # we know the italic snippet occurs in this line
   # and that this line is part of a [cf...] multi-line section.
   # we want to the snippet to occur 'within' the cf-section,
   # i.e., after the '[cf.' and before the ']'
   # we set the Boolean 'flag' variable to be True in this occasion
   # if false (i.e., snippet occurs before the [cf. or after the ])
   # This determination is rather delicate
   inline = inlines[ilinenum-1]
   inline = re.sub(r'\[Page.*?\]','',inline)
   j=-9
   k1=-9
   k2=-9
   flag='NOFLAG'
   if (ilinebeg<ilinenum) and (ilinenum<ilineend):
    flag = True
   elif len(re.findall(r'\[cf[.]',inline)) > 1:
    # there are about 25 of these.  We'll count all of them as True
    flag = True
   else:
    j = inline.find(rec.txt) # position of the italic snippet
    if j == -1:
     out= " etymology %s not found in %s" %(rec.line,inline)
     print out.encode('utf-8')
    k1 = inline.find('[cf.') # position of [cf. may be -1 (absent)
    k2 = inline.find(']')  # position of ] may be -1 (absent)
    if j < k1:
     flag = False # snippet occurs before
    elif (k2 != -1) and (k2 < j):
     flag = False  # snippet occurs after
    else:
     flag = True
   if (ilinenum == 65825):
    print "chk:",j,k1,k2,rec.line,flag
   if flag:
    ety.italics.append(rec)
   else:
    #print "skipping",rec.line.encode('utf-8')
    pass
   # reset iety for efficiency
   iety = i
   break
  
def etymology(filein,filein1,fileout):
 italics = init_italics(filein)
 # dictionary on updates
 #dtemp = italics_dict(italics)
 # slurp digitization txt file into list of lines
 with codecs.open(filein1,encoding='utf-8',mode='r') as f:
  inlines = f.readlines()
 etymologies = find_etymologies(inlines)
 print len(etymologies),"etymology sections"
 def chkprint(msg):
  print msg
  for ety in etymologies:
   if ety.ilinebeg == 65825:
    for rec in ety.italics:
     print rec.line.encode('utf-8')
    break
 chkprint('chk1')
 # find italics in etymology sections
 # logic assumes both italics array and etymologies array are in increasing 
 # order by line number of mw72
 update_etymologies(etymologies,italics,inlines)
 chkprint('chk2')
 # set the status of each etymology object
 for ety in etymologies:
  ety.set_status(inlines)
 chkprint('chk3')
 # sort etymologies by status.  The line-order should be
 # preserved as Python sorting routines are 'stable'
 etymologies.sort(key = lambda ety: ety.status)
 # generate output
 fout = codecs.open(fileout,'w','utf-8')
 ntodo = 0
 counter = collections.Counter()
 for i in xrange(0,len(etymologies)):
  ety = etymologies[i]
  status = ety.status
  counter.update([status])
  if status != 'COMPLETE':
   fout.write('; ------------------------------------------------------\n')
  fout.write('; Case %04d: %s-%s %s\n' % (i+1,ety.ilinebeg,ety.ilineend,status))
  todolines=[] # for lines with TODO etymologies
  for rec in ety.italics:
   # for convenience in examining cases and generating codes,
   # comment out those italic snippets whose 'itype' is NOT the 
   # default
   if rec.itype == '':
    fout.write(rec.line + '\n')
    todolines.append(int(rec.linenum))
   #elif rec.itype == 'SAN1':
   # fout.write(rec.line + '\n')
   else:
    fout.write('; ' + rec.line + '\n')
  if status != 'COMPLETE':
   # for TODO,  extract the lines from mw72
   for idx in xrange(ety.ibeg,ety.iend+1):
    inline = inlines[idx].rstrip('\r\n')
    linenum = idx+1
    if linenum in todolines:
     fout.write(';**** %06d %s\n' %(idx+1,inline))
    else:
     fout.write('; %06d %s\n' %(idx+1,inline))

 keys = counter.keys()
 keys.sort()
 for status in keys:
  print counter[status],"etymologies are",status

 fout.close()
 
if __name__=="__main__":
 filein = sys.argv[1] # italics
 filein1= sys.argv[2] # X.txt
 fileout = sys.argv[3] # 
 etymology(filein,filein1,fileout)

