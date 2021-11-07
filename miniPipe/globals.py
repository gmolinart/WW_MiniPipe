from NodeGraphQt import BaseNode


class Globals(BaseNode):
    """
    An example of a node with a embedded QLineEdit.
    """

    # unique node identifier.
    __identifier__ = 'project.globals'

    # initial default node name.
    NODE_NAME = 'Globals'

    def __init__(self):
        super(Globals, self).__init__()

        # create input & output ports
        self.add_input('in')
        self.add_output('out')

        # create QLineEdit text input widget.
        self.add_text_input('projectName', 'Project Name', tab='widgets')
        items = ['ACES cct', 'Linear', 'Cineon']
        self.add_combo_menu('colorspace', 'Working Colorspace', items=items)
        self.add_text_input('ext', 'File Extension', tab='widgets')
        self.add_text_input('frameRate', 'Frame Rate', tab='widgets')
        self.add_text_input('ouputRes', 'Output Res', tab='widgets')
        self.add_text_input('proxyRes', 'Proxy Res', tab='widgets')

