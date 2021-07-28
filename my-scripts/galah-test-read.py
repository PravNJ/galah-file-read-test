from specutils import Spectrum1D
import matplotlib.pyplot as plt
import matplotlib as mpl
from matplotlib.backends.backend_pdf import PdfPages
from matplotlib import gridspec
from mpl_toolkits.axes_grid1 import make_axes_locatable
import numpy as np
import pandas as pd
import matplotlib.ticker as plticker
from astropy.stats import sigma_clip
from astropy.time import Time
import requests
import re
from io import BytesIO
from astropy import units as u
from pyvo.dal.ssa  import search, SSAService

