import React from 'react';
import logo from './logo.svg';
import './App.css';
import useMediaQuery from '@material-ui/core/useMediaQuery';
import { createTheme, ThemeProvider } from '@material-ui/core/styles';
import CssBaseline from '@material-ui/core/CssBaseline';

import SocketCommunicator from './socket/Socket';
import LobbyPage from './LobbyPage';

const comms = SocketCommunicator.getInstance();

function App() {
  const prefersDarkMode = useMediaQuery('(prefers-color-scheme: dark)');

  const theme = React.useMemo(
    () =>
      createTheme({
        palette: {
          type: prefersDarkMode ? 'dark' : 'light',
        },
      }),
    [prefersDarkMode],
  );

  return (
    <ThemeProvider theme={theme}>
      <CssBaseline/>
      {/* <Routes /> */}
      <div className="App">
        <LobbyPage></LobbyPage>
      </div>
    </ThemeProvider>
    
  );
}

export default App;
