# yamlviewer.py, Copyright (c) 2016, Patrick O'Grady.
#
# MIT License
# 
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
# 
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
#

#
# Read-only tree viewer for Yaml scripts written in PyQt4.  Trees are displayed
# in a lazy manner, meaning that the child contents of an item are added only
# when the user opens the item.  This way the viewer avoids problems with
# trees that have circular dependencies.

# Usage:
#   python yamlviewer.py [yamlfile]

#
# Pressing <F5> reloads the currently displayed file.
#


from PyQt4 import QtCore, QtGui, uic
import os
import sys
import yaml

def debug(msg):
    if False:
        print "DEBUG %s" % msg

class YamlViewer(QtCore.QObject):
    def __init__(self, view, controller, configuration, filename=None):
        super(YamlViewer, self).__init__()
        self._view = view
        self._controller = controller
        self._configuration = configuration
        view.action_Open.activated.connect(self.file_open)
        view.action_Reload.activated.connect(self.re_load)
        view.action_Reload.setShortcut(QtGui.QKeySequence("F5"))
        self._root = view.yaml.invisibleRootItem()
        self._item_map = { }
        self._marker = QtGui.QTreeWidgetItem(["marker"])
        view.yaml.itemExpanded.connect(self.expanded)
        if filename:
            self.load(filename)
    def file_open(self):
        fname = str(QtGui.QFileDialog.getOpenFileName(
                    self._controller,
                    'Open file',
                    self._configuration["directory"]
                ))
        debug("fname=%s." % fname)
        self._configuration["directory"] = os.path.dirname(fname)
        self.load(fname)
    def re_load(self):
        if self._fname:
            self.load(self._fname)
    def populate(self, content, item, ch):
        item.removeChild(ch)
        self._item_map[item] = self.good
        def add(k, v):
            debug("type(v)=%s." % (type(v),))
            if type(v) == dict:
                x = QtGui.QTreeWidgetItem([k,])
                z = QtGui.QTreeWidgetItem(["marker"])
                self._item_map[x] = lambda item, x=x, v=v: self.populate(v, x, z)
                x.addChild(z)
                item.addChild(x)
                return
            if type(v) == list:
                x = QtGui.QTreeWidgetItem([k, "(list with %u item%s)" % (len(v), "" if len(v)==1 else "s")])
                z = QtGui.QTreeWidgetItem(["marker"])
                self._item_map[x] = lambda item, x=x, v=v: self.populate(v, x, z)
                x.addChild(z)
                item.addChild(x)
                return
            debug("type(k)=%s, type(v)=%s." % (type(k), type(v)))
            x = QtGui.QTreeWidgetItem([k, "%s" % v])
            self._item_map[x] = self.good
            item.addChild(x)
        if type(content) == dict:
            for k, v in content.iteritems():
                add(k, v)
            return
        if type(content) == list:
            for n, datum in enumerate(content):
                add("%u" % n, datum)
            return
    def load(self, fname):
        with open(fname, "rt") as f:
            s = f.read()
        self._content = yaml.load(s, Loader=MapLoader)
        self._root.takeChildren()
        self.populate(self._content, self._root, self._marker)
        self._fname = fname
    def good(self, item):
        pass
    def expanded(self, item):
        debug("expanded, item=%s, map=%s" % (item, self._item_map.get(item, "N/A")))
        h = self._item_map[item]
        h(item)

# MapLoader makes all object/python instances into maps.
class MapLoader(yaml.SafeLoader):
    def construct_x(self, tag_suffix, node):
        debug("node.tag=%s, tag_suffix=%s." % (node.tag, tag_suffix))
        return self.construct_mapping(node)
MapLoader.add_multi_constructor(
        "tag:yaml.org,2002:python/object",
        MapLoader.construct_x)

def main():
    configuration = {
        "directory": os.path.expanduser("~"),
    }
    try:
        with open(os.path.expanduser("~/.yamlviewer.yaml"), "rt") as f:
            s = f.read()
            c = yaml.load(s)
            configuration.update(c)
    except IOError:
        # file not found
        pass
    try:
        app = QtGui.QApplication(sys.argv)
        View, Controller = uic.loadUiType("yamlviewer.ui")
        controller = Controller(parent=None)
        view = View()
        view.setupUi(controller)
        filename = None
        if len(sys.argv) > 1:
            filename = sys.argv[1]
        yaml_viewer = YamlViewer(view, controller, configuration, filename)
        controller.show()
        sys.exit(app.exec_())
    finally:
        s = yaml.dump(configuration)
        with open(os.path.expanduser("~/.yamlviewer.yaml"), "wt") as f:
            f.write(s)

main()

