#!/usr/bin/python
import sys
import argparse

parser = argparse.ArgumentParser(prog='MaskMix',description='MaskMix - This tool will convert the output file beagle 3.x files into Masked beagle files MASKING for a specified ancestry')
parser.add_argument('--viterbi','-v',help="Viterbi file",required=True)
parser.add_argument('--markers','-m',help='MArker file in PCAdmix format',required=True)
parser.add_argument('--beagle','-b',help='Beagle file',required=True)
parser.add_argument('--ancestry','-a',help='Index of the ancestry to keep',required=True)
args = vars(parser.parse_args())

def maskMix(viterbi,markers,beagle,ancestry):

    #viterbi="GlobalRecipientsJuhoansiKeptConfidence0.95Ratio0.2.vit"
    #markers="GlobalRecipients.markers"
    #beagle="GlobalRecipientsJuhoansiKeptRatio0.2.bgl"
    
    outName="TestMaskNov.bgl"
    
    '''0.01 Define which ancestry to keep'''

    '''0.1 open files'''
    
    vitfile=open(viterbi,"r")
    markersfile=open(markers,"r")
    beaglefile=open(beagle,"r")
    
    
    
    ninds=0
    with open (viterbi, "r" )as v:    
        for line in v:
            ninds+=1
    
    nsnps=-1
    with open(beagle,"r") as b:
        for line in b:
            nsnps+=1
        
    
    print ("%i individuals found..." %(ninds))
    print ("%i SNPs found..." %(nsnps))
    
    
    windows={}
    with open(viterbi) as v:
        for line in v:
            line=line.strip().split()
            #print(line)
            windows[line[0]]=line[1:]
    
    markerswin={}
    
    with open(markers) as m:
        i=0
        for line in m:
            line=line.strip().split()
            markerswin[i]=line[1:]
            i+=1
    
    final={}
    
    n=0
    for ind in windows:
        l=windows[ind]
        indlist=[]
        for i,a in enumerate (l):
            if a != str(ancestry):
                indlist.append(markerswin[i])
        final[n]={item for sublist in indlist for item in sublist}
        n+=1
    
    markers_list_dict = {}
    for idx, marker in enumerate(final):
        markers_list_dict[marker] = idx
    
    with open (beagle,"r") as b:
        with open (outName,"w") as o:
            i=0
            for line in b:
                line=line.strip().split()
                if i==0:
                    linenew=[item for item in line[2:] for i in range(2)]
                    linenew=line[0:2]+linenew
                    #linenew=line
                    o.write("\t".join(linenew)+"\n")
                    i+=1
                else:
                    sys.stdout.write("Processing marker %i of %i \r" %(i,nsnps))
                    sys.stdout.flush()
                    linenew=line[0:2]
                    for j,l in enumerate(line[2:]):
                        if line[1] in final[j]:
                            l="0"
                        linenew=linenew +[l,l]
                    o.write("\t".join(linenew)+"\n")
                    i+=1


maskMix(args['viterbi'], args['markers'], args['beagle'],args['ancestry'])
                