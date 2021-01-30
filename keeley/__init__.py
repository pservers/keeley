import jinja2
import flask
import httpauth
from keeley import views, utils


KEELEY_VERSION = utils.guess_git_revision() or "1.5.2"


class Keeley(flask.Flask):
    jinja_options = {
        "extensions": ["jinja2.ext.autoescape"],
        "undefined": jinja2.StrictUndefined,
    }

    def __init__(self, dir_path, site_name):
        """(See `make_app` for parameter descriptions.)"""
        self.dir_path = dir_path
        self.site_name = site_name

        flask.Flask.__init__(self, __name__)

        self.setup_routes()

    def create_jinja_environment(self):
        """Called by Flask.__init__"""
        env = super(Keeley, self).create_jinja_environment()
        for func in [
            "force_unicode",
            "timesince",
            "shorten_sha1",
            "shorten_message",
            "extract_author_name",
            "formattimestamp",
        ]:
            env.filters[func] = getattr(utils, func)

        env.globals["KEELEY_VERSION"] = KEELEY_VERSION
        env.globals["SITE_NAME"] = self.site_name

        return env

    def setup_routes(self):
        # fmt: off
        rules = [
            ('robots_txt',      '/robots.txt'),
            ('site_name',       '/api/SiteName'),
            ('file_operations', '/api/FileManager/FileOperations'),
            ('download',        '/api/FileManager/Download'),
            ('upload',          '/api/FileManager/Upload'),
            ('get_image',       '/api/FileManager/GetImage'),
        ]
        # fmt: on
        for endpoint, rule in rules:
            self.add_url_rule(rule, view_func=getattr(views, endpoint))


def make_app(
    dir_path,
    site_name,
    htdigest_file=None,
    require_browser_auth=False,
    disable_write=False,
    unauthenticated_write=False,
):
    """
    Returns a WSGI app with all the features (smarthttp, authentication)
    already patched in.
    :param dir_path: Directories to serve. This can either be a path string
        or dictionary of the following form:
            {
                "name1": "path string",
                "name2": "path string",
                ...
                None: "path string"
            }
    :param site_name: Name of the Web site (e.g. "John Doe's Git Repositories")
    :param require_browser_auth: Require HTTP authentication according to the
        credentials in `htdigest_file` for ALL access to the Web interface.
        Requires the `htdigest_file` option to be set.
    :param disable_write: Disable push support. This is required in case 
        `require_browser_auth` is set, but push should not be supported.
    :param htdigest_file: A *file-like* object that contains the HTTP auth credentials.
    :param unauthenticated_write: Allow push'ing without authentication. DANGER ZONE!
    """
    if unauthenticated_write:
        if disable_write:
            raise ValueError("'unauthenticated_write' set with 'disable_write'")
        if require_browser_auth:
            raise ValueError(
                "Incompatible options 'unauthenticated_write' and 'require_browser_auth'"
            )
    if htdigest_file and not require_browser_auth:
        raise ValueError(
            "'htdigest_file' set without 'require_browser_auth'"
        )
    if not isinstance(dir_path, dict):
        # If repos is given as a flat list, put all repos under the "no name" key
        dir_path = {None: dir_path}

    app = Keeley(dir_path, site_name)
    app.wsgi_app = utils.ProxyFix(app.wsgi_app)

    if require_browser_auth:
        app.wsgi_app = httpauth.DigestFileHttpAuthMiddleware(
            htdigest_file, wsgi_app=app.wsgi_app
        )

    return app
