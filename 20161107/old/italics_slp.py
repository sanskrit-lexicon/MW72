# coding=utf-8
""" adjtxt2_italics.py
 transcoding of italics4.txt or similar from AS to iast

"""
import sys, re,codecs
sys.path.append('../')  # for transcoder
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
 """ do transcoder, for the 
 """
 parts=line.split('@')
 # 4th part is the part to convert
 parts[4] = transcoder.transcoder_processString(parts[4],tranfrom,tranto)
 if re.search(r'[a-zA-Z][0-9]',parts[4]):
  unconverted=True
 else:
  unconverted=False
 return (unconverted,'@'.join(parts))

def make(tranfrom,tranto,italics,fileout):
 f = codecs.open(filein,encoding='utf-8',mode='r')
 fout = codecs.open(fileout,'w','utf-8')
 n = 0
 nchg = 0
 nprob = 0
 nunc = 0 # number of lines with unconverted AS codes
 for rec in italics:
  line = rec.line
  line = line + '\n' # other program steps assume line ends in newline
  n = n + 1
  (flag,line1) = convertline(line,tranfrom,tranto)
  fout.write(line1)
  if line1 != line: 
   nchg = nchg + 1
  # check for invertibility
  (dummy,line2) = convertline(line1,tranto,tranfrom)
  if line2 != line:
   nprob = nprob + 1
   outarr = []
   outarr.append('Problem # %s @ line %s\n' %(nprob,n))
   outarr.append('line :%s' % line)
   outarr.append('line1:%s' % line1)
   outarr.append('line2:%s' % line2)
   for out in outarr:
    out = out.rstrip('\r\n')
    print out.encode('utf-8')
   #print
   #exit(1)
  if flag:
   # There is unconverted AS in this line
   out = "%s AS remains: %s" %(n,line1.rstrip('\r\n'))
   print out.encode('utf-8')
   nunc = nunc + 1
 f.close()
 fout.close()
 print n,"lines read from",filein
 print nchg,"of these lines are changed in",fileout
 print nprob,"of these transformations are not invertible"
 print nunc,"lines with unconverted AS codes"

if __name__=="__main__":
 (tranfrom,tranto) = sys.argv[1].split(',')  # e.g., as,roman2
 filein = sys.argv[2] # italics4.txt
 italics = init_italics(filein)
 fileout = sys.argv[3] #Xadj1.txt
 make(tranfrom,tranto,italics,fileout)
