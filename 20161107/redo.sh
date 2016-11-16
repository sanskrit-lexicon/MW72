python adjtxt.py ../../orig/mw72.txt mw72adj.txt
python adjtxt_inv.py mw72adj.txt mw72_temp.txt
diff mw72_temp.txt ../../orig/mw72.txt
rm mw72_temp.txt  # don't need this
python italics.py mw72adj.txt ../mw72hw2.txt italics.txt > italics_log.txt
source /c/ejf/pdfs/TM2013/ccs/research/german/pyenchant/Scripts/activate
python italics_eng.py italics.txt italics_eng.txt > italics_eng_log.txt
python display.py italics_eng.txt mw72adj.txt italics_eng_display.txt
python italics_update.py italics.txt italics_corrections.txt italics1.txt
python check_as.py italics1.txt ../as_roman.txt italics1_check_as.txt

python display.py italics1_check_as.txt mw72adj.txt italics1_check_as_display.txt
python italics_update.py italics1.txt italics_corrections1.txt italics2.txt

python check_as.py italics2.txt ../as_roman.txt italics2_check_as.txt

python display.py italics2_check_as.txt mw72adj.txt italics2_check_as_display.txt

python etymology.py italics2.txt mw72adj.txt italics_etymology.txt

python italics_update.py italics2.txt italics_corrections2.txt italics3.txt

python etymology.py italics3.txt mw72adj.txt italics3_etymology.txt

python italics_update.py italics3.txt italics_corrections3.txt italics4.txt > italics4_log.txt

python adjtxt1.py mw72adj.txt italics4.txt mw72adj1.txt > adjust1_log.txt

python check_as1.py italics4.txt ../as_roman.txt italics4_san_as.txt italics4_nonsan_as.txt

python italics_caps.py italics4.txt italics_caps_exceptions.txt

python italics_check1.py italics4.txt italics_check1.txt

python etymology1.py italics4.txt mw72adj1.txt italics_etymology1.txt > italics_etymology1_log.txt
echo "making mw72adj1_roman2.txt"
python adjtxt2.py as,roman2 mw72adj1.txt mw72adj1_roman2.txt > mw72adj1_roman2_prob.txt

echo "making mw72adj1_roman2_ea.txt"

python check_ea.py mw72adj1_roman2.txt mw72adj1_roman2_ea.txt

echo "making mw72adj1_roman2_ea_sanitalics.txt"
python check_ea1.py mw72adj1_roman2.txt mw72adj1_roman2_ea_sanitalics.txt
echo "making italics4_roman2.txt"
python adjtxt2_italics.py as,roman2 italics4.txt italics4_roman2.txt 
echo "making italics4_slp.txt"
python adjtxt3_italics.py roman2,slp italics4_roman2.txt italics4_slp.txt > adjtxt3_italics_log.txt



