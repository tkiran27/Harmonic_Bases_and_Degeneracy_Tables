Hello!

This Jupyter notebook contains functions to generate polynomial bases for spherical harmonics of bidegree 
$(p,q)$ using the Newton Potential. 

It can also generate degeneracy tables for lens spaces. For a given lens space, we look at the space ($H_{p,q}^G$) of 
harmonic homogeneous polynomials of bidegree $(p,q)$ that are invariant under the corresponding group action $G$,
and we find its dimension using a Taylor expansion of the Ikeda generating function. A degeneracy table simply shows these
dimensions for various bidegrees.

We transfered our code to a Kaggle notebook so that the resulting expressions would be typeset nicely. It also worked out
quite well for the degeneracy tables. These can take a while to generate, so we linked our code to a database that stores the
tables once they are generated: https://www.kaggle.com/datasets/tanvikiran27/degeneracy-tables/data
