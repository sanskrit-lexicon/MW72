
# See note at bottom for how to run the code.

# adjust the open italics of mw72.txt, so that
# all italic markup is complete in each line
# Use the {%% and %%} new markup for the required extra italic markup
python adjtxt.py ../../orig/mw72.txt mw72adj.txt

# invert the adjustment of adjtxt.  
# The resulting output should be identical to the original mw72.txt
python adjtxt_inv.py mw72adj.txt mw72_temp.txt
diff mw72_temp.txt ../../orig/mw72.txt
[should be no difference] -   True, there is no differe
rm mw72_temp.txt  # don't need this

#  extract the italic text snippets from mw72
L@key1@linenum@type@snippet
'type' is either the empty string, or 
'hw', meaning this is a

python italics.py mw72adj.txt ../mw72hw2.txt italics.txt > italics_log.txt


# Use pyenchant to check for english
In italics.txt, there are still some lurking non-Sanskrit words whose
code is the empty string.  An example is the word 'repeated' which occurs
twice, and was the impetus for this investigation.
  ref: https://github.com/sanskrit-lexicon/CORRECTIONS/issues/314

In italics_eng, such words are filtered by  PyEnchant to recognize English
words.  Of course, some words (eg. 'as' are not only English, but also
used as Sanskrit, for masculine singular ending).  Some some additional
manual filtering will be needed, no doubt.

To use the Pyenchant, we need to activate a virtual environment. On my machine,
this is done (in GitBash) via:
 source /c/ejf/pdfs/TM2013/ccs/research/german/pyenchant/Scripts/activate

python italics_eng.py italics.txt italics_eng.txt > italics_eng_log.txt
There are 246 distinct LONG (more than 2 characters) likely English words;
these are listed in the log file.  The instances (1452) of these likely
English words are in the output file (italics_eng.txt).

# display
This program reads files like italics.txt (or italics_eng.txt), and
extracts records from mw72adj.txt.  The output is used to provide context
for checking the accuracy of classification of italic phrases.

python display.py italics_eng.txt mw72adj.txt italics_eng_display.txt

## reclassification based on italics_eng_display.txt
From context, it is found that most of the snippets in italics_eng_display
are in fact NOT English.  We can use these contextual observations to
provide corrections to the classifications in italics.txt.

For example, the 500+ italics snippets `tum` are in fact part of Sanskrit 
infinitives, and thus are correctly classified in italics.txt as Sanskrit.
The following list shows all the 'English' words found from italics_eng, 
along with the term count. 
In case of those instances determined to be non-Sanskrit, the 
corresponding records (of italic.txt) are shown, with the correction
to the language-type field.
For instance, the 51 cases of italic term 'man' are all Sanskrit EXCEPT
the case at line 121068, which is reclassified as 'Zend'.

tum (506 cases)
vat (53 cases),
man (51), except 
36329@man@169839@Zend@man,
ram (28), except 
26908@pad@121068@Zend@pad,
mad (27), pad (25),van (21), pat (20), yam (20), yoga (20), tan (19), 
para (18), except
26987@para@121966@Zend@para,
27007@parA@122700@Zend@para:
29512@puras@133227@Zend@para,
sat (17),lag (14), mat (14) , mantra (13),  'yoga as' (13), 'man a' (12), 
pal (12), guru (11), sad (11), tantra (11), 'tantra am' (11), duh (10), 
karma (10), khan (10), dam (9). lap (9), mas (9), rush (9), tap (8), dad (7), 
has (7), mud (7), mush (7), push (7), sap (7), soma (7), tat (7), hum (6), 
plush (6), rap (6), tush (6), gal (5), him (5), jam (5), lip (5), 
paras (5), pare (5), vis (5), ahas (4), bind (4), divas (4), dram (4), 
guru us (4), lamb (4), mantra as (4), mid (4), 
pan (4),  except
52532@sUpa@260795@Sax@pan.
'van a' (4), Brahma (3), 'ash am' (3), bah (3), bid (3), dos (3), gad (3), 
lash (3), mama (3), 
par (3), except
29732@pf@135924@Zend@par,
29806@pF@136684@Zend@par,
'sad t' (3), sate (3), shin (3), 
the (3) , Except 
29708@pUrva@135634@Eng1@the
37472@mImAMsA@179196@Eng1@the
51742@sANKya@254016@Eng1@the
and (2), ante (2), ark (2), ash (2), bad (2), 
ban (2), except
39139@raB@191493@Goth@ban:
54519@hvf@271891@Goth@ban:
barb (2), bas (2), 
bis (2), except
23100@dvis@101903@Zend@bis;
bud (2), except
34778@buD@156799@Zemd@bud,
bus (2), 
fer (2), except
30106@pra@137663@Germ@fer,
35714@Bf@164908@Lat@fer
gala (2), 
hail (2), except
22564@duh@97327@Scot.@hail,
47380@Sri@236296@Goth@hail:
hard (2), except
53828@ha@267947@Eng1@hard
kit (2), except
40512@lI@199849@Sax@lam.
lam (2), 
mar (2), except
37776@mf@181311@Zend@mar,
mash (2), 
mask (2), 
mate (2), 
may (2), 
parka as (2), 
per (2), except
27007@parA@122704@Lith@per,
30106@pra@137660@Umbr@per,
pita (2), except
29243@pitf@131245@Zend@pita,
pro (2), except
30106@pra@137665@Lith@pro,
put (2), 
rat (2), 
repeated (2), except
43110@vinistap@213019@Eng1@repeated
55066@nistap@272761@Eng1@repeated
rip (2), 
sag (2), except
47565@Svan@237438@Pers@sag.
sham (2), 
sip (2), 
soma as (2), 
sun (2), except
26264@nI@116836@Slav@sun,
52545@sUrya@260929@Sax@sun.
tar (2), except
12693@eka@41571@Hib@tar,
22568@duhitf@97340@Germ@tar;
tram (2), 
trap (2), 
villa (2), 
vita (2), 
yak (2), 
Brahman (1), except
1397@aDvaryu@6807@Eng1@Brahman
Cerberus (1), except
38395@yama@186112@Eng1@= Cerberus?
Flora (1), except
34237@Pal@152934@Lat@Flora:
Kali (1), 
September October (1), except
41896@vAra@208362@Eng1@September, October,
Soma (1), 
a fortiori (1), 
4943@kEmutikanyAya@272550@Lat@a fortiori.
a name (1), 
39644@rudra@195374@Eng1@a name
a posteriori (1), 
47116@Seza@235058@Lat@a posteriori
after (1), 
51640@saha@253297@Eng1@after
aha (1), 
aha am (1), 
aha as (1), 
aha id (1), 
aim (1), 
14939@kuYc@52939@Hib@aim,
anal (1), 
1886@anila@8186@Irish@anal
another word (1), 
20342@tad@82090@Eng1@another word;
ant (1), 
anti (1), 
ape (1), 
approach (1), 
4968@aBisArin@16547@Eng1@approach
aves (1), 
bale (1), 
band (1), 
bar (1), 
35714@Bf@164903@Zend@bar,
bash (1), 
birch (1), 
35699@BUrja@164800@Eng1@birch;
bright (1), 
35942@BrAj@166344@Eng1@bright:
brim (1), 
35910@Bram@166134@Iceland@brim,
brow (1), 
35976@BrU@166491@Eng1@brow;
bust (1), 
can (1), 
21308@tfh@87377@Goth@can;
cars (1), 
15589@kf@55926@Lat@cars
chin (1), 
41324@varAha@204860@Hib@chin.
coal (1), 
329@aNgAra@3172@Eng1@coal
coin (1), 
47565@Svan@237437@Hib@coin;
col (1), 
15576@kUla@55738@Hib@col,
day (1), 
dead (1), 
22090@dA@93108@Brit@dead,
dips (1), 
dive (1), 
drum (1), 
20155@qa@81235@Eng1@drum,
eat (1), 
958@ad@5376@Eng1@eat;
eke (1), 
emission (1), 
44399@visarga@219017@Eng1@emission
external (1), 
52373@su@258269@Eng1@external
far (1), 
7821@A@25480@Eng1@far.
feel (1), 
10043@I@32769@Eng1@feel.
full (1), 
10135@u@33062@Eng1@full.
gala am (1), 
garb (1), 
ghat (1), 
give (1), 
16976@ga@62977@Eng1@give.
gram (1), 
had (1), 
hall (1), 
halts (1), 
12693@eka@41575@Them@halts,
ham (1), 
ham ho (1), 
hand (1), 
54020@hasta@269260@Eng1@hand.
haste (1), 
hat (1), 
hate (1), 
have (1), 
hay (1), 
his is is is (1), 
hog (1), 
45988@Sakuni@227439@Danish@hog;
hone (1), 
46397@SARa@230354@Eng1@hone;
hoof (1), 
46099@SaPa@228535@Eng1@hoof.
hum as (1), 
hut t t t (1), 
idem (1), 
imam (1), 
inch (1), 
20086@Ya@81057@Eng1@inch;
kart (1), 
keep (1), 
13236@ka@43819@Eng1@keep
kid (1), 
kill (1), 
9821@i@31475@Eng1@kill
kin (1), 
lab (1), 
lava (1), 
lay (1), 
leaf left (1), 
40595@luB@200237@Sax@leaf, left:
made (1), 
mall (1), 
mandate (1), 
manta as (1), 
men (1), 
23459@DU@104629@Lat@men:
mind (1), 
minute (1), 
mus (1), 
must (1), 
net (1), 
nod (1), 
not (1), 
37283@mAs@178103@Germ@not:
our (1), 
12998@O@43220@Eng1@our.
pad t (1), 
pall (1), 
pampas (1), 
para am (1), 
para paras (1), 
para vat (1), 
paras b (1), 
paras g (1), 
paras l (1), 
paras r (1), 
paras v (1), 
parasol (1), 
38848@yoga@189076@Eng1@parasol
path (1), 
pin (1), 
port (1), 
30676@prati@140019@Lat@port
pram (1), 
pus (1), 
quote (1), 
13512@kaT@45210@Eng1@quote;
rad (1), 
radius (1), 
39096@rad@191343@Lat@radius;
ran (1), 
rap lap (1), 
ray (1), 
rev (1), 
saliva (1), 
51444@salila@252644@Lat@saliva;
samba (1), 
seam (1), 
52273@siv@257029@Engl@seam:
shah (1), 
shun (1), 
47643@za@237950@Eng1@shun.
shut (1), 
sic (1), 
51921@sAman@255041@Lat@sic
sin (1), 
53631@svayam@266793@Hib@sin,
so ham (1), 
song (1), 
18074@Na@70637@Eng1@song
span (1), 
stave (1), 
steer (1), 
53201@sTUrin@264352@Eng1@steer:
step (1), 
stiff (1), 
52996@stabDa@263077@Eng1@stiff.
sumo (1), 
38378@yam@185906@Lat@sumo
sup (1), 
52532@sUpa@260794@Norse@sup;
tale (1), 
tau (1), 
that (1), 
till (1), 
tip (1), 
tor (1), 
21311@tF@87430@Hib@tor,
triplex (1), 
21548@tri@88733@Lat@triplex
true (1), 
20088@wa@81066@Eng1@true,
trump (1), 
try (1), 
uphill loophole (1), 
34201@Pa@152760@Eng1@uphill, loophole.
velum (1), 
44656@vf@220214@Lat@velum,
versus (1), 
44700@vft@220531@Lat@versus;
very (1), 
2163@anudAtta@8922@Eng1@very
visa (1), 
walk (1), 
41552@valg@206007@Eng@walk.
wan (1), 
15589@kf@55925@Germ@wan,
yo ham (1), 



## italics1.txt
This is an updated classification of the records in italics.txt, based
upon the italics_corrections.txt file.  This file currently is just
comprised of the 'exceptions' shown above.

python italics_update.py italics.txt italics_corrections.txt italics1.txt

## check_as
python check_as.py italics1.txt ../as_roman.txt italics1_check_as.txt

python display.py italics1_check_as.txt mw72adj.txt italics1_check_as_display.txt
This generates another set of corrections:
italics_corrections1.txt
python italics_update.py italics1.txt italics_corrections1.txt italics2.txt

python check_as.py italics2.txt ../as_roman.txt italics2_check_as.txt

python display.py italics2_check_as.txt mw72adj.txt italics2_check_as_display.txt

As of now, the items in italics2_check_as.txt are ok. There are 7 cases:
- prau7ga (5 cases) diaresis
- N2  (1 case) (upper-case retroflex nasal)
- N4  (1 case) (upper-case guttural nasal)


## prepare updatebyline correction records 
NOTE: 11/7/2016. These changes have been installed to mw72, and
this program should not be rerun (change01.txt should be left unchanged)
python prep_change.py italics2_check_as.txt ../../orig/mw72.txt change01.txt



## 'etymology' sections
Numerous other languages are mentioned in the 'etymology' section of mw72.
Such a section has the form [cf. xxxx], over several lines.  There may be
non-etymology sections of the same form.  
There are 7622 such [cf. xxxx] cases.

Within these sections, there are italic-snippets for many languages,
only rarely sanskrit.

Many of these have been correctly identified previously, as per italics2.txt.
However, it is believed that there are many still unidentified non-sanskrit
italics snippets lurking in these etymology sections.

python etymology.py italics2.txt mw72adj.txt italics_etymology.txt

The italics_etymology display shows the italicized snippets that occur within
etymology sections; it further analyzes these as follows.
For snippets whose 'type' field is unassigned, several attempts are made
to analyze the type as sanskrit, and type codes such as SAN1, SAN1A, etc
are auto-assigned.   Further, after taking these automatic type assignments
into account, each etymology group of snippets is analyzed to determine
whether all the snippets have been assigned a type-code.   The output 
is sorted  by completed type code.  The last group is classified as TODO,
because for each case in the group there is at least one untyped snippet.

These TODO cases were examined and type codes developed manually.
These are included in the italics_corrections2.txt file. The installation
of these corrections start with italics2.txt and result in italics3.txt

python italics_update.py italics2.txt italics_corrections2.txt italics3.txt

python etymology.py italics3.txt mw72adj.txt italics3_etymology.txt

With these corrections, the classification of italic snippets within
etymology sections ([cf. ... ]) is now considered complete, since there are no
TODO sections within italics3_etymology.txt.

Further, the classification of snippet types in italics3.txt is now 
considered complete.  To make things a bit easier to understand, it seems
adviseable to make one additional set of corrections, namely all those
auto-assigned Sanskrit italic snippets identified by etymology.py.
These are put into italics_corrections3.txt and applied to italics3.txt,
resulting in a final italics4.txt (there are 4606 of these).

python italics_update.py italics3.txt italics_corrections3.txt italics4.txt > italics4_log.txt

The italics4_log.txt file has frequency counts of all the italic snippet categories.
The salient points for now are the Sanskrit snippet categories:
summary of Sanskrit snippets
 175438
SAN 629
SAN1 3673
SAN1A 114
SAN1B 194
SAN1C 67
SAN2 555
hw1 25827
hw2 29546
Total Sanskrit snippets: 236043

Total non-Sanskrit snippets: 5533

We plan to incorporate this binary classification of italic snippets (into
Sanskrit and non-Sanskrit) into the markup of mw72.txt.

* mw72adj1.txt

Thus, from mw72adj.txt and italics4.txt we will construct another version,
mw72adj1.txt, of the digitization. This construction could be done variously.
Our choice is to change the markup for the non-Sanskrit snippets only;
rather than {%...%} we use <nsi>...</nsi> for non-Sanskrit snippets. 
('nsi' is acronym for  'non sanskrit italic').
So Sanskrit snippets will continue to be marked as {%...%}.

Note 1: in mw72adj.txt, we added markup '{%%' and '%%}' at the beginning
and end of lines so that each line would be 'closed' in terms of italicized
markup.  34239 of the lines of mw72adj.txt are changed by this.
We chose to use the double percent '%%' so that the added
markup would be distinguishable from that in mw72.txt.  However,
in mw72adj1.txt, we feel comfortable in removing this distinction, and
will not use the '%%'.

Note 2: The use of 'nsi' tag in mw72adj1.txt will have to be taken into
account when construction mw72.xml (and will require a change to mw72.dtd).
This may necessitate a change in programs that display mw72.xml (the Basic
Display, etc.)

python adjtxt1.py mw72adj.txt italics4.txt mw72adj1.txt > adjust1_log.txt
 The log shows that in 6 lines, the markup for a given non-sanskrit snippet
 occurs 2 or 3 times.  These were checked individually, and appear to be
 legitimate.


* mw72adj2.txt
We are now going to construct a version of the digitization where the
AS (so-called Anglicized Sanskrit) coding is changed.
In the printed work, this coding is used to represent the version of IAST
used by the author in this work.
This book's IAST is 'non-standard' in several respects, when compared to
current conventions of IAST. When we want to emphasize the differences,
we will use the term MWIAST for the form used in the printed text.

The primary use of MWIAST is to represent Sanskrit words with the English
alphabet, by adding various 'diacritical' marks to English letters.  
In the AS system, these diacritical marks are represented by certain 
numbers following the letters.  
However, the author uses a similar system to represent non-Sanskrit words.

Here is a study of the AS codes used in the italicized snippets, for
both sanskrit and non-sanskrit snippets.
python check_as1.py italics4.txt ../as_roman.txt italics4_san_as.txt italics4_nonsan_as.txt

## Capital letters in Sanskrit italic snippets.
It would be 'nice' to convert all Sanskrit snippets to slp1.  The reason
is that such a form would allow spelling comparisons and analysis.

However, such a conversion would lose some information; namely, the
capitalization that occurs in some MWIAST words.  It is believed that
capitalization occurs ONLY for 'subheadwords' (compounds of major headwords),
and in 'type-2' major headwords.

We need to test this hypothesis.

python italics_caps.py italics4.txt italics_caps_exceptions.txt

This examines all the italic snippets for capital letters, and flags those
where a capital letter occurs in an 'unexpected' place.  The expected 
places are
 - as the first letter in an hw2 snippet
   Example: <P>{%Ra1ji1vini1,%} f. the plant Nelumbium Speciosum.
 - as the first non hyphen letter in any other Sanskrit snippet.
   Example: <>blue-eyed. {%--Ra1ji1va-pr2is4ni, is, is, i,%} Ved. having
Unfortunately, there are numerous irregularities (i.e. exceptions) to this
expected pattern.
 (a) There are many sub-headwords (--Xyz) where the scope of the italic
     markup continues from the prior sub-headword; thus '--Xyz' occurs
     other than at the beginning.  There are about 2500 of these.
     Most could be identified by the pattern 'A. --Xyz', and so could be
     identified and the markup changed to 'A%}. {%--Xyz'.
     Note: This change has now been made as corrections to mw72.txt.
      The changes are within manualByLine03.
     python make_corrections_subheadword.py ../../orig/mw72.txt corrections_subheadword.txt
     cd ../  # get in pywork, the parent directory
     cp manualByLine03.txt prev_manualByLine03.txt
     cat prev_manualByLine03.txt 20161107/corrections_subheadword.txt > manualByLine03.txt
     sh update_sync.sh
     NOTE: There were several 'false positives' in these corrections.
      Adjustments were made manually to manualByLine03.txt so that the
      resulting mw72.xml was valid xml.
 (b) About 150 other cases, capitalization occurs within a Sanskrit Phrase.
These difficulties make it hard to have a lossless transformation to SLP1 for
the italic Sanskrit snippets.

## italics_check1
I keep noticing occasional snippets that are misclassified as Sanskrit.
This program tries to identify such cases.

python italics_check1.py italics4.txt italics_check1.txt

This was fruitful, leading to about 50 corrections, added to 
italics_corrections.txt, and to a few markup corrections in 
pywork/manualByLine03.txt.
These corrections were installed.
When italics_check1 was rerun, it led to about 160 cases, but these
appear to be false positives.

## etymology1
We now should have some ability to distinguish the etymology types.
We will use italics4 and mw72adj1:
python etymology1.py italics4.txt mw72adj1.txt italics_etymology1.txt

By definition, we consider an etymology in mw72adj1 to be a
section that begins with '[cf.' and ends with ']' (excluding [Page...] markup)

Now that we have marked the italic types (per italics4),
we should be able to distinguish etymology sections as:
(a) All sanskrit
(b) All non-sanskrit
(c) A mixture of sanskrit and non-sanskrit.
The (b) and (c) cases should be considered foreign-word etymologies.
Once we are sure of the two classes, we might consider adding markup to
the (much less frequent) foreign-word etymologies.

python etymology1.py italics4.txt mw72adj1.txt italics_etymology1.txt > italics_etymology1_log.txt

Note:  The initial effort to find etymologies also uncovered that there
are several (est. 300) cases where etymologies do NOT have the initial '[cf.'.
For instance, under headword akra :
 <P>1. {%akra, as, a1, am,%} Ved. violent [Lat. <nsi>acer?</nsi>].
etymology1 ignores these, but the log file italics_etymology1_log.txt shows
the instances, in case we want to deal with these cases later.

The identified 'etymology' sections are classified into 4 categories, based
on the language categories of the italicized snippets within the section.
 - EMPTY (228) These are cases with no italicized snippets.  A brief sampling
   suggests these are references to Greek words.
 - SAN (6199)  All italicized snippets are Sanskrit.
 - NONSAN (1000) All italicized snippets are non-Sanskrit
 - MIXED (220)  Some italicized snippets are Sanskrit, some are non-Sanskrit.


# Conversion of AS codes to Roman unicode.
1. Copy as_roman.xml from pywork directory.
2. Tidy it, by removing no-ops: <in>X</in> <out>X<out>
python transcoder_tidy.py as_roman.xml as_roman1.xml
  Note: There are still un-needed transcodings in the file. 
        We'll leave them for now.
3. change the \uxxxx codes in as_roman to their unicode character equivalents.

python transcoder_unicode.py as_roman1.xml as_roman2.xml
4. get the inverse transformation
python transcoder_invert.py as_roman2.xml roman2_as.xml
 Edit roman2_as.xml manually to add a comment.

5. Change as codes in mw72adj1 to roman unicode.
python adjtxt2.py as,roman2 mw72adj1.txt mw72adj1_roman2.txt

273293 lines read from mw72adj1.txt
160099 of these lines are changed in mw72adj1_roman2.txt
179 of these transformations are not invertible

We run this again, this time printing the non-invertible cases to log file.

python adjtxt2.py as,roman2 mw72adj1.txt mw72adj1_roman2.txt > mw72adj1_roman2_prob.txt

Lessons from the non-invertible lines:
1. The text sometimes prints a vowel with the breve diacritic. 
   In the coding of mw72.txt, such vowels are coded as vowel + Ç (capital C with
   cedilla).  
   <in>aÇ</in> <out>ă</out>   \u0103 
   <in>eÇ</in> <out>ĕ</out>    \u0115
   <in>iÇ</in> <out>ĭ</out>   \u012d
   <in>oÇ</in> <out>ŏ</out>    \u014f
   <in>uÇ</in> <out>ŭ</out>   \u016d
2. a10, e10,u10,i10, o10  
   These codes (vowel+circumflex) were missing in as_roman
   <in>a10</in> <out>â</out>  \u00e2
   <in>e10</in> <out>ê</out>   \u00ea
   <in>i10</in> <out>î</out>    \u00ee
   <in>o10</in> <out>ô</out>    \u00f4
   <in>u10</in> <out>û</out>    \u00fb
The additions as shown above are added to as_roman2.xml, and
   roman2_as.xml is regenerated
python transcoder_invert.py as_roman2.xml roman2_as.xml

Then rerun:
python adjtxt2.py as,roman2 mw72adj1.txt mw72adj1_roman2.txt > mw72adj1_roman2_prob.txt

After adjustments, there are no problem codes (the conversion is invertible!).
Also, there are no unconverted AS [letter-number] codes.

## mw72adj1_roman2.txt is equivalent to mw72.txt.
It differs from mw72.txt in two ways:
 - italics:
   - italics are closed in each line in the new version, whereas italics
     span lines in mw72.txt
   - non-sanskrit italics are coded using <nsi>X</nsi> in place of {%X%}
 - AS has been converted everywhere to Roman Unicode.  This is done
   - invertibly
   - with retention of peculiarities of MWIAST (see mwiast-iast.txt)

## remaining awkwardness
Some of the codes that MW72 uses differ from current IAST conventions:
- guttural nasal ń  vs. ṅ  (n-accent vs. n-dot)
   Actually, MW72 uses an 'n + middle-dot-to-right' for guttural nasal
- palatal nasal  ṅ  vs. ñ  (n-dot vs. n-tilde)
- hard palatal ć  vs. ch,  aspirated hard palatal ćh  vs. chh

## examine all extended ascii codes in m272adj1_roman.txt

python check_ea.py mw72adj1_roman2.txt mw72adj1_roman2_ea.txt

There are 207 such extended ascii codes, but this includes Arabic
and Greek, and the special characters used in 'nsi' (non-Sanskrit Italics).

We want to specialize this to EA codes used just in Sanskrit, in particular
 in italicized Sanskrit.  (Note Sanskrit words in MWIAST also occurs
 outside of italicized text --  we currently have no way to identify these.)

python check_ea1.py mw72adj1_roman2.txt mw72adj1_roman2_ea_sanitalics.txt

There were some errors noted, where the unicode left or right single quote
was used in Sanskrit italics where the apostrophe (single quote character )
should be used (for avagraha).  Corrections are generated for these and
everything rerun.
     python make_corrections_quotes.py ../../orig/mw72.txt corrections_quotes.txt
     cd ../  # get in pywork, the parent directory
     cp manualByLine03.txt prev_manualByLine03.txt
     cat prev_manualByLine03.txt 20161107/corrections_quotes.txt > manualByLine03.txt
     sh update_synch.sh
     cd 20161107
     sh redo.sh

## mwiast.txt extracts the description of 'indo-romanic' equivalents to nagari
letters from page xxviii of the mw72 dictionary.

mwiast-iast.txt  compares mwiast to the IAST as described in
 https://en.wikipedia.org/wiki/International_Alphabet_of_Sanskrit_Transliteration

## italics4_roman2
python adjtxt2_italics.py slp,roman2 italics4.txt italics4_roman2.txt 

## italics4_slp
python adjtxt3_italics.py roman2,slp italics4_roman2.txt italics4_slp.txt > adjtxt3_italics_log.txt

slp_roman2.xml conversion table derived (manually) from mwiast-iast.txt

python transcoder_invert.py slp_roman2.xml roman2_slp.xml
  Then roman2_slp.xml is augmented also based on mwiast-iast.txt

The adjtxt3_italics program's main function is to convert the
  sanskrit italics (of italics4.txt) into slp1.
This is a non-invertible transformation, for various reasons.
The transformation is applied only to the Sanskrit italics snippets of
italics4.txt; the non-sanskrit snippets are NOT written to the output.

For a given Sanskrit snippet, the transformation algorithm first
 lower-cases the snippet, then applies the roman2_slp.xml transcoding.

A check of invertibility (from slp back to roman2) is made.  While there
are many Sanskrit snippets for which the conversion from roman2 to slp and
then back to roman2 is different from the original snippet,  these differences
for the most part of very regular. Here is a tabulation of the 
invertibility status of the Sanskrit italic snippets:
CAP 86827   Difference due to Capitalization in roman2-spellings
CAPṉ,ṁ 2599  Differece due to capitalization (perhaps) and also these nasals.
SAME 148922 These cases are invertible.
TODO 5  These cases are unresolved.  4 of them involve the use of 
    the a-breve ă,  and 1 is case pra-üga.
    (details in adjtxt3_italics_log.txt).


## comment on roman2
Recall that in this document, the roman2 coding system is, by definition, the
same as 'mwiast', at least for italicized Sanskrit. This coding is also 
applied to text not identified as italicized Sanskrit, including
 - text as identified as non-sanskrit italicized text, 
   and marked with <nsi> tag/
 - non-italic text: this is not identified by any markup, it is simply
   generic text in which there is some kind of diacritic; the language
   categories are not known.

We have developed a version of the mw72 digitization (mw72adj1_roman2.txt)
  in which all the original AS coding (letter-number) has been replaced
  by the roman2 coding. This replacement is universal, including both
  Sanskrit italic text, non-Sanskrit italic text, and non-italic text.
  The replacement occurs both in the digitization of the Preface material of
  the dictionary, as well as the body of the dictionary.

We have also developed a version of the Sanskrit italicized snippets,
first in this roman2 coding, and second in the SLP coding. These files are
respectivey italics4_roman2.txt and italics4_slp.txt.

## Pros and cons of modern iast version of mw72

It would be possible to replace the roman2 (mwiast) coding of mw72 with
the modern IAST coding.  The file mwiast-iast.txt describes (at least for
Sanskrit) how this coding would differ from mwiast (roman2).

The main advantage of this would be that the few arcana of the mwiast
coding would be brought to modern standards.

However, there would be several disadvantages to this:
- The preface of the dictionary clearly describes the coding which the
  author has chosen.  If we changed the coding to modern iast, this preface
  material would no longer be accurate.
- Comparison between the digitization and the printed text would be harder.
  With the current roman2 coding of mw72adj1_roman2.txt, a comparison between
  the digitization and the printed text is easy (with the one exception of
  the palatal nasal, which roman2 represents as ṅ (n with dot above) in place
  of the non-unicode-supported n-with-middle-right-dot). 
  All of the differences between mwiast and iast indicated in mwiast-iast.txt
  would have to be 'remembered' when comparing the digitization with the text.
- We would have to deal with the non-italic text. Currently, the roman2
  coding applies to non-italic text as well as italic text.  For non-Sanskrit
  text, whether italicized or not, it is probably better to retain the roman2
  coding.  Since we do not know whether a given non-italic text with a diacritic
  represents Sanskrit or non-Sanskrit, we could be inappropriately
  applying modern iast (which refers to Sanskrit only) to non-Sanskrit text.

It certainly would be possible to add markup to the digitization to make all
  the necessary distinctions so that modern iast could be applied solely to
  Sanskrit, while retaining the roman2 coding for non-Sanskrit text.  But the
  development of this markup and applying it uniformly to the digitization would
  likely be another quite lengthy task.

My current opinion is that we should make mw72adj1_roman2.txt the standard
form of the mw72 digitization now and going forward; in other words, it 
will be the new mw72.txt.
- it is demonstrably equivalent to the current digitization
- it improves the markup of italic text, and in particular allows the
  distinction between Sanskrit and non-Sanskrit italic text (via the <nsi> tag).
- it replaces the AS coding with roman2 coding, thereby facilitating comparison
  between the digitization and the printed text.

If we decide to make this large change to the base form of the mw72 
digitization, it will be necessary to alter the programs which extract the
headwords (resulting in mw72hw2.txt) and which construct the xml form and
which display the xml form (Basic display).  I do not foresee any major
obstacles to implementing these changes.

It would be possible to modify either the xml form and/or the display forms
to display Sanskrit italicized text in modern IAST.  This could be done if
we decide it would be helpful to users.  I am undecided whether this should
be done, but wanted to mention that it could be done.

## examination of italicized Sanskrit
The italics4_slp.txt file has all the italicized Sanskrit nicely isolated
and ready to form the basis of further studies.  Two uses which come to mind 
are:
- n-gram and other analyses to search for spelling errors.
- Sub-headword identification

One important detail which may come into play, certainly for sub-headword
studies, is the hyphenation of words due to line breaks.  The mw72 digitization
represents each line of the text with a line of the digitization.  Thus,
reconstituting an entire word requires using two lines of the digitization
(and similarly two lines of the italics4 file).

# How to run the code
The redo.sh file regenerates everything that needs to be regenerated.
It assumes the following directory structure:
mw72 (parent)
 - orig  (the home of mw72.txt)
 - pywork (python code)
   - 20161107 (this directory)
 - web  (not used in this work; contains displays for mw72)

This github directory was copied from a local version of mw72 downloaded
from a backup of the sanskrit-lexicon web site directories, and was put
as xampp/htdocs/cologne/mw72 in a local (Windows OS) copy of xampp.
