"""
Requirements Utilities
======================

Define the requirements utilities objects.
"""

from __future__ import annotations

import functools
import shutil
import subprocess
import typing

if typing.TYPE_CHECKING:
    from colour.hints import (
        Any,
        Callable,
        Literal,
    )

from colour.utilities import CanonicalMapping

__author__ = "Colour Developers"
__copyright__ = "Copyright 2013 Colour Developers"
__license__ = "BSD-3-Clause - https://opensource.org/licenses/BSD-3-Clause"
__maintainer__ = "Colour Developers"
__email__ = "colour-developers@colour-science.org"
__status__ = "Production"

__all__ = [
    "is_ctlrender_installed",
    "is_matplotlib_installed",
    "is_networkx_installed",
    "is_opencolorio_installed",
    "is_openimageio_installed",
    "is_pandas_installed",
    "is_pydot_installed",
    "is_tqdm_installed",
    "is_trimesh_installed",
    "is_xxhash_installed",
    "REQUIREMENTS_TO_CALLABLE",
    "required",
]


def is_ctlrender_installed(raise_exception: bool = False) -> bool:
    """
    Return whether *ctlrender* is installed and available.

    Parameters
    ----------
    raise_exception
        Whether to raise an exception if *ctlrender* is unavailable.

    Returns
    -------
    :class:`bool`
        Whether *ctlrender* is installed.

    Raises
    ------
    :class:`ImportError`
        If *ctlrender* is not installed.
    """

    try:  # pragma: no cover
        stdout = subprocess.run(  # noqa: S603
            ["ctlrender", "-help"],  # noqa: S607
            capture_output=True,
            check=False,
        ).stdout.decode("utf-8")

        if "transforms an image using one or more CTL scripts" not in stdout:
            raise FileNotFoundError  # noqa: TRY301
    except FileNotFoundError as exception:  # pragma: no cover
        if raise_exception:
            error = (
                '"ctlrender" related API features are not available: '
                f'"{exception}".\nSee the installation guide for more information: '
                "https://www.colour-science.org/installation-guide/"
            )

            raise FileNotFoundError(error) from exception

        return False
    else:
        return True


def is_matplotlib_installed(raise_exception: bool = False) -> bool:
    """
    Return whether *Matplotlib* is installed and available.

    Parameters
    ----------
    raise_exception
        Whether to raise an exception if *Matplotlib* is unavailable.

    Returns
    -------
    :class:`bool`
        Whether *Matplotlib* is installed.

    Raises
    ------
    :class:`ImportError`
        If *Matplotlib* is not installed.
    """

    try:  # pragma: no cover
        import matplotlib as mpl  # noqa: F401
    except ImportError as exception:  # pragma: no cover
        if raise_exception:
            error = (
                '"Matplotlib" related API features are not available: '
                f'"{exception}".\nSee the installation guide for more information: '
                "https://www.colour-science.org/installation-guide/"
            )

            raise ImportError(error) from exception

        return False
    else:
        return True


def is_networkx_installed(raise_exception: bool = False) -> bool:
    """
    Return whether *NetworkX* is installed and available.

    Parameters
    ----------
    raise_exception
        Whether to raise an exception if *NetworkX* is unavailable.

    Returns
    -------
    :class:`bool`
        Whether *NetworkX* is installed.

    Raises
    ------
    :class:`ImportError`
        If *NetworkX* is not installed.
    """

    try:  # pragma: no cover
        import networkx as nx  # noqa: F401
    except ImportError as exception:  # pragma: no cover
        if raise_exception:
            error = (
                '"NetworkX" related API features, e.g., the automatic colour '
                f'conversion graph, are not available: "{exception}".\nPlease refer '
                "to the installation guide for more information: "
                "https://www.colour-science.org/installation-guide/"
            )

            raise ImportError(error) from exception

        return False
    else:
        return True


def is_opencolorio_installed(raise_exception: bool = False) -> bool:
    """
    Return whether *OpenColorIO* is installed and available.

    Parameters
    ----------
    raise_exception
        Whether to raise an exception if *OpenColorIO* is unavailable.

    Returns
    -------
    :class:`bool`
        Whether *OpenColorIO* is installed.

    Raises
    ------
    :class:`ImportError`
        If *OpenColorIO* is not installed.
    """

    try:  # pragma: no cover
        import PyOpenColorIO  # noqa: F401
    except ImportError as exception:  # pragma: no cover
        if raise_exception:
            error = (
                '"OpenColorIO" related API features are not available: '
                f'"{exception}".\nSee the installation guide for more information: '
                "https://www.colour-science.org/installation-guide/"
            )

            raise ImportError(error) from exception

        return False
    else:
        return True


def is_openimageio_installed(raise_exception: bool = False) -> bool:
    """
    Return whether *OpenImageIO* is installed and available.

    Parameters
    ----------
    raise_exception
        Whether to raise an exception if *OpenImageIO* is unavailable.

    Returns
    -------
    :class:`bool`
        Whether *OpenImageIO* is installed.

    Raises
    ------
    :class:`ImportError`
        If *OpenImageIO* is not installed.
    """

    try:  # pragma: no cover
        import OpenImageIO  # noqa: F401
    except ImportError as exception:  # pragma: no cover
        if raise_exception:
            error = (
                '"OpenImageIO" related API features are not available: '
                f'"{exception}".\nSee the installation guide for more information: '
                "https://www.colour-science.org/installation-guide/"
            )

            raise ImportError(error) from exception

        return False
    else:
        return True


def is_pandas_installed(raise_exception: bool = False) -> bool:
    """
    Return whether *Pandas* is installed and available.

    Parameters
    ----------
    raise_exception
        Whether to raise an exception if *Pandas* is unavailable.

    Returns
    -------
    :class:`bool`
        Whether *Pandas* is installed.

    Raises
    ------
    :class:`ImportError`
        If *Pandas* is not installed.
    """

    try:  # pragma: no cover
        import pandas  # noqa: F401, ICN001
    except ImportError as exception:  # pragma: no cover
        if raise_exception:
            error = (
                f'"Pandas" related API features are not available: "{exception}".\n'
                "See the installation guide for more information: "
                "https://www.colour-science.org/installation-guide/"
            )

            raise ImportError(error) from exception

        return False
    else:
        return True


def is_pydot_installed(raise_exception: bool = False) -> bool:
    """
    Return whether *Pydot* is installed and available. The presence of
    *Graphviz* will also be tested.

    Parameters
    ----------
    raise_exception
        Whether to raise an exception if *Pydot* is unavailable.

    Returns
    -------
    :class:`bool`
        Whether *Pydot* is installed.

    Raises
    ------
    :class:`ImportError`
        If *Pydot* is not installed.
    """

    try:  # pragma: no cover
        import pydot  # noqa: F401

    except ImportError as exception:  # pragma: no cover
        if raise_exception:
            error = (
                '"Pydot" related API features are not available: '
                f'"{exception}".\nSee the installation guide for more information: '
                "https://www.colour-science.org/installation-guide/"
            )

            raise ImportError(error) from exception

    if shutil.which("fdp") is not None:
        return True

    if raise_exception:
        error = (
            '"Graphviz" is not installed, "Pydot" related API features '
            "are not available!"
            "\nSee the installation guide for more information: "
            "https://www.colour-science.org/installation-guide/"
        )

        raise RuntimeError(error)

    return False


def is_tqdm_installed(raise_exception: bool = False) -> bool:
    """
    Return whether *tqdm* is installed and available.

    Parameters
    ----------
    raise_exception
        Whether to raise an exception if *tqdm* is unavailable.

    Returns
    -------
    :class:`bool`
        Whether *tqdm* is installed.

    Raises
    ------
    :class:`ImportError`
        If *tqdm* is not installed.
    """

    try:  # pragma: no cover
        import tqdm  # noqa: F401
    except ImportError as exception:  # pragma: no cover
        if raise_exception:
            error = (
                f'"tqdm" related API features are not available: "{exception}".\n'
                "See the installation guide for more information: "
                "https://www.colour-science.org/installation-guide/"
            )

            raise ImportError(error) from exception

        return False
    else:
        return True


def is_trimesh_installed(raise_exception: bool = False) -> bool:
    """
    Return whether *Trimesh* is installed and available.

    Parameters
    ----------
    raise_exception
        Whether to raise an exception if *Trimesh* is unavailable.

    Returns
    -------
    :class:`bool`
        Whether *Trimesh* is installed.

    Raises
    ------
    :class:`ImportError`
        If *Trimesh* is not installed.
    """

    try:  # pragma: no cover
        import trimesh  # noqa: F401
    except ImportError as exception:  # pragma: no cover
        if raise_exception:
            error = (
                '"Trimesh" related API features are not available: '
                f'"{exception}".\nSee the installation guide for more information: '
                "https://www.colour-science.org/installation-guide/"
            )

            raise ImportError(error) from exception

        return False
    else:
        return True


def is_xxhash_installed(raise_exception: bool = False) -> bool:
    """
    Return whether *xxhash* is installed and available.

    Parameters
    ----------
    raise_exception
        Whether to raise an exception if *xxhash* is unavailable.

    Returns
    -------
    :class:`bool`
        Whether *xxhash* is installed.

    Raises
    ------
    :class:`ImportError`
        If *xxhash* is not installed.
    """

    try:  # pragma: no cover
        import xxhash  # noqa: F401
    except ImportError as exception:  # pragma: no cover
        if raise_exception:
            error = (
                '"xxhash" related API features are not available: '
                f'"{exception}".\nSee the installation guide for more information: '
                "https://www.colour-science.org/installation-guide/"
            )

            raise ImportError(error) from exception

        return False
    else:
        return True


REQUIREMENTS_TO_CALLABLE: CanonicalMapping = CanonicalMapping(
    {
        "ctlrender": is_ctlrender_installed,
        "Matplotlib": is_matplotlib_installed,
        "NetworkX": is_networkx_installed,
        "OpenColorIO": is_opencolorio_installed,
        "OpenImageIO": is_openimageio_installed,
        "Pandas": is_pandas_installed,
        "Pydot": is_pydot_installed,
        "tqdm": is_tqdm_installed,
        "trimesh": is_trimesh_installed,
        "xxhash": is_xxhash_installed,
    }
)
"""
Mapping of requirements to their respective callables.
"""


def required(
    *requirements: Literal[
        "ctlrender",
        "Matplotlib",
        "NetworkX",
        "OpenColorIO",
        "OpenImageIO",
        "Pandas",
        "Pydot",
        "tqdm",
        "trimesh",
        "xxhash",
    ],
) -> Callable:
    """
    Decorate a function to check whether various ancillary package requirements
    are satisfied.

    Other Parameters
    ----------------
    requirements
        Requirements to check whether they are satisfied.

    Returns
    -------
    Callable
    """

    def wrapper(function: Callable) -> Callable:
        """Wrap given function wrapper."""

        @functools.wraps(function)
        def wrapped(*args: Any, **kwargs: Any) -> Any:
            """Wrap given function."""

            for requirement in requirements:
                REQUIREMENTS_TO_CALLABLE[requirement](raise_exception=True)

            return function(*args, **kwargs)

        return wrapped

    return wrapper
