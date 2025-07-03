Hello!

This repo contains Python code written for the University of Michigan-Dearborn 2025 REU in Spectral Theory and CR Geometry.

bases_for_spherical_harmonics.ipynb generates polynomial bases for spherical harmonics of bidegree $(p,q)$ using the complex Newton Potential. 

degeneracy_table_generator.ipynb generates degeneracy tables for quotient spaces. For a quotient space under the action of a group $G$, we look at the space $H_{p,q}^G$ of $G$-invariant
harmonic homogeneous polynomials of bidegree $(p,q)$, and we find its dimension using a Taylor expansion of the Ikeda generating function. A degeneracy table simply 
shows these dimensions for various bidegrees. These tables can take a while to generate, so we linked our code to a database of tables that we've generated.

Kaggle dataset: https://www.kaggle.com/datasets/tanvikiran27/degeneracy-tables-for-sphere-quotients

If you're brave enough to work with APIs, you can use the code in degeneracy_tables_with_api.ipynb as a starting point to be able to add your own tables to the dataset. There are links to several helpful resources in the comments throughout the code.

Thank you, and we hope this is helpful!
