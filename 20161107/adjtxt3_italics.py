# coding=utf-8
""" adjtxt3_italics.py
 transcoding of sanskrit snippets of italics4_roman.txt  from a
 form of iast to slp1.  Non-invertibility instances are classified.

"""
import sys, re,codecs
sys.path.append('../')  # for transcoder
from collections import Counter
import transcoder
transcoder.transcoder_set_dir("") # use local versions of transcoder files

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

def convertline(line,tranfrom,tranto):
 """ 
 """
 parts=line.split('@')
 # 4th part is the part to convert
 if tranfrom == 'roman2':
  parts[4] = parts[4].lower()
 parts[4] = transcoder.transcoder_processString(parts[4],tranfrom,tranto)
 return '@'.join(parts)

def classify_diff(oldline,newline):
 oldparts = oldline.split('@')
 newparts = newline.split('@')
 oldtxt = oldparts[4]
 newtxt = newparts[4]
 # old is original roman2
 # new is from roman2->slp->roman2  (convert oldtxt from roman2 to slp, then back to roman2)
 if oldtxt == newtxt:
  return 'SAME'
 oldlow = oldtxt.lower()
 if oldlow == newtxt:
  return 'CAP'
 if re.sub(u'[ṉṁ]',u'ṃ',oldlow) == newtxt:
  return 'CAPṉ,ṁ'
 return 'TODO' # don't know how to classify yet

def make(tranfrom,tranto,italics,fileout):
 f = codecs.open(filein,encoding='utf-8',mode='r')
 fout = codecs.open(fileout,'w','utf-8')
 n = 0
 nchg = 0
 nprob = 0
 nunc = 0 # number of lines with unconverted AS codes
 diffcounter = Counter() # summarize non-invertibility
 for rec in italics:
  line = rec.line
  # skip non-sanskrit italic snippet
  if not rec.is_sanskrit():
   continue
  line = line + '\n' # other program steps assume line ends in newline
  n = n + 1
  line1 = convertline(line,tranfrom,tranto)
  # keep old fields, and add extra field for the slp1 transcoding
  parts = line1.split('@')
  newtxt = parts[4]
  fout.write(rec.line + '@' + newtxt )
  #if line1 != line: 
  # nchg = nchg + 1  # not very interesting, perhaps. 
  # check for invertibility
  line2 = convertline(line1,tranto,tranfrom)
  difftype = classify_diff(line,line2)
  diffcounter.update([difftype])
  if difftype == 'SAME': # conversion is invertible
   continue   
  if difftype != 'TODO':
   # difference type is known. Don't need to write this case
   continue
  # difftype is TODO. Write this out for further review
  nprob = nprob + 1
  outarr = []
  outarr.append('Non-invertible unknown: %s \n' % nprob)
  outarr.append('line :%s' % line)
  outarr.append('line1:%s' % line1)
  outarr.append('line2:%s' % line2)
  for out in outarr:
   out = out.rstrip('\r\n')
   print out.encode('utf-8')
 f.close()
 fout.close()
 print n,"lines read from",filein
 #print nunc,"lines with unconverted AS codes"
 difftypes = diffcounter.keys()
 difftypes.sort()
 for difftype in difftypes:
  print difftype,diffcounter[difftype]

if __name__=="__main__":
 (tranfrom,tranto) = sys.argv[1].split(',')  # e.g., roman2,slp
 filein = sys.argv[2] # italics4_roman.txt
 italics = init_italics(filein)
 fileout = sys.argv[3] #.txt
 if False:
  print "dbg"
  print "chk0"
  temp = transcoder.transcoder_processString('a',tranfrom,tranto)
  print "chk1"
  temp = transcoder.transcoder_processString('a',tranto,tranfrom)
  print "chk2"
  exit(0)
 make(tranfrom,tranto,italics,fileout)
