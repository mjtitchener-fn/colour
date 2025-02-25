"""
SMPTE 240M
==========

Define the *SMPTE 240M* opto-electrical transfer function (OETF) and
electro-optical transfer function (EOTF):

-   :func:`colour.models.oetf_SMPTE240M`
-   :func:`colour.models.eotf_SMPTE240M`

References
----------
-   :cite:`SocietyofMotionPictureandTelevisionEngineers1999b` : Society of
    Motion Picture and Television Engineers. (1999). ANSI/SMPTE 240M-1995 -
    Signal Parameters - 1125-Line High-Definition Production Systems (pp. 1-7).
    http://car.france3.mars.free.fr/HD/INA-%2026%20jan%2006/\
SMPTE%20normes%20et%20confs/s240m.pdf
"""

from __future__ import annotations

import typing

import numpy as np

from colour.algebra import spow

if typing.TYPE_CHECKING:
    from colour.hints import ArrayLike, NDArrayFloat

from colour.utilities import as_float, domain_range_scale, from_range_1, to_domain_1

__author__ = "Colour Developers"
__copyright__ = "Copyright 2013 Colour Developers"
__license__ = "BSD-3-Clause - https://opensource.org/licenses/BSD-3-Clause"
__maintainer__ = "Colour Developers"
__email__ = "colour-developers@colour-science.org"
__status__ = "Production"

__all__ = [
    "oetf_SMPTE240M",
    "eotf_SMPTE240M",
]


def oetf_SMPTE240M(L_c: ArrayLike) -> NDArrayFloat:
    """
    Define *SMPTE 240M* opto-electrical transfer function (OETF).

    Parameters
    ----------
    L_c
        Light input :math:`L_c` to the reference camera normalised to the
        system reference white.

    Returns
    -------
    :class:`numpy.ndarray`
        Video signal output :math:`V_c` of the reference camera normalised to
        the system reference white.

    Notes
    -----
    +------------+-----------------------+---------------+
    | **Domain** | **Scale - Reference** | **Scale - 1** |
    +============+=======================+===============+
    | ``L_c``    | [0, 1]                | [0, 1]        |
    +------------+-----------------------+---------------+

    +------------+-----------------------+---------------+
    | **Range**  | **Scale - Reference** | **Scale - 1** |
    +============+=======================+===============+
    | ``V_c``    | [0, 1]                | [0, 1]        |
    +------------+-----------------------+---------------+

    References
    ----------
    :cite:`SocietyofMotionPictureandTelevisionEngineers1999b`

    Examples
    --------
    >>> oetf_SMPTE240M(0.18)  # doctest: +ELLIPSIS
    0.4022857...
    """

    L_c = to_domain_1(L_c)

    V_c = np.where(L_c < 0.0228, 4 * L_c, 1.1115 * spow(L_c, 0.45) - 0.1115)

    return as_float(from_range_1(V_c))


def eotf_SMPTE240M(V_r: ArrayLike) -> NDArrayFloat:
    """
    Define *SMPTE 240M* electro-optical transfer function (EOTF).

    Parameters
    ----------
    V_r
        Video signal level :math:`V_r` driving the reference reproducer
        normalised to the system reference white.

    Returns
    -------
    :class:`numpy.ndarray`
         Light output :math:`L_r` from the reference reproducer normalised to
         the system reference white.

    Notes
    -----
    +------------+-----------------------+---------------+
    | **Domain** | **Scale - Reference** | **Scale - 1** |
    +============+=======================+===============+
    | ``V_c``    | [0, 1]                | [0, 1]        |
    +------------+-----------------------+---------------+

    +------------+-----------------------+---------------+
    | **Range**  | **Scale - Reference** | **Scale - 1** |
    +============+=======================+===============+
    | ``L_c``    | [0, 1]                | [0, 1]        |
    +------------+-----------------------+---------------+

    References
    ----------
    :cite:`SocietyofMotionPictureandTelevisionEngineers1999b`

    Examples
    --------
    >>> eotf_SMPTE240M(0.402285796753870)  # doctest: +ELLIPSIS
    0.1...
    """

    V_r = to_domain_1(V_r)

    with domain_range_scale("ignore"):
        L_r = np.where(
            V_r < oetf_SMPTE240M(0.0228),
            V_r / 4,
            spow((V_r + 0.1115) / 1.1115, 1 / 0.45),
        )

    return as_float(from_range_1(L_r))
