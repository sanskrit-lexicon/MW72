# coding=utf-8
""" italics.py
 extract italic text from mw72adj.txt
"""
#import xml.etree.ElementTree as ET
import sys, re,codecs
import operator

non_sanskrit_misc=[
 "stairno;",
 "uched,",
]
langcodes=[
 'Sax', # Angl. Sax.
 'Arab',
 'Arm', 'Armor', # Armorican
 'Armen',
 'Boh','Bohem', # Bohemian
 'Bret',
 'Cambro-Brit','Brit', # the language of Wales.
 'Dor', #Doric
 'Eng', 'Engl',
 'Gae7l', 
 'Germ',
 'Goth',
 'Hib',
 'Hind', # Hindi
 'Icel',
 'Ion',
 'Island', # German form of Icelandic
 'Lat',
 'Lett', # Lettish
 'Lith', 'Lit', #Lithuanian - Lit may be typo 
 'Osc','Osk', # Oscan or Oskan
 'Osset',
 'Pol',
 'Pra1k',
 'Pruss',
 'Russ',
 'Sabin', # Sabine or Sabellian
 'Sax', # Saxon
 'Scot',
 'Slav',
 'Umbr',
 'Zend', # sometimes missing '.'
]
class Snippet(object):
 def __init__(self,m,prevline):
  m1 = re.search(r'\W([A-Z][a-z0-9-]+)[.] *$',m.group(1))
  if m1:
   temp = m1.group(1)
   if temp in langcodes:
    self.hwtype=temp
   else:
    self.hwtype=''
  else:
   self.hwtype=''
  self.txt=m.group(2)

  # override
  if self.txt in non_sanskrit_misc:
   self.hwtype=''

def smart_match(line,prevline):
 """ Currently, prevline is unused
     There is a known flaw in the logic,
     namely with the first {%..%} group
     is preceded ON THE PREVIOUS LINE
     by one of the language codes,
     the current logic does not pick up that language code as hwtype.
     Thus, such examples are (wrongly) assumed to be Sanskrit.

 """
 reg=r'([^{]*){[%]+(.*?)[%]+}'
 snippets=[]
 icase=0
 for m in re.finditer(reg,line):
  s=Snippet(m,prevline)
  snippets.append(s)
  icase = icase+1
 return snippets

def check_ending_langcode(prevline,line,linenum):
 m1 = re.search(r'\W([A-Z][a-z0-9-]+)[.] *$',prevline)
 if not m1:
  return ''   
 temp = m1.group(1)
 if temp not in langcodes:
  return ''
 # potential problem with first italic in line
 if False:  # initial debugging
  print
  out = 'CHKa:%s:%s' %(linenum-1,prevline)
  print out.encode('utf-8')
  out = 'CHKb:%s:%s' %(linenum,line)
  print out.encode('utf-8')
 return temp  # use as revised hwcode

def construct_italics(datalines,key1,lnum,page,n1):
 # n1 is index of first line
 datalines1 = []
 fout=None
 # parse head info from first line
 line = datalines[0]
 line = line.strip()
 line0 = line

 regex1 = u'^(<P>[.]{#.*?#}¦ *[0-9]?)(.*)$'
 regex1a = r' *{%(.*?)[%]+}(.*)$'
 regex2 = r'^<P>[0-9]?.? *{%(.*?)[%]+}(.*)$'
 m1 = re.search(regex1 ,line)
 if m1:
  rest = m1.group(2)
  m1a = re.search(regex1a,rest)
  if not m1a:
   print "Unexpected headword 1 @ linenum",n1+1,"line=",line.encode('utf-8')
   hwtype=None
  else:
   hwtype='hw1'
   hwtxt = m1a.group(1)
   rest = m1a.group(2)
 else:
  m2 = re.search(regex2 ,line)
  assert m2,"Unexpected headword 2: %s"%line.encode('utf-8')
  hwtype='hw2'
  hwtxt = m2.group(1)
  rest = m2.group(2)
 if hwtype:
  datalines1.append((hwtype,hwtxt,n1+1))
 hwtype=''  # for all the rest
 datalines[0] = rest
 reg=r'{[%]+(.*?)[%]+}'
 preg = re.compile(reg)
 prevline=''
 for idx in xrange(0,len(datalines)):
  line = datalines[idx]
  snippets = smart_match(line,prevline)
  #snippets = re.findall(reg,line)
  linenum = n1+idx+1
  # Test for previous line ending in a langcode
  newhwtype=check_ending_langcode(prevline,line,linenum)
  idxs=0
  for s in snippets:
   if (idxs == 0) and (newhwtype != ''):
    # mark with the newhwtype, annotate with asterisk
    datalines1.append((newhwtype+'*',s.txt,linenum))
   else:
    datalines1.append((s.hwtype,s.txt,linenum))
   idxs = idxs + 1 # update index of italics
  prevline = line #update prevline
 return datalines1

def make_txtfun(filein,filein1,fileout):
 # slurp txt file into list of lines
 with codecs.open(filein,encoding='utf-8',mode='r') as f:
    inlines = f.readlines()
 # open output text file
 fout = codecs.open(fileout,'w','utf-8')
 nout = 0
 # read headword lines, and generate output
 f = open(filein1,'r')
 n = 0 # count of lines read
 lnum = 0 # generate record number for xml records constructed
 cats = {} # dictionary to count italic types
 for line in f:
  n = n+1
  if n > 1000000:
   print "debug stopping"
   break
  line = line.strip() # remove starting or ending whitespace
  try:
   (pagecol,hwslp,linenum12) = re.split('[:]',line)
  except:
   print "Problem at line %s = %s" %(n,line)
   exit(1)
  (linenum1,linenum2) = re.split(',',linenum12)
  (page,col) = re.split('[,-]',pagecol)
  #col = 1 # there is no column 
  n1 = int(linenum1) - 1 # make 0-based
  n2 = int(linenum2) - 1
  datalines = inlines[n1:n2+1]
  # construct output
  lnum = lnum + 1  # computed L code
  key1 = hwslp
  italics = construct_italics(datalines,key1,lnum,pagecol,n1)
  for (itype,txt,linenum) in italics:
   out = '%s@%s@%s@%s@%s' % (lnum,key1,linenum,itype,txt)
   fout.write(out + '\n')
   nout = nout+1
   if itype not in cats:
    cats[itype]=0
   cats[itype] = cats[itype]+1
 fout.close()
 print nout,"lines written to",fileout
 # print cats
 sorted_cats = sorted(cats.items(), key=operator.itemgetter(1))
 for (cat,count) in sorted_cats:
  print "%s %d" %(cat,count)

if __name__=="__main__":
 filein = sys.argv[1] # X.txt
 filein1 = sys.argv[2] # Xhw2.txt
 fileout = sys.argv[3] #
 make_txtfun(filein,filein1,fileout)
