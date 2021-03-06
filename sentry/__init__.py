import os
from subprocess import check_output

try:
    VERSION = __import__('pkg_resources') \
        .get_distribution('sentry').version
except Exception as e:
    VERSION = 'unknown'


# print(VERSION)

def _get_git_revision(path):
    if not os.path.exists(os.path.join(path, '.git')):
        return None
    try:
        revision = check_output(['git', 'rev-parse', 'HEAD'], cwd=path, env=os.environ)
    except Exception:
        return None
    return revision.strip().decode()


def get_revision():
    if 'SENTRY_BUILD' in os.environ:
        return os.environ['SENTRY_BUILD']
    package_dir = os.path.dirname(__file__)
    chekout_dir = os.path.normpath(os.path.join(package_dir, os.pardir, os.curdir))
    path = os.path.join(chekout_dir)
    if os.path.exists(path):
        return _get_git_revision(path)
    return None


def get_version():
    if __build__:
        return '%s.%s' % (__version__, __build__)
    return __version__


__version__ = VERSION
__build__ = get_revision()


if __name__ == '__main__':
    print(get_version())
    print(__version__)
    print(__build__)
