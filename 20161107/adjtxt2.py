# coding=utf-8
""" adjtxt2.py
 transcoding of mw72

"""
import sys, re,codecs
sys.path.append('../')  # for transcoder
import transcoder
transcoder.transcoder_set_dir("") # use local versions of transcoder files



def convertline(line,tranfrom,tranto):
 """ do transcoder, but don't convert [Page...]
 """
 parts=line.split('[Page')
 parts[0] = transcoder.transcoder_processString(parts[0],tranfrom,tranto)
 if re.search(r'[a-zA-Z][0-9]',parts[0]):
  unconverted=True
 else:
  unconverted=False
 return (unconverted,'[Page'.join(parts))

def make(tranfrom,tranto,filein,fileout):
 f = codecs.open(filein,encoding='utf-8',mode='r')
 fout = codecs.open(fileout,'w','utf-8')
 n = 0
 nchg = 0
 nprob = 0
 nunc = 0 # number of lines with unconverted AS codes
 for line in f:
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
 (tranfrom,tranto) = sys.argv[1].split(',')  # e.g., as,roman
 filein = sys.argv[2] # Xadj.txt
 fileout = sys.argv[3] #Xadj1.txt
 make(tranfrom,tranto,filein,fileout)
