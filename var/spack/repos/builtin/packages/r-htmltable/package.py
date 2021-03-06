# Copyright 2013-2018 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class RHtmltable(RPackage):
    """Tables with state-of-the-art layout elements such as row
    spanners, column spanners, table spanners, zebra striping, and
    more. While allowing advanced layout, the underlying css-structure
    is simple in order to maximize compatibility with word processors
    such as 'MS Word' or 'LibreOffice'. The package also contains a
    few text formatting functions that help outputting text
    compatible with HTML/'LaTeX'."""

    homepage = "https://CRAN.R-project.org/package=htmlTable"
    url      = "https://cran.rstudio.com/src/contrib/htmlTable_1.11.2.tar.gz"
    list_url = "https://cran.r-project.org/src/contrib/Archive/htmlTable"

    version('1.11.2', '473e6d486e7714f8dd7f16a31480c896')
    version('1.9', '08c62c19e1ffe570e7d8fa57db5094b9')

    depends_on('r-stringr', type=('build', 'run'))
    depends_on('r-knitr@1.6:', type=('build', 'run'))
    depends_on('r-magrittr@1.5:', type=('build', 'run'))
    depends_on('r-checkmate', type=('build', 'run'))
    depends_on('r-htmlwidgets', type=('build', 'run'))
    depends_on('r-rstudioapi@0.6:', type=('build', 'run'), when="@1.11.0:")
