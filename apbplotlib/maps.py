import cartopy.crs as ccrs


class EASE2_North(ccrs.Projection):
    """
    Projection class for NSIDC EASE-Grid 2.0 North

    See Brodzik, M. J., B. Billingsley, T. Haran, B. Raup, M. H. Savoie. 2014. EASE-Grid 2.0: Incremental but Significant Improvements for Earth-Gridded Data Sets. ISPRS International Journal of Geo-Information 2012, 1, 32-45 & correction in 2014, 3, 1154-1156.

    Uses the default Globe object which is WGS84
    """

    def __init__(self):

        proj4_params = {
            'proj': 'laea',
            'lat_0': 90.,
            'lon_0': 0.,
            'x_0': 0,
            'y_0': 0,
            'ellps': 'WGS84',
            #'towgs84': 0,0,0,0,0,0,0,
            'units': 'm',
            'no_defs': ''
            }

        super(EASE2_North, self).__init__(proj4_params)

    @property
    def boundary(self):
        coords = ((self.x_limits[0], self.y_limits[0]),(self.x_limits[1], self.y_limits[0]),
                  (self.x_limits[1], self.y_limits[1]),(self.x_limits[0], self.y_limits[1]),
                  (self.x_limits[0], self.y_limits[0]))

        return ccrs.sgeom.Polygon(coords).exterior

    @property
    def threshold(self):
        return 1e5

    @property
    def x_limits(self):
        return (-4500000.0, 4500000.0)

    @property
    def y_limits(self):
        return (-4500000.0, 4500000.0)

    def describe(self):
        for k, v in vars(self).items():
            print (f'{k}: {v}')

            
# Original EASE North projection class
class EASE_North(ccrs.Projection):
    '''Projection class for NSIDC EASE grid north'''
    
    def __init__(self):

        # see: http://www.spatialreference.org/ref/epsg/3408/
        proj4_params = {'proj': 'laea',
            'lat_0': 90.,
            'lon_0': 0,
            'x_0': 0,
            'y_0': 0,
            'a': 6371228,
            'b': 6371228,
            'units': 'm',
            'no_defs': ''}

        super(EASE_North, self).__init__(proj4_params)

    @property
    def boundary(self):
        coords = ((self.x_limits[0], self.y_limits[0]),(self.x_limits[1], self.y_limits[0]),
                  (self.x_limits[1], self.y_limits[1]),(self.x_limits[0], self.y_limits[1]),
                  (self.x_limits[0], self.y_limits[0]))

        return ccrs.sgeom.Polygon(coords).exterior

    @property
    def threshold(self):
        return 1e5

    @property
    def x_limits(self):
        return (-9030575.88125, 9030575.88125)
        #return (-9000000, 9000000)

    @property
    def y_limits(self):
        return (-9030575.88125, 9030575.88125)
        #return (-9000000, 9000000)

    def describe(self):
        for k, v in vars(self).items():
            print (f'{k}: {v}')

            
# Grid class
class Grid:

    def __init__(self, grid_params):
        self.extent = grid_params['extent']
        self.limit = grid_params['limit']
        self.origin = grid_params['origin']
        self.projection = grid_params['projection']

    def describe(self):
        for k, v in vars(self).items():
            print (f'{k}: {v}')
        

class Nh50km(Grid):

    def __init__(self):

        grid_params = {
            'extent': [-9036842.762500, 9036842.762500,
                       -9036842.762500, 9036842.762500],
            'limit': 3000000,
            'origin': 'upper',
            'projection': EASE_North()
            }

        super(Nh50km, self).__init__(grid_params)

