# coding=utf-8
""" italics_eng.py
 Read hw2 file for AE.  Use en_GB and en_US dictionaries to check
 spelling.  Write lines line hw2, with a 'status' field.


 Requires virtualenv with enchant installed. See readme

 The following English words are in fact used only as Sanskrit words 
 when within italics in mw72:
 tum - infinitive
 vat - suffix, like
 man - suffix , or root 
  Exception: #Zend 36329@man@169839@@man,
 man a - (end in man, 'a' = n.singular. karman a n,)
 ram - root, etc.
 mad - root, pron. (asmat)
 pad - root, 
  Exception: # 26908@pad@121068@@pad,  (Zend {%pad,%}
 van - root, sfx
 pat - root, noun pad
 frons ? # 28304@parRa@126498@@pat,
 yam - root, sfx (ya)
 yoga 
 yoga as  (yoga, with m. nom. sing. end in as)
 tan - root 
 para - pronoun
   Exception: Zend 27007@parA@122700@@para:
              Zend 26987@para@121966@@para,
              Zend 29512@puras@133227@@para,
 sat - noun
 lag - root
 mat - sfx, form of pron. asmad
 mantra - noun, Denom. verb
 pal - root
 guru - noun.
 sad - root
 tantra - noun, Denominative verb
 tantra am - noun, with n. nom. sing. ending
 duh - root (? Why was this in dictionary of English words?
 karma - noun Question: in 15589@kf@55786@@karma,, what is 'Let2' ? grammar?
 khan - root 
 dam - root
 lap - root
 mas - root (why English? pl. of 'ma' (mother))
 rush - root  (= slp1 ruz)
 tap - root
 dad - (related to root dA)
 has - root 
 mud - root
 mush - root (= slp1 muz)
 push - root (= slp1 puz)
 sap - root
 soma - noun 
 tat - pron tad (rare Eng. word - make lace with knots)
 hum - noun (mystical syllable)
 plush - root (= slp1 pluz)
 rap - root
 tush - root (= slp1 tuz)
 gal - root
 him - noun (a sound)
 jam - root 
 lip - root 
 paras - indeclineable
 pare - forms of para 
 vis - root 
 ahas - form of ahan
 bind - root 
 divas - form of div (day)
 dram - root 
 guru us - noun m.sg. 
 lamb - root 
 mantra as - noun m.sg.
 mid - root 
 pan - root Except. #Sax 52532@sUpa@260795@@pan.
 van a - sfx with n.sg. 
 Brahma - noun
 ash am - related to azwa, n.sg. 
 bah - root 
 bid - root 
 dos - noun
 gad - root 
 lash - root = slp1 laz
 mama - gen. of asmad
 par - root Exception: #Zend 29732@pf@135924@@par,
            Exception: #Zend 29806@pF@136684@@par,
 sad t - noun m.sg.
 sate - verb ending (pre. A. 3s)
 shin - sfx. = slp1 zin
 the - Appears to be English in all 3 cases
 and - root 
 ante - loc. of anta
 ark - root 
 ash - abbreviated part of Sanskrit word
 bad - Gothic in both cases
 ban - root, sfx 
 barb - root 
 bas - root 
 bis - root. Exception #Zend 23100@dvis@101903@@bis;
        Latin 101904 <>{%bis, dis-%} in {%dis-cedo%} &c.; probably also Goth.
 bud - root Exception: #Zemd 34778@buD@156799@@bud,  NOTE TYPO
 bus - root 
 fer - One is German, another Latin
  Also, these are Latin
164908 <>{%%fer%} in {%belli-fer, fer-cu-lu-m, fer-a1x, for-du-s,%%}
164909 <>{%%far, far-i1na, fer-ti-li-s, for(t)-s, for-tu1-na, for-%%}
 
 gala - noun
 hail - other langs. See also
236295 <>{%%hlidh, hlœ-dre, hlœ-der, hold, hal:%} Goth. {%hlains,%%}
236296 <>{%%hlei-thra, hlija, hulth,%} (perhaps) {%hail:%} Lith. {%kle†-%%}
236297 <>{%%tis,%} a room in the uppermost part of a house; {%kle-%%}
 
 hard - 1 is San, another English 
 kit - 
 lam - 1 is San, other Angl. Sax.
 mar - 1 is San, other Zend
181311 <>{%%marti;%} [cf. Zend {%mar,%} ‘to die;’ {%mare-ta,%} ‘mortal;’
181312 <>{%maretan,%} ‘man:’ Gr. <g></g>

 mash - root 
 mask - root 
 mate - verb ending
 may - root 
 parka as - noun m.sg.
 per - both other lang.
122703 <>{%for:%} Old Germ. {%far-, fer:%} Mod. Germ. {%ver-:%}
122704 <>Lith. {%par-,%} ‘back, again;’ {%per,%} ‘through:’ Hib.
122705 <>{%frea, far-,%} ‘back, again.’]
137659 <>{%provi1na:%} Umbr. {%pru = pro; pre = prœ; perne,%}
137660 <>‘in front;’ {%pernaio,%} ‘ancient;’ {%per,%} ‘for (?):’ Goth.
137661 <>{%fru-ma,%} ‘first;’ {%frum-ist,%} ‘at first;’ {%fairra,%} ‘far:’
 pita - 1 San, other Zend
131245 <>Zend {%pita,%} base {%pa-tar:%} Gr. <g></g>
131246 <>Lat. {%pa-ter, Jup-piter:%} Goth. {%fa-dar:%} Old
 pro - 1 is San, other Lith
137664 <>{%pra-, pro-,%} ‘before;’ {%priÇ-vy,%} ‘first:’ Lith. {%pra-,%}
137665 <>‘before;’ {%pro,%} ‘through, for;’ {%pir-ma-s,%} ‘first;’
137666 <>{%pirm,%} ‘before:’ Hib. {%fur,%} ‘for;’ {%foir,%} ‘before;’
 put - related to putra
 rat - sfx
 repeated - English
 rip - root 
 sag - 1 is Persiaon
237437 <>gen. {%szuns;%} Hib. nom. {%cu,%} gen. and pl. {%coin;%} Russ.
237438 <>{%sobaka%} (for {%shaka%}); Pers. {%sag.%}] {%--S4va-kishkin, i1,%%}
 sham - word endin (slp1 zam)
 sip - gram. term?
 soma as - noun m.sg.
 sun - Slav, Sax.
 tar - Hib, Germ
041570 <>‘any;’ {%neach,%} ‘any one, one, some one, he;’ {%neach-%%}
041571 <>{%%tar,%} ‘neither;’ {%neachdarach,%} ‘neutral:’ Gr. <g>ἑκάτερος</g>
041572 <><g>ἕκα-τος</g> Lat. {%œquus, c-ocles%} fr. {%e10c-ocles:%}

 tram - noun ending
 trap - root 
 villa - noun ending
 vita - noun ending
 yak - sfx
 Brahman -  English ?
 Cerberus - English use of Latin term
 Flora - Lat
 Kali - noun (capitalized)
 September October - Eng1 Also 'ber'?
208362 <>‘once;’ {%ber%} in {%September, October,%} &c.] {%--Va1ra-%%}
 Soma - English? or capitalized Sanskrit
 a fortiori - Latin
 a name - Eng
 a posteriori - Lat
 after - Eng
 aha - noun ahan
 aha am - noun ahan
 aha as - noun ahan
 aha id - ahan
 aim - Hibernian
 anal - Irish
 another word - English
 ant - root 
 anti - noun
 ape - root apa + i
 approach - English
 aves - root form of vid
 bale -  noun f.du.
 band - root 
 bar - Zend 
 bash - root 
 birch - English
 bright - English
 brim - Icelandic
 brow - English
 bust - root 
 can - Goth
 cars - Latin
 chin - Hibernian
 coal - English
 coin - Hibernian
 col - Hibernian
 day - root 
 dead - Cambro-Brit
 dips - root form
 dive - loc. of div
 drum - English
 eat - English
 eke - pl. of eka
 emission - English
 external - English
 far - Eng1
 feel - Eng1 also
032768 <>corresponding to {%i%} long, and having the sound of {%ee%}
032769 <>in {%feel.%} [Page0143-b+ 73]

 full - Eng1
033062 <>vowel of the alphabet, pronounced as the {%u%} in {%full.%%}
 gala am - root 
 garb - noun n.sg.
 ghat - noun
 give - Eng1
062977 <>bet, the soft guttural having the sound of {%g%} in {%give.%%}
 gram - noun
 had - root 
 hall - noun
 halts - Them?
 ham - noun
 ham ho - noun
 hand - Eng1
 haste - noun loc.sg.
 hat - mahat
 hate - verb ending
 have - verb form
 hay - root 
 his is is is - barhis noun
 hog - Danish
 hone - Eng1
 hoof - Eng1
 hum as - noun m.sg
 hut t t t - noun, with endings for 3 genders
 idem - pron.
031873 <>{%%ea, id,%} and {%idem;%} the regular forms are partly de-
 
 imam - pron
 inch - English
081057 <>has much the sound of {%n%} in {%inch;%} when preceding
081058 <>{%j, jh,%} much the sound of {%n%} in {%singe. --Na-ka1ra, as,%}

 kart -  
 keep - English
043819 <>sound to {%k%} in {%keep%} or {%king. --Ka-ka1ra, as,%} m. the
 kid - pron
 kill - English
 kin - pron
 lab - Sanskrit 
 lava - noun
 lay - root 
 leaf left - Ang. Sax
 made - loc. of mada
 mall - root 
 mandate - verb form
 manta as - noun ending, m.sg.
 men - Latin
 mind - root 
 minute - verb form
 mus - root 
 must - Sanskrit stem?
 net - indeclineable
 nod - indeclineable
 not - German
 our - English, also 'ou' in
043220 <>alphabet, having the same sound as {%ou%} in {%our.%}
 pad t - noun,
 pall - root 
 pampas - Denom. root
 para am - pron.
 para paras - pron.
 para vat - pron.
 paras b - abbrev.
 paras g - abbrev.
 paras l - abbrev.
 paras r - abbrev.
 paras v - abbrev.
 parasol - English
 path - noun (slp1 paT)
 pin - noun ending
 port - Latin
140018 <>{%red-%} as in {%red-dere, red-ire; re-%} as in {%re-ferre;%%}
140019 <>{%%prœ%} for {%prai; por, pol, pos%} for {%port%} in the forms
140020 <>{%por-rigo, pol-liceor, pol-lus, pos-sides:%} Old Slav.
 pram - suffix
 pus - root 
 quote - English, also quoth
045210 <>Eng. {%quoth%} and {%quote;%} Gr. <g>κωτίλος, κωτίλλω.</g>]
 rad - root 
 radius - Latin
 ran - root 
 rap lap - root 
 ray - root 
 rev - root 
 saliva - Latin
 samba - root ?
 seam - root 
 shah - in 'nfzah'
 shun - Eng1 also 'sh'
237950 <>to {%sh%} in the English word {%shun.%} (Many roots which
 shut - noun sfx (maDuzut)
 sic - Latin
 sin - Hibernian, also siom
266794 <>‘that, there;’ {%siom,%} ‘they, them:’ Cambro-Brit. {%hun,%}
 so ham - Sanskrit: so'ham 
 song - root , also 'ng' in
070637 <>that of {%ng%} in {%song%}. -- {%N4a-ka1ra, as,%} m. the letter or
 span - root 
 stave - verb form
 steer - English
 step - root 
 stiff - English
 sumo - Lat also 
185906 <>{%sumo%}), {%sub-imo, demo%} (for {%de-imo%}): Lith. {%immu,%}
 sup - Norse, also Germ. sufan, saufjan
260794 <>{%%sufan, saufjan;%} Old Norse {%sup;%} Angl. Sax. {%su-%%}
 tale - loc.sg. of tala
 tau - 1du of tad
 that - Aorist verb end (Tat)
 till - root 
 tip - root 
 tor - Hibernian, also 
087430 <>Hib. {%toir,%} ‘a pursuit;’ {%tor,%} ‘a pursuer;’ {%toramh,%}
087431 <>‘pursuit;’ {%toras,%} ‘a journey;’ {%teirin,%} ‘a descent;’
 triplex - Latin
 true - English, also 't'
081066 <>it has much the sound of {%t%} in {%true,%} but properly pro-
 trump - root 
 try - cpd form of 'tri'
 uphill loophole - ENglish, also 'ph'
152760 <>said to be pronounced like {%ph%} in {%uphill, loophole.%%}
 velum - Latin, also
220215 <>{%%velare; verus, valeo, valor; velle:%} Old Germ.
 versus - Latin
 very - English
 visa - noun
 walk - English
 wan - German
 yo ham - yaH aham

"""
import sys, re,codecs
import enchant
import collections # requires Python 2.7+


class Italics(object):
 def __init__(self,line):
  line = line.rstrip('\r\n')
  self.line=line
  (self.lnum,self.key1,self.linenum,self.itype,self.txt) = line.split('@')

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

def tokenize(s0):
 """
 """
 # Use only letters and numbers and '-'
 s = re.sub(r'[^a-zA-Z0-9-]',' ',s0)
 # Split on sequences of space characters
 tokens = re.split(r' +',s)
 tokens = [t for t in tokens if t!='']
 if False:
  out = ' :: '.join(tokens)
  out = '%s => %s => %s' %(s0,s,tokens)
  print out.encode('utf-8')
 return tokens

def check1(filein,fileout):
 dictnames = ['en_GB','en_US']
 dictrefs = [enchant.Dict(d) for d in dictnames]
 n=0
 fout = codecs.open(fileout,'w','utf-8')
 italics = init_italics(filein)
 # counters
 c = collections.Counter() 
 cshort = collections.Counter() 
 nout = 0
 for rec in italics:
  n=n+1
  if rec.itype != '':
   continue
  #c.update(['ALL'])
  words = tokenize(rec.txt)
  if len(words) == 0:
   continue
  found=True # Are all words English?
  for word in words:
   for idict in xrange(0,len(dictnames)):
    try:
     found = dictrefs[idict].check(word)
    except:
     out = "pyenchant error: word=%s, dict=%s, line=%s" %(word,dictnames[idict],rec.line)
     print out.encode('utf-8')
     exit(1)
    if not found:
     break
   if not found:
    break
  if not found:
   continue # Not English
  #words_str = ','.join(words)
  #c.update([rec.txt])
  shortwords = [w for w in words if len(w)<=2]
  cshort.update(shortwords)
  longwords = [w for w in words if len(w)>2]
  if len(shortwords)==len(words):
   continue
  c.update(longwords)
  rec.itype = 'Eng1'
  out = '%s@%s@%s@%s@%s' % (rec.lnum,rec.key1,rec.linenum,rec.itype,rec.txt)
  fout.write(out + '\n')
  nout = nout+1
 fout.close()
 print nout,"records written to",fileout
 print len(c.keys()),"distinct LONG English phrases"
 for status in sorted(c.keys()):
  out = "%s,%s" % (status,c[status])
  print out.encode('utf-8')
 print len(cshort.keys()),"distinct SHORT English phrases (skipped)"
 for status in sorted(cshort.keys()):
  out = "%s,%s" % (status,cshort[status])
  print out.encode('utf-8')

if __name__=="__main__":
 filein = sys.argv[1] # extract
 #dictname = sys.argv[3] # german_words dictionary prefix for enchant
 fileout = sys.argv[2] # ok
 check1(filein,fileout)

