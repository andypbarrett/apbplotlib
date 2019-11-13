import matplotlib.pyplot as plt
from mpl_toolkits import axes_grid1
import numpy as np

import calendar

def ax_add_colorbar(im, aspect=20., pad_fraction=0.05, **kwargs):
    """Add a vertical color bar to an image plot."""
    divider = axes_grid1.make_axes_locatable(im.axes)
    width = axes_grid1.axes_size.AxesY(im.axes, aspect=1./aspect)
    pad = axes_grid1.axes_size.Fraction(pad_fraction, width)
    current_ax = plt.gca()
    cax = divider.append_axes("right", size=width, pad=pad)
    plt.sca(current_ax)
    return im.axes.figure.colorbar(im, cax=cax, **kwargs)

def hovmoller(x, y, z, cmap=None, norm=None, add_colorbar=False, ax=None, title=None, 
              units=None, cb_extend='neither', cb_units_fontsize=20, cb_label_fontsize=15,
              label_fontsize=15, title_fontsize=25, xlim=None, aspect=1.):
    """
    Plots a Hovmoller for an array
    
    Arguments
    ---------
    x - x-axis values for plot (year)
    y - y-axis values for plot (month)
    z - values for hovmoller
    """

    print (ax)
    
    ny, nx = z.shape
    
    if not ax:
        ax = plt.subplot(111)

    extent = [x.min()-0.5, x.max()+0.5, y.min()-0.5, y.max()+0.5]
    im = ax.imshow(z, cmap=cmap, norm=norm, extent=extent, origin='lower', aspect=aspect)

    if add_colorbar:
        #cbar = plt.colorbar(im, ax=ax, extend=cb_extend)
        cbar = ax_add_colorbar(im, pad_fraction=1.)
        #divider = axes_grid1.make_axes_locatable(ax)
        #cax = divider.append_axes("right", size="1%", pad=0.05)
        #cbar = plt.colorbar(im, cax=cax)
        cbar.ax.tick_params(labelsize=cb_label_fontsize)
        if units: cbar.ax.set_ylabel(units, fontsize=cb_units_fontsize)

    ylabels = [calendar.month_abbr[i].upper() for i in y]
    
    ax.set_yticks(np.arange(1,ny+1,1))
    ax.set_yticklabels(ylabels, fontsize=label_fontsize)

    ax.tick_params(labelsize=label_fontsize)

    if xlim:
        ax.set_xlim(xlim)
        
    if title: ax.set_title(title, fontsize=title_fontsize)
