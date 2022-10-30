from ..hooks import pm
from .hookspec import CollectorHookspec

# Register the hookspec for Collector
pm.add_hookspecs(CollectorHookspec)

from .router import router