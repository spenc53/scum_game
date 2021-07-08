import React from 'react';

import SocketCommunicator from '../socket/Socket';
import { Button, Typography } from '@material-ui/core';
import RegisterUserCommand from '../socket/commands/RegisterUserCommand';

const comms = SocketCommunicator.getInstance();

function LobbyPage() {
  return (
    <>
        <Typography variant="h1">Welcome (to) Scum</Typography>
        <Button variant="contained" onClick={() => {
            let command = new RegisterUserCommand({
                'name': 'test'
            });
            console.log(JSON.stringify(command))
            comms.sendCommand(command);
        }}>Create New Game</Button>
    </>
  );
}

export default LobbyPage;
