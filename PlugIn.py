import os
import sys

__author__ = "@the_new_sky"
__license__ = "MIT"

class LoadPlugins(object):

    def __init__(self, plugin_dir):

        sys.path.append(os.path.abspath(plugin_dir))

        plugin_list = os.listdir(plugin_dir)
        self.plugin_list = []

        for plugin in plugin_list:
            if not plugin.endswith('__'):
                self.plugin_list.append(os.path.splitext(plugin)[0])

    def import_all(self):
        self.uselist = list(map(__import__, self.plugin_list))

    @property
    def plugins(self):
        return self.uselist
