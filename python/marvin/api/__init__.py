
def parse_params(request):
    """Parses the release from a POST Interaction request."""

    release = request.form['release'] if 'release' in request.form else None
    drver = request.form['drver'] if 'drver' in request.form else None

    return release
