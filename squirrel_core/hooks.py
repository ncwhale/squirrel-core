from pluggy import HookspecMarker, HookimplMarker, PluginManager
from pytest import hookspec

pm = PluginManager("squirrel-core")
hookspec = HookspecMarker("squirrel-core")
hookimpl = HookimplMarker("squirrel-core")