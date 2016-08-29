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
			nvals[a].extend([(n,int(ast.literal_eval(g)[0])) for g in vals[n]])
		else:
			nvals[a] = [(n,int(ast.literal_eval(g)[0])) for g in vals[n]]
	for a in nvals:
		con_an = False
		str_an = False
		con_ev = False
		str_ev = False
		if len(nvals[a]) < 4:
			for val in nvals[a]:
				name = val[0].split()
				if name[1].startswith("quast_con"):
					if name[0].split('_')[-1].startswith("ancestor"):
						con_an = True
					else:
						con_ev = True

				else:
					if name[0].split('_')[-1].startswith("ancestor"):
						str_an = True
					else:
						str_ev = True
		else:
			con_an = True
			str_an = True
			con_ev = True
			str_ev = True
		ex = [con_an,str_an,con_ev,str_ev]
		v = []
		pos = 0
		for b in ex:
			if b:
				v.append(nvals[a][pos])
				pos += 1
			else:
				v.append(('NA','NA'))
		nvals[a] = v
	toWrite = "strain\tancestor consensus\tevolved consensus\tancestor strain\tevolved strain\n"
	for a in nvals:
		toWrite += "%s\t%s\t%s\t%s\t%s\n" % (a,nvals[a][0][1],nvals[a][2][1],nvals[a][1][1],nvals[a][3][1])
	print toWrite
else:
	for n in vals:
		print "%s\t%s" % (n,vals[n])

#print nvals

#print len(vals)
