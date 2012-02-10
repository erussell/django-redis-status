from django import template
from django.core import cache
from django.conf import settings

register = template.Library()

DETAILED_STATS = ('used_memory',
                  'used_memory_human',
                  'used_memory_peak_human',
                  'redis_version',
                  'connected_clients',
                  'keyspace_hits',
                  'keyspace_misses',
                  'mem_fragmentation_ratio',
                  'used_cpu_sys',
                  'used_cpu_user',
                  'expired_keys',
                  'evicted_keys',)

class CacheStats(template.Node):
    """
    Reads the cache stats out of the memcached cache backend. Returns `None`
    if no cache stats supported.
    """
    def render (self, context):
        cache_stats = []
        for cache_name in settings.CACHES.keys():
            client = getattr(cache.get_cache(cache_name), '_client', None)
            if client is not None:
                kw = client.connection_pool.connection_kwargs
                server = 'redis://%s:%s/%s' % (kw['host'], kw['port'], kw['db'])
                stats = dict((k, v) for k,v in client.info().iteritems() if k in DETAILED_STATS)
                stats['key_operations'] = stats['keyspace_hits'] + stats['keyspace_misses']
                stats['maxmemory'] = client.config_get()['maxmemory']
                cache_stats.append((server, stats))
        context['cache_stats'] = cache_stats
        return ''

@register.tag
def get_cache_stats (parser, token):
    return CacheStats()

@register.filter
def prettyname (name):
    return ' '.join([word.capitalize() for word in name.split('_')])
