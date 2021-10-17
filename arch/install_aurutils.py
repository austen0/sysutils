from pathlib import Path
from subprocess import run
from tempfile import TemporaryDirectory


GIT_CLONE_URL = 'https://aur.archlinux.org/aurutils.git'
TEMPDIR = Path(TemporaryDirectory().name)
TEMPDIR.mkdir()
run(['git', 'clone', 'https://aur.archlinux.org/aurutils.git', TEMPDIR])
run(['makepkg', '-si', '--needed'], cwd=TEMPDIR)
