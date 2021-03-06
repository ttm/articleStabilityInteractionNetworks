#-*- coding: utf8 -*-
from __future__ import division
import numpy as n, pylab as p, networkx as x, random as r, collections as c, string
from scipy import special # special.binom(x,y) ~ binom(x,y)

__doc__="""Script to plot both scale-free network and random network distributions."""

import gmane as g, os, pickle, time as T, numpy as n, pylab as p
ENV=os.environ["PATH"]
import  importlib
from IPython.lib.deepreload import reload as dreload
importlib.reload(g.pca)
importlib.reload(g.loadMessages)
importlib.reload(g.listDataStructures)
importlib.reload(g.timeStatistics)
importlib.reload(g.agentStatistics)
importlib.reload(g.tableHelpers)
importlib.reload(g.networkPartitioning)
importlib.reload(g.networkEvolution)
importlib.reload(g.evolutionTimelines)
#importlib.reload(g.interactionNetwork)
#importlib.reload(g.networkMeasures)
dreload(g,exclude="pytz")
os.environ["PATH"]=ENV

labels={'gmane.comp.gcc.libstdc++.devel':"CPP", 'gmane.linux.audio.devel':"LAD", 'gmane.linux.audio.users':"LAU", 'gmane.politics.organizations.metareciclagem':"MET"}
##print("initializing")
dl=g.DownloadGmaneData('~/.gmane4/')
TT=T.time()
##print("{0:.2f} for initializing download dir initializing".format(T.time()-TT)); TT=T.time()
def pDump(tobject,tfilename):
    with open(tfilename,"wb") as f:
        pickle.dump(tobject,f,-1)
def pRead(tfilename):
    with open(tfilename,"rb") as f:
        tobject=pickle.load(f)
    return tobject

PDIR="/home/r/repos/gmane/tests/pickledir/"
NEs=[] # for evolutions of the networks

for lid in dl.downloaded_lists[:1]:
    label=labels[lid]
    NEs.append(pRead("{}neP{}.pickle".format(PDIR,label)))
    print(label+"{0:.2f} for PICKLE loading evolved PCA structures".format(T.time()-TT)); TT=T.time()
# NEs[0].network_measures[X] have E, N, degrees, etc and my be ok to make network partition
ne=NEs[0] # snapshots ordenados
nm=ne.networks_measures[-1]

# nao achei network partitionings no ne (binario de versao antiga da classe?)
# fazendo o partitionings

np=g.NetworkPartitioning(nm)
#p.subplot(212)
p.figure(figsize=(10.,3.))
p.subplots_adjust(left=0.05,bottom=0.28,right=0.99,top=0.87)


p.bar([i[0]-0.4 for i in np.bins],
        np.empirical_distribution,
        alpha=.4,color="k", label="empirical distribution")
#p.bar(n.log([i[0]-0.5 for i in np.bins]),
#      n.log(  np.empirical_distribution),
#        alpha=.7, label="empirical distribution")
centers=[i[0] for i in np.bins]
binomial_probs=[]
for i, bin_ in enumerate(np.bins):
    llimit=bin_[0]
    rlimit=bin_[1]
    ldegree=np.incident_degrees_[llimit]-1
    rdegree=np.incident_degrees_[rlimit]
    binomial_prob=np.binomial.cdf(rdegree)-np.binomial.cdf(ldegree)
    binomial_probs.append(binomial_prob)
#p.plot(centers,np.binomial.cdf(centers))
#p.plot(centers,binomial_probs,"ro")
p.plot(centers,binomial_probs,"k-.^",label="binomial distribution",linewidth=8,alpha=.8)
#p.plot(n.log(centers),n.log(binomial_probs),"ro",label="binomial distribution")
#p.title("Three sections of a scale-free network"+"\nCPP list, {} messages, {} participants, {} edges".format(
#         ne.window_size, nm.N, nm.E),size=25)
p.title(u"Three sections of a scale-free network",size=25)
p.xlabel(r"k $\rightarrow$",size=20)
#p.xticks(centers)
p.yticks(())
p.xticks((2,7),(r"$k_L$",r"$k_R$"),size=20)
p.ylabel(r"P(k) $\rightarrow$",size=20)

c_=n.array(centers)
pk=c_[1:]**-1.5
#p.plot(centers[1:],.4*pk,"ko")
p.plot(centers[1:],.4*pk,"k-o",label="power-law distribution",linewidth=5,alpha=.8)
p.ylim(0,0.4*pk[0]-0.03)

# pontos de intersecção:
x1=2.5; y=41.16-5
p.plot((x1,x1),(-1000,y),"g--")
x2=7.5; y=60.-5
p.plot((x2,x2),(-1000,y),"g--")
#p.xticks((x1,x2),(r"$(k_L)$",r"$(k_R)$"),size=25)

p.text(-.28,0.12,"periphery"  ,size=20)
p.text(4,.27,"intermediary",   size=20)
p.text(10,.08,"hubs"      ,   size=20)



p.legend()
p.savefig("../figs/fser__.png")
#p.show()
