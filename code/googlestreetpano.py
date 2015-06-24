# https://developers.google.com/maps/documentation/javascript/streetview
# https://maps.googleapis.com/maps/api/streetview?size=800x400&location=Manhattan&fov=90&heading=270
DEFAULT_SIZE = "600x300"
DEFAULT_PITCH = 0
DEFAULT_ROTATIONS = [('North': 0, 'East': 90, 'South':180, 'West': 270)]
DEFAULT_COLLATION = (1, 4)

def make_pano(location, rotations = DEFAULT_ROTATIONS, collation = DEFAULT_COLLATION,
                    size = DEFAULT_SIZE, pitch = DEFAULT_HEADING):



def get_street_view_url(location, size, heading, pitch):

