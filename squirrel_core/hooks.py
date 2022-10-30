from pluggy import HookspecMarker, HookimplMarker, PluginManager

pm = PluginManager("squirrel-core")
hookspec = HookspecMarker("squirrel-core")
hookimpl = HookimplMarker("squirrel-core")