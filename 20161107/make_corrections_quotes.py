# coding=utf-8
""" make_corrections_quotes.py
  Generates a file of correction transactions.

"""
import sys, re,codecs


def make_corrections(filein,fileout):
 # slurp txt file into list of lines
 with codecs.open(filein,encoding='utf-8',mode='r') as f:
    inlines = f.readlines()
 # open output file
 fout = codecs.open(fileout,'w','utf-8')
 nlines = len(inlines)
 icase=0
 for idxline in xrange(0,nlines):
  line = inlines[idxline]
  if not re.search(u'{%[^%]+[’‘]',line):
   # only consider changes within italics 
   continue
  line1 = re.sub(u'[’‘]',"'",line)
  if line1 == line:
   continue
  # generate correction
  icase = icase+1
  line = line.rstrip('\r\n')
  line1 = line1.rstrip('\r\n')
  iline = idxline + 1
  outarr=[]
  outarr.append('; quote correction %04d'%icase)
  if icase == 1:
   outarr.append(u'; All these quote corrections change "’‘"  to "\'"')
  outarr.append('%s old %s' %(iline,line))
  outarr.append('%s new %s' %(iline,line1))
  for out in outarr:
   fout.write(out + '\n')
 fout.close()
 print icase,"correction transactions written to",fileout
if __name__=="__main__":
 filein = sys.argv[1] # X.txt
 fileout = sys.argv[2] #Xadj.txt
 make_corrections(filein,fileout)
