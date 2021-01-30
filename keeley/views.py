from flask import request, render_template, current_app
from flask.views import View


def robots_txt():
    """Serve the robots.txt file to manage the indexing of the site by search engines."""
    return current_app.send_static_file("robots.txt")


def file_operations():
    """Show a list of all repos. Can be sorted by last update and repo names can be searched."""
    repos = [repo.freeze() for repo in current_app.valid_repos.values()]
    invalid_repos = current_app.invalid_repos.values()

    order_by = request.args.get("order_by") or "last_updated"
    search_query = request.args.get("q") or ""

    if search_query:
        repos = [r for r in repos if search_query.lower() in r.namespaced_name.lower()]
        invalid_repos = [
            r
            for r in invalid_repos
            if search_query.lower() in r.namespaced_name.lower()
        ]

    if order_by == "name":
        sort_key = lambda repo: repo.namespaced_name
    else:
        sort_key = lambda repo: (
            -(repo.fast_get_last_updated_at() or -1),
            repo.namespaced_name,
        )

    repos = sorted(repos, key=sort_key)
    invalid_repos = sorted(invalid_repos, key=lambda repo: repo.namespaced_name)

    return render_template(
        "repo_list.html",
        repos=repos,
        invalid_repos=invalid_repos,
        order_by=order_by,
        search_query=search_query,
        base_href=None,
    )


class DownloadView(BaseRepoView):
    """Download a repo as a tar.gz file."""

    def get_response(self):
        basename = "%s@%s" % (
            self.context["repo"].name,
            sanitize_branch_name(self.context["rev"]),
        )
        tarname = basename + ".tar.gz"
        headers = {
            "Content-Disposition": "attachment; filename=%s" % tarname,
            "Cache-Control": "no-store",  # Disables browser caching
        }

        tar_stream = dulwich.archive.tar_stream(
            self.context["repo"],
            self.context["blob_or_tree"],
            self.context["commit"].commit_time,
            format="gz",
            prefix=encode_for_git(basename),
        )
        return Response(tar_stream, mimetype="application/x-tgz", headers=headers)


download = DownloadView.as_view("download", "download")


def upload():
    pass


def get_image():
    pass

