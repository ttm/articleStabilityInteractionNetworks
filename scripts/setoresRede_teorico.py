#-*- coding: utf8 -*-
from __future__ import division
import numpy as n, pylab as p, networkx as x, random as r, collections as c, string
from scipy import special # special.binom(x,y) ~ binom(x,y)

__doc__="""Script to plot both scale-free network and random network distributions."""

N=1200

# for the free scale network
# P(k) = \beta *  k^(-\alpha), with \alpha typically in (2, 3)
kk=n.arange(N)
Pk=.10*kk**(-10.5)

# for the random network
# P(k) = (N-1 k)p^k(1-p)^(N-k)
p_=.1
Pk_=special.binom(N-1, kk)*(p_**kk)*((1-p_)**(N-kk))

#p.plot(n.log(kk),n.log(Pk));p.plot(n.log(kk),n.log(Pk),"ro",label="free-scale model")
#p.plot(n.log(kk),n.log(Pk_));p.plot(n.log(kk),n.log(Pk_),"bo",label="Edos-Renyi model")

#F=p.gcf()
#F.set_size_inches((10.,3.))
#F.set_figwidth(10.)
p.figure(figsize=(10.,3.))
p.subplots_adjust(left=0.06,bottom=0.32,right=0.99,top=0.86)
p.plot(n.log(kk),n.log(Pk),label="scale-free model", linewidth=3)
p.plot(n.log(kk),n.log(Pk_),label=u"Erdös-Rényi model", linewidth=3)
p.text(0.9,-70,"periphery"  ,size=25)
p.text(3.6,-100,"intermediary",size=25)
p.text(5.9,-110,"hubs"      ,size=25)
p.title(u"Three sections of a scale-free network",size=25)
p.legend()
p.xlabel(r"$\log(k)\;\rightarrow$",size=25)
p.ylabel(r"$\log(P(k))\;\rightarrow$",size=25)
p.yticks(())
p.xticks(())
p.xlim((-0.1,n.log(N)+1))
p.ylim((-150,1))

# pontos de intersecção:
x1=3.7; y=-41.16-5
p.plot((x1,x1),(-1000,y),"r--")
x2=5.4951; y=-60.-5
p.plot((x2,x2),(-1000,y),"r--")
p.xticks((x1,x2),(r"$(k_L)$",r"$(k_R)$"),size=25)

p.savefig("../figs/fser_.png")
#p.show()


#p.plot(kk,Pk) ;p.plot(kk,Pk,"ro")
#p.plot(kk,Pk_);p.plot(kk,Pk_,"bo")
#p.show()
