
'''
This script will parse the output of ldd command. So, at first, use
`ldd binary_file > ldd.txt` to get the dependent libraries. Then ,
use `python parse_ldd.py` to parse the results to find the attributes
of all these shared libraries. 
'''

import os
import re
import magic
import subprocess

f=open("ldd.txt", "r")
f2=open("file.txt","w")
while(1):
	line=f.readline()
	match=re.search('(.*)(\=\>)(.*)(\(.*\))',line)
	if match:
		groups=match.groups()
		filename=os.path.realpath(groups[2].strip())
		p = subprocess.Popen(['file', filename], stdout=subprocess.PIPE,stderr=subprocess.PIPE)
		out, err = p.communicate()
		f2.write(out)
		print out

	if not line:
		break

f.close()
f2.close()





