from flask import request, render_template, current_app
from flask.views import View


def robots_txt():
    """Serve the robots.txt file to manage the indexing of the site by search engines."""
    return current_app.send_static_file("robots.txt")


def file_operations():
    pass


class DownloadView(View):
    """Download a repo as a tar.gz file."""

    def get_response(self):
        # basename = "%s@%s" % (
        #     self.context["repo"].name,
        #     sanitize_branch_name(self.context["rev"]),
        # )
        # tarname = basename + ".tar.gz"
        # headers = {
        #     "Content-Disposition": "attachment; filename=%s" % tarname,
        #     "Cache-Control": "no-store",  # Disables browser caching
        # }
        # tar_stream = dulwich.archive.tar_stream(
        #     self.context["repo"],
        #     self.context["blob_or_tree"],
        #     self.context["commit"].commit_time,
        #     format="gz",
        #     prefix=encode_for_git(basename),
        # )
        # return Response(tar_stream, mimetype="application/x-tgz", headers=headers)
        pass


download = DownloadView.as_view("download", "download")


def upload():
    pass


def get_image():
    pass

