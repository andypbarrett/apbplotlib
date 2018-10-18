def plot_hovmoller(x, y, z, cmap=None, norm=None, add_colorbar=False, ax=None, title=None, 
                   units=None, cb_extend='neither', cb_units_fontsize=20, cb_label_fonsize=15,
                   label_fontsize=20, title_fontsize=25):
    """
    Plots a Hovmoller for an array
    
    Arguments
    ---------
    x - x-axis values for plot
    y - y-axis values for plot
    z - values for hovmoller
    """
    
    ny, nx = z.shape
    
    if not ax:
        ax = plt.subplot(111)
        
    im = ax.pcolormesh(z, cmap=cmap, norm=norm)
    
    if add_colorbar:
        cbar = fig.colorbar(im, ax=ax, extend=cb_extend)
        cbar.ax.set_yticklabels(cbar.ax.get_yticklabels(), fontsize=cb_label_fontsize)
        if units: cbar.ax.set_ylabel(units, fontsize=cb_units_fontsize)
        
    ax.set_yticks(np.arange(0.5,ny,1.))
    ax.set_yticklabels(['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'], fontsize=label_fontsize)
    ax.set_xticks(np.arange(0.5,nx,5))
    ax.set_xticklabels(x[::5], fontsize=label_fontsize)
    
    if title: ax.set_title(title, fontsize=title_fontsize)
