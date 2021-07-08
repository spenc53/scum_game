from server.commands.server_commands import *

class CommandFactory():

    commandBuilders = {
        'RegisterPlayerCommand': RegisterPlayerCommand
    }

    def createCommand(command):
        commandType = command['type']
        data = command['data']

        if commandType not in CommandFactory.commandBuilders:
            raise ValueError('Command not found')

        return CommandFactory.commandBuilders[commandType](**data)

        

# Commands are formatted as
'''
{
    CommandType: str
    data: any
}
'''