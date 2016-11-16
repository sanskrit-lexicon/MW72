# coding=utf-8
""" adjtxt1.py
  python adjtxt1.py mw72adj.txt italics4.txt mw72adj1.txt
  a. change all {%% to {%, and %%} to %}
  b. for any italicized snippets identified as non-sanskrit in italics4.txt,
     change the markup from {%X%} to <nsi>X</nsi>.

"""
#import xml.etree.ElementTree as ET
import sys, re,codecs

def adjustline(line,idxline,nonsand):
 line = line.rstrip('\r\n') # maybe already done by readlines 
 #1. Replace {%% with {%, and %%} with %}
 line=line.replace('{%%','{%')
 line=line.replace('%%}','%}')
 #2. search for {%X%}. For each such X, check if X is in nonsand in this line
 #   and if so, replace with <nsi>X</nsi>
 ilinenum = idxline + 1
 linenum = str(ilinenum) # convert to string for function f
 def f(m):
  expr = m.group()  # the whole expression: {%X%}
  txt = m.group(1)  # X only
  key = linenum + txt # see as Italics.key()
  if key not in nonsand:
   return expr
  # this is a non-sanskrit snippet. Change the markup
  # update number of times this snippet changed
  rec = nonsand[key]
  rec.used = rec.used + 1
  return "<nsi>%s</nsi>" % txt
 line1 = re.sub(r'{%(.*?)%}',f,line)
 return line1

class Italics(object):
 def __init__(self,line):
  line = line.rstrip('\r\n')
  self.line=line
  (self.lnum,self.key1,self.linenum,self.itype,self.txt) = line.split('@')
  # number of times this is used in a replacement. See adjustline function
  self.used=0  
 def key(self):
  return self.linenum + self.txt
 def is_sanskrit(self):
  santypes = ['','hw1','hw2','SAN','SAN1','SAN1A','SAN1B','SAN1C','SAN2']
  return (self.itype in santypes)

def init_non_sanskrit(filein):
 f = codecs.open(filein,encoding='utf-8',mode='r')
 d = {}
 for line in f:
  rec = Italics(line)
  # skip if this is Sanskrit
  if rec.is_sanskrit():
   continue
  key = rec.key()
  if key in d:
   print "Occurs twice:",rec.line.encode('utf-8')
  d[key]=rec
 return d

def make_txtfun(filein,filein1,fileout):
 # slurp txt file into list of lines
 with codecs.open(filein,encoding='utf-8',mode='r') as f:
  inlines = f.readlines()
 # Determine non-sanskrit snippets 
 nonsand = init_non_sanskrit(filein1)
 print len(nonsand.keys()),"non-sanskrit snippets retrieved from",filein1
 
 # open output file
 fout = codecs.open(fileout,'w','utf-8')
 nlines = len(inlines)
 for idxline in xrange(0,nlines):
  line = inlines[idxline]
  line1 = adjustline(line,idxline,nonsand)
  fout.write(line1 + '\n')
 fout.close()
 # identify anomalies in nonsand usage
 notused=0
 multiused=0
 for key,rec in nonsand.iteritems():
  if rec.used == 0:
   notused=notused+1
   print notused," UNUSED:",rec.line.encode('utf-8')
  elif rec.used > 1:
   multiused=multiused+1
   print multiused," MULTIUSED (%s):"%rec.used,rec.line.encode('utf-8')
 print notused,"nonsand cases were not used"
 print multiused,"nonsand cases were used more than once"

if __name__=="__main__":
 filein = sys.argv[1] # Xadj.txt
 filein1 = sys.argv[2] # italics4.txt, or similar
 fileout = sys.argv[3] #Xadj1.txt
 make_txtfun(filein,filein1,fileout)
