# coding=utf-8
""" adjtxt_inv.py
 Reads the output of adjtxt, and removed {%% and %%}

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
  line = line.replace('[Page','%%} [Page')
 else:
  line = line + '%%}'
 return line

def unadjustline(line):
 line = line.rstrip('\r\n') # maybe already done by readlines 
 line = line.replace('{%%','')
 line = line.replace('%%}','')
 return line

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
  line = unadjustline(line)
  fout.write(line + '\n')
 fout.close()

if __name__=="__main__":
 filein = sys.argv[1] # X.txt
 fileout = sys.argv[2] #Xadj.txt
 make_txtfun(filein,fileout)
