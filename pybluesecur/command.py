from pybluesecur.enum.DeviceAction import DeviceAction


class BlueSecurCommand:
    class CommandsObject(object):
        pass

    Commands = CommandsObject()

    @staticmethod
    def UpdateCommands():
        for action, value in DeviceAction.__dict__.items():
            if type(value) is int:
                setattr(BlueSecurCommand.Commands, action, value)


BlueSecurCommand.UpdateCommands()
