# yamlviewer

Read-only tree viewer for Yaml scripts with PySide2 (PyQt).  Trees are displayed
in a lazy manner, meaning that the child contents of an item are added only
when the user opens the item.  This way the viewer avoids problems with
trees that have circular dependencies.

