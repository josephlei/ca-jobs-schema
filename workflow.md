### Use wget to retrieve current classification data pdf from CalHR website
wget -O schema_alphabetic.pdf http://www.calhr.ca.gov/Pay%20Scales%20Library/PS_Sec_15.pdf

### Manually open PDF, copy all, paste into plain text editor, save it
future enhancement to use automation, pdftk, ghostscript, etc.

### Use GREP to throw out all the junk we don't want, headers, titles, etc.
grep -vwE "(Schem Class|Code Full Class Title|Compensation SISA Footnotes AR Crit MCR Prob. Mo. WWG NT CBID|Civil Service Pay Scale - by Class Title|State of California|Pay Scales/CalHR Net: Updated)" schema_alphabetic_raw > schema_alphabetic_cleaned

### Run python to convert to csv file

### Notes to self
* Grep `-v` **inverts** matches
* use `:%s/<Ctrl-V><Ctrl-M>/\r/g` within VIM to replace all the ^M characters with real newlines `\r`, the control characters need to be pressed, not pasted in
* ps2ascii schema_alphabetic.pdf raw.txt
* grep -vwE "(Schem|Class|Civil Service Pay Scale - by Class Title|State of California|Code Full Class Title|Compensation SISA Footnotes AR Crit MCR Prob. Mo. WWG NT CBID|Pay Scales/CalHR Net: Updated)" schema_alphabetic_raw > schema_alphabetic_cleaned