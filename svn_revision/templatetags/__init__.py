def get_revision():
    from os import popen3
    import re, os

    try:
        stIO = popen3('svnversion '+os.path.join(os.path.abspath(os.path.dirname(__file__)), "../../../"))
        outS = stIO[1].read().strip()
        m = re.match(':?(\d*).*[MS]?$', outS);
        errS = stIO[2].read().strip()
        for f in stIO: f.close()

        if errS:
            return errS
        if m:
            return m.group(1) or ' '
    except:
        return 'Versioning Unavailable'

REVISION = get_revision()