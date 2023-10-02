import nox
from nox import Session
from nox import session


python_versions = ["3.11"]
nox.options.sessions = ("automation",)


@session(python=python_versions, name="automation")
def automation(session: Session) -> None:
    session.install("poetry")
    session.run("poetry", "install", "--with", "dev", "--with", "nox")

    session.log("### pre-commit ###")
    session.run(
        "pre-commit",
    )

    session.log("### mypy ###")
    session.run(
        "mypy",
        "src/",
        "tests/",
        "noxfile.py",
    )

    session.log("### pytest ###")
    session.run(
        "pytest",
    )
