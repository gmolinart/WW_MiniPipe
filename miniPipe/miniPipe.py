#!/usr/bin/python
# -*- coding: utf-8 -*-
import os

from Qt import QtCore, QtGui, QtWidgets
from NodeGraphQt import (NodeGraph,
                         BaseNode,
                         BackdropNode,
                         PropertiesBinWidget,
                         NodeTreeWidget,
                         setup_context_menu)

from tasks import *

from globals import Globals
from NodeGraphQt.widgets import  input

# import example nodes from the "example_nodes" package


def draw_triangle_port(painter, rect, info):
    """
    Custom paint function for drawing a Triangle shaped port.

    Args:
        painter (QtGui.QPainter): painter object.
        rect (QtCore.QRectF): port rect used to describe parameters
                              needed to draw.
        info (dict): information describing the ports current state.
            {
                'port_type': 'in',
                'color': (0, 0, 0),
                'border_color': (255, 255, 255),
                'multi_connection': False,
                'connected': False,
                'hovered': False,
            }
    """
    painter.save()

    size = int(rect.height() / 2)
    triangle = QtGui.QPolygonF()
    triangle.append(QtCore.QPointF(-size, size))
    triangle.append(QtCore.QPointF(0.0, -size))
    triangle.append(QtCore.QPointF(size, size))

    transform = QtGui.QTransform()
    transform.translate(rect.center().x(), rect.center().y())
    port_poly = transform.map(triangle)

    # mouse over port color.
    if info['hovered']:
        color = QtGui.QColor(14, 45, 59)
        border_color = QtGui.QColor(136, 255, 35)
    # port connected color.
    elif info['connected']:
        color = QtGui.QColor(195, 60, 60)
        border_color = QtGui.QColor(200, 130, 70)
    # default port color
    else:
        color = QtGui.QColor(*info['color'])
        border_color = QtGui.QColor(*info['border_color'])

    pen = QtGui.QPen(border_color, 1.8)
    pen.setJoinStyle(QtCore.Qt.MiterJoin)

    painter.setPen(pen)
    painter.setBrush(color)
    painter.drawPolygon(port_poly)

    painter.restore()

def draw_square_port(painter, rect, info):
    """
    Custom paint function for drawing a Square shaped port.

    Args:
        painter (QtGui.QPainter): painter object.
        rect (QtCore.QRectF): port rect used to describe parameters
                              needed to draw.
        info (dict): information describing the ports current state.
            {
                'port_type': 'in',
                'color': (0, 0, 0),
                'border_color': (255, 255, 255),
                'multi_connection': False,
                'connected': False,
                'hovered': False,
            }
    """
    painter.save()

    # mouse over port color.
    if info['hovered']:
        color = QtGui.QColor(14, 45, 59)
        border_color = QtGui.QColor(136, 255, 35, 255)
    # port connected color.
    elif info['connected']:
        color = QtGui.QColor(195, 60, 60)
        border_color = QtGui.QColor(200, 130, 70)
    # default port color
    else:
        color = QtGui.QColor(*info['color'])
        border_color = QtGui.QColor(*info['border_color'])

    pen = QtGui.QPen(border_color, 1.8)
    pen.setJoinStyle(QtCore.Qt.MiterJoin)

    painter.setPen(pen)
    painter.setBrush(color)
    painter.drawRect(rect)

    painter.restore()


class MyNode(BaseNode):
    """
    example test node.
    """

    # set a unique node identifier.
    __identifier__ = 'com.chantasticvfx'

    # set the initial default node name.
    NODE_NAME = 'my node'

    def __init__(self):
        super(MyNode, self).__init__()
        self.set_color(25, 58, 51)

        # create input and output port.
        self.add_input('in port', color=(200, 10, 0))
        self.add_output('default port')
        self.add_output('square port', painter_func=draw_square_port)
        self.add_output('triangle port', painter_func=draw_triangle_port)


if __name__ == '__main__':
    QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)
    app = QtWidgets.QApplication([])

    # create node graph.
    graph = NodeGraph()

    # set up default menu and commands.
    setup_context_menu(graph)

    # widget used for the node graph.
    graph_widget = graph.widget
    graph_widget.resize(1100, 800)
    graph_widget.show()


    # show the properties bin when a node is "double clicked" in the graph.
    properties_bin = PropertiesBinWidget(node_graph=graph)
    properties_bin.setWindowFlags(QtCore.Qt.Tool)

    def show_prop_bin(node):
        if not properties_bin.isVisible():
            properties_bin.show()

    graph.node_double_clicked.connect(show_prop_bin)
    inputDialog = input.InputDialog(node_graph=graph)
    graph.node_double_clicked.connect(inputDialog.show())


    # show the nodes list when a node is "double clicked" in the graph.
    node_tree = NodeTreeWidget(node_graph=graph)
    def show_nodes_list(node):
        if not node_tree.isVisible():
            node_tree.update()
            node_tree.show()
    graph.node_double_clicked.connect(show_nodes_list)


    # registered nodes.
    nodes_to_reg = [
        BackdropNode,
        Anim,
        Mdl,
        Light,
        Sim,
        Rig,
        Review,
        Lay,
        Globals

    ]
    graph.register_nodes(nodes_to_reg)


    def assign_icon(node,name =None):

        extensions = ['png','jpg']
        this_path = os.path.dirname(os.path.abspath(__file__))
        if not name:
            name = node
        for ext in extensions:
            iconDir = os.path.join(this_path, 'miniPipe/icons/', '{}.png'.format(name))

            node.set_icon(iconDir)
            print('found________________')

    def create_default_nodes(name,graph):

        node = graph.create_node('com.chantasticvfx.{}'.format(name))
        node.set_name(name)
        assign_icon(node,name)



    def change_icons(node,name):

        this_path = os.path.dirname(os.path.abspath(__file__))
        iconHoudini = os.path.join(this_path, 'miniPipe/icons/', name)
        node.set_icon(iconHoudini)
        node.set_name('icon node')



    # auto layout nodes.
    graph.auto_layout_nodes()
    graph.fit_to_selection()

    app.exec_()


