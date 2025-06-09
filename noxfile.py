# noxfile.py
import nox

nox.options.sessions = []
nox.options.default_venv_backend = "uv"


@nox.session()
def docs(session: nox.Session) -> None:
    """
    Make the website
    """
    session.run_install(
        "uv",
        "sync",
        "--frozen",
        "--group",
        "docs",
        env={"UV_PROJECT_ENVIRONMENT": session.virtualenv.location},
    )
    session.run("sphinx-build", "-b", "html", "-W", "source/", "build/")


@nox.session()
def translation(session: nox.Session) -> None:
    """
    Build the gettext .pot files
    """
    session.run_install(
        "uv",
        "sync",
        "--frozen",
        "--group",
        "docs",
        env={"UV_PROJECT_ENVIRONMENT": session.virtualenv.location},
    )
    session.run("sphinx-build", "-b", "gettext", "-W", "source", "locales")
