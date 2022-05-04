from nox import session


@session(reuse_venv=True)
def test(session):
    session.install("-e.[test]")
    session.run("pytest")
