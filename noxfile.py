# noxfile.py
import nox

nox.options.sessions = []
nox.options.default_venv_backend = "uv"


@nox.session(python="3.11")
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
    session.run("sphinx-build", "-b", "dirhtml", "-v", "source/", "build/")


@nox.session(python="3.11")
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
    session.run("sphinx-build", "-b", "gettext", "-W", "source/", "locales/")


@nox.session(python="3.11")
def lint(session: nox.Session) -> None:
    """
    Not Support CJK!!!
    """
    session.run_install(
        "uv",
        "sync",
        "--frozen",
        "--group",
        "dev",
        env={"UV_PROJECT_ENVIRONMENT": session.virtualenv.location},
    )
    session.run("docstrfmt", "source")
