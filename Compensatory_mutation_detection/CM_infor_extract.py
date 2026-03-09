#!/usr/local/bin/python3
# coding=UTF-8
#python *.py *.snp > *.CM.infor

import sys
single_M={}
double_M={}

with open('/home/ND140/cyw/script/CM_mutation_identify/CM_list.txt') as f1:
    next(f1)
    for line in f1:
        line=line.strip().split('\t')
        if '/' in line[0]:
            index_gene1=line[0].split('/')[0]+line[1].split('/')[0]+line[2].split('/')[0]
            index_gene2=line[0].split('/')[1]+line[1].split('/')[1]+line[2].split('/')[1]
            index_gene=index_gene1+'/'+index_gene2
            double_M[index_gene]=line
        else:
            index_gene=line[0]+line[1]+line[2]
            single_M[index_gene]=line


snp_infor=[]
with open(sys.argv[1]) as f1:
    for line in f1:
        line=line.strip().split('\t')
        if line[0][0] != "#":
            snp_infor.append(line[0]+line[1]+line[2])            
            
for i in single_M.keys():
    if i in snp_infor:
        print('\t'.join(single_M[i]))   
for j in double_M.keys():
    if j.split('/')[0] in snp_infor and j.split('/')[1] in snp_infor:
        print('\t'.join(double_M[j]))

