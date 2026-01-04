#!/usr/bin/env -S uv run --script

# /// script
# dependencies = ["nox"]
# ///

"""Nox configuration."""

from __future__ import annotations

import nox

PYPROJECT = nox.project.load_toml()
python_versions = nox.project.python_versions(PYPROJECT)

nox.needs_version = ">=2024.4.15"
nox.options.default_venv_backend = "uv"
nox.options.reuse_venv = "yes"


@nox.session
def lint(session: nox.Session) -> None:
    """Lint."""
    session.run(
        "uv",
        "run",
        "--active",
        "prek",
        "run",
        "--all-files",
        "--show-diff-on-failure",
    )


@nox.session(python=python_versions)
def tests(session: nox.Session) -> None:
    """Execute pytest tests."""
    session.run(
        "uv",
        "run",
        "--verbose",
        "--python",
        f"python{session.python}",
        "pytest",
        *session.posargs,
    )


@nox.session(tags=["typing"])
def mypy(session: nox.Session) -> None:
    """Check types with mypy."""
    args = session.posargs or ("tap_google_play",)
    session.run("uv", "run", "--active", "mypy", *args)


@nox.session(tags=["typing"])
def ty(session: nox.Session) -> None:
    """Check types with ty."""
    args = session.posargs or ("tap_google_play",)
    session.run("uv", "run", "--active", "ty", "check", *args)


if __name__ == "__main__":
    nox.main()
