from __future__ import division, print_function
import numpy as np

#
#
#
def overlap_ni(me, sp1,R1, sp2,R2, **kvargs):
    """
      Computes overlap for an atom pair. The atom pair is given by a pair of species indices
      and the coordinates of the atoms.
      Args: 
        sp1,sp2 : specie indices, and
        R1,R2 :   respective coordinates in Bohr, atomic units
      Result:
        matrix of orbital overlaps
      The procedure uses the numerical integration in coordinate space.
    """
    from pyscf.nao.m_ao_matelem import build_3dgrid
    from pyscf.nao.m_ao_eval_libnao import ao_eval_libnao as ao_eval #_libnao

    grids = build_3dgrid(me, sp1, R1, sp2, R2, **kvargs)

    ao1 = ao_eval(me.ao1, R1, sp1, grids.coords)
    ao1 = ao1 * grids.weights

    ao2 = ao_eval(me.ao2, R2, sp2, grids.coords)

    overlaps = np.einsum("ij,kj->ik", ao1, ao2) #      overlaps = np.matmul(ao1, ao2.T)

    return overlaps
