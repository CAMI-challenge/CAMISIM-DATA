#!/usr/bin/python

import io
import sys
import ast

fname = sys.argv[1]
t = ast.literal_eval(sys.argv[2])
f = open(fname)

name_count = {}
vals = {}
for line in f:
	if line.startswith("Assemblies"):
		continue
	s = line.split() #splits results and name
	if t:
		name = s[0] + " " + s[1]
		val = s[2]
	else:
		name = s[0]+" "+fname.split('/')[1] #gets name
		val = s[1]
	if name in name_count:
		name_count[name] += 1
		vals[name].append(val)
	else:
		name_count[name] = 1
		vals[name] = [val]
f.close()

if t:
	nvals = {}
	for n in vals:
		tot = n.rsplit('_',2)
		a = tot[0]
		b = tot[1].lstrip()
		if a in nvals:
			nvals[a].extend([(n,float(ast.literal_eval(g)[0])) for g in vals[n]])
		else:
			nvals[a] = [(n,float(ast.literal_eval(g)[0])) for g in vals[n]]
	for a in nvals:
		con_an = 'NA'
		str_an = 'NA'
		con_ev = 'NA'
		str_ev = 'NA'
		for val in nvals[a]:
			name = val[0].split()
			if name[1].startswith("quast_con"):
				if name[0].split('_')[-1].startswith("ancestor"):
					con_an = val[1]
				else:
					con_ev = val[1]
			else:
				if name[0].split('_')[-1].startswith("ancestor"):
					str_an = val[1]
				else:
					str_ev = val[1]
		nvals[a] = [con_an,str_an,con_ev,str_ev]
	toWrite = "strain\tancestor consensus\tevolved consensus\tancestor strain\tevolved strain\n"
	for a in nvals:
		toWrite += "%s\t%s\t%s\t%s\t%s\n" % (a,nvals[a][0],nvals[a][1],nvals[a][2],nvals[a][3])
	print toWrite
else:
	for n in vals:
		print "%s\t%s" % (n,vals[n])

#print nvals

#print len(vals)
