from squirrel_core import __version__ as core_version
from squirrel_core.api import __version__ as api_version

def test_version():
    assert core_version == '0.1.0'
    assert api_version == '0.1.0'
