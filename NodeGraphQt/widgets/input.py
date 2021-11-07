from PyQt5.QtWidgets import *
import os
from pathlib import Path

class InputDialog(QWidget):
    def __init__(self,parent = None,node_graph = None):
        super(InputDialog,self ).__init__(parent )
        self.setWindowTitle("ToolBox")
        hbox = QHBoxLayout()
        hbox.addStretch(1)

        vbox = QVBoxLayout()
        vbox.addStretch(1)
        vbox.addLayout(hbox)

        self.setLayout(vbox)

        self.addInput = QLineEdit('input name',self)

        self.addInput.move(50, 50)
        self.addOutput = QLineEdit('output name', self)
        self.addOutput.move(200,50)
        self.graph = node_graph
        #self.ledTitle.textChanged.connect(self.evt_ledTitle_textChanged)
        self.btnIn = QPushButton("Add Input", self)
        self.btnIn.move(50, 80)
        self.btnIn.clicked.connect(self.set_input)

        # self.btnIn = QPushButton("remove Input", self)
        # self.btnIn.move(50, 100)
        # self.btnIn.clicked.connect(self.remove_input)


        self.btnOut = QPushButton("Add Output", self)
        self.btnOut.move(250, 80)
        self.btnOut.clicked.connect(self.set_output)

        self.failurePoints = QLabel("Failures points =", self)
        self.failurePoints.move(200,100)
        self.btnUpdate = QPushButton('calculate',self)
        self.btnUpdate.clicked.connect(self.calculate)
        self.btnPublish = QPushButton('Publish',self)
        self.btnPublish.clicked.connect(self.publish)

        hbox.addWidget(self.addInput)
        hbox.addWidget(self.addOutput)
        hbox.addWidget(self.btnIn)
        hbox.addWidget(self.btnOut)
        vbox.addWidget(self.failurePoints)
        vbox.addWidget(self.btnUpdate)
        vbox.addWidget(self.btnPublish)


    def publish(self):
        """
        publishes configuration from globals node to file
        """
        from general import save_json

        nodes = self.graph.all_nodes()
        for n in nodes:
            if n.type_ == 'project.globals.Globals':
                globalData = n.properties()['custom']

                this_path = p = Path(__file__).parents[2]
                writeDir = os.path.join(this_path,'projects','{}.json'.format(globalData['projectName']))
                save_json(writeDir,globalData)

    def calculate(self):
        nodes = self.graph.all_nodes()
        failure = 0
        for n in nodes:
            inputsOutputs = n.connected_input_nodes().values()
            #inputsOutputs += n.connected_output_nodes().values()
            for i in inputsOutputs:
                if i:
                    failure += 1


        self.failurePoints.setText("Failures points ={}".format(str(failure)))

    def remove_input(self):
        #Todo: get this remove working

        for n in self.graph.selected_nodes():
            #print(n._inputs)
            port = n.get_input(0)
            n._inputs.remove(port)


    def set_input(self):

        for n in self.graph.selected_nodes():

            print(self.addInput.text())
            n.add_input(self.addInput.text())

    def set_output(self):
        for n in self.graph.selected_nodes():
            print(self.addOutput.text())
            n.add_output(self.addOutput.text())
