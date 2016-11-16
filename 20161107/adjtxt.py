# coding=utf-8
""" adjtxt.py
  Modifies mw72. Primarily, it 'closes' the italic text on each line

"""
#import xml.etree.ElementTree as ET
import sys, re,codecs

def closeitalic(line):
 """ Add closing italic at end of line, taking account of [Page...]
     Line has the form
     ...{%...   no closing italic
     if line has form
     ...{%...[Page...]$  
     we change to
     ...{%...%%}[Page...]
     otherwise, just append %%} to end of line
 """
 if '[Page' in line:
  line = line.replace('[Page','%%}[Page')
 else:
  line = line + '%%}'
 return line

def adjustline(line,openitalic,idxline):
 line = line.rstrip('\r\n') # maybe already done by readlines 
 if openitalic:
  # This line has an open italic from a previous line
  # Put an opening italic.  
  # assume line starts with <>
  assert line.startswith('<>'),"line %s doesn't start with <>\n%s"%(idxline,line.encode('utf-8'))
  line=line.replace('<>','<>{%%')
  if '%}' in line:
   # this line closes the previous openitalic
   openitalic = False
  else:
   # there is an open italic from previous line, 
   #but this line does not close it
   line = closeitalic(line)
   return (line,openitalic)
 # we know openitalic is False.
 # Search for a new openitalic in this line
 m = re.search(r'({%[^}]*)$',line)
 if m:
  # we need to close the open italic, and set openitalic to True
  line = closeitalic(line)
  openitalic=True
 # whether m is found or not, we are ready to return
 return (line,openitalic)


def make_txtfun(filein,fileout):
 # slurp txt file into list of lines
 with codecs.open(filein,encoding='utf-8',mode='r') as f:
    inlines = f.readlines()
 # open output file
 fout = codecs.open(fileout,'w','utf-8')
 openitalic=False  # when some prior line has an 'open' {% italic
 nlines = len(inlines)
 for idxline in xrange(0,nlines):
  line = inlines[idxline]
  (line,openitalic) = adjustline(line,openitalic,idxline)
  fout.write(line + '\n')
 fout.close()

if __name__=="__main__":
 filein = sys.argv[1] # X.txt
 fileout = sys.argv[2] #Xadj.txt
 make_txtfun(filein,fileout)
