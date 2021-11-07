from NodeGraphQt import BaseNode


class Mdl(BaseNode):
    """
    A node class with 3 inputs and 3 outputs.
    The last input and last output can take in multiple pipes.
    """

    # unique node identifier.
    __identifier__ = 'tasks.CG'

    # initial default node name.
    NODE_NAME = 'mdl'

    def __init__(self):
        super(Mdl, self).__init__()

        # create node inputs
        self.add_input('reference')

        # create node outputs
        self.add_output('.mb', multi_output=False)
        self.add_output('.abc', multi_output=False)
        self.add_output('.fbx')
        self.add_output('.mov')

class Rig(BaseNode):
    """
    A node class with 3 inputs and 3 outputs.
    The last input and last output can take in multiple pipes.
    """

    # unique node identifier.
    __identifier__ = 'tasks.CG'

    # initial default node name.
    NODE_NAME = 'rig'

    def __init__(self):
        super(Rig, self).__init__()

        # create node inputs
        self.add_input('.mb')
        self.add_input('tex')

        # create node outputs
        self.add_output('.mb', multi_output=False)
        self.add_output('.mov')

class Anim(BaseNode):
    """
    A node class with 3 inputs and 3 outputs.
    The last input and last output can take in multiple pipes.
    """

    # unique node identifier.
    __identifier__ = 'tasks.CG'

    # initial default node name.
    NODE_NAME = 'anim'

    def __init__(self):
        super(Anim, self).__init__()

        # create node inputs
        self.add_input('.mb')
        self.add_input('.tex')

        # create node outputs

        self.add_output('.mb', multi_output=False)
        self.add_output('.abc')
        self.add_output('.mov')

class Lay(BaseNode):
    """
    A node class with 3 inputs and 3 outputs.
    The last input and last output can take in multiple pipes.
    """

    # unique node identifier.
    __identifier__ = 'tasks.CG'

    # initial default node name.
    NODE_NAME = 'layout'

    def __init__(self):
        super(Lay, self).__init__()

        # create node inputs
        self.add_input('.mb')
        self.add_input('.tex')

        # create node outputs

        self.add_output('.mb', multi_output=False)
        self.add_output('.abc')
        self.add_output('.mov')

class Light(BaseNode):
    """
    A node class with 3 inputs and 3 outputs.
    The last input and last output can take in multiple pipes.
    """

    # unique node identifier.
    __identifier__ = 'tasks.CG'

    # initial default node name.
    NODE_NAME = 'light'

    def __init__(self):
        super(Light, self).__init__()

        # create node inputs
        self.add_input('.abc')
        self.add_input('shdr')
        self.add_input('sim')

        # create node outputs
        self.add_output('.exr', multi_output=False)
        self.add_output('.mov')

class Comp(BaseNode):
    """
    A node class with 3 inputs and 3 outputs.
    The last input and last output can take in multiple pipes.
    """

    # unique node identifier.
    __identifier__ = 'tasks.CG'

    # initial default node name.
    NODE_NAME = 'comp'

    def __init__(self):
        super(Light, self).__init__()

        # create node inputs
        self.add_input('.exr')
        # create node outputs
        self.add_output('.exr', multi_output=False)
        self.add_output('.mov')

class Sim(BaseNode):
    """
    A node class with 3 inputs and 3 outputs.
    The last input and last output can take in multiple pipes.
    """

    # unique node identifier.
    __identifier__ = 'tasks.CG'

    # initial default node name.
    NODE_NAME = 'sim'

    def __init__(self):
        super(Sim, self).__init__()

        # create node inputs
        self.add_input('abc')

        # create node outputs
        self.add_output('.abc', multi_output=False)
        self.add_output('.geo')

class Blank(BaseNode):
    """
    A blank Node Class
    """

    # unique node identifier.
    __identifier__ = 'com.chantasticvfx'

    # initial default node name.
    NODE_NAME = 'Blank'

    def __init__(self):
        super(Blank, self).__init__()

        # create node inputs
        # create node outputs


class Review(BaseNode):
    """
    A node class with 3 inputs and 3 outputs.
    The last input and last output can take in multiple pipes.
    """

    # unique node identifier.
    __identifier__ = 'tasks.review'

    # initial default node name.
    NODE_NAME = 'review'

    def __init__(self):
        super(Review, self).__init__()

        # create node inputs
        self.add_input('mov')

        # create node outputs
        self.add_output('feedback', multi_output=False)
        self.add_output('approval')
