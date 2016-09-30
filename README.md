# yamlviewer

Read-only tree viewer for Yaml scripts written in PyQt4.  Trees are displayed
in a lazy manner, meaning that the child contents of an item are added only
when the user opens the item.  This way the viewer avoids problems with
trees that have circular dependencies.

