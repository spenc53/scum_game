import io, {Socket} from 'socket.io-client';
import BaseCommand from './commands/BaseCommand';

export default class SocketCommuicator {
    private static instance: SocketCommuicator;

    private socket: Socket;

    static getInstance() {
        if (!SocketCommuicator.instance) {
            SocketCommuicator.instance = new SocketCommuicator();
        }
        return SocketCommuicator.instance;
    }

    private constructor() {
        this.socket = io('http://localhost:5000/');
        this.socket.connect();
        this.socket.on("t", (data: any) => {
            console.log(data);
        })
        this.socket.on("message", (data: any) => {
            console.log("for me")
            console.log(data)
        })
    }

    public test() {
        this.socket.emit("command", {"test": "command"});
    }

    public sendCommand(command: BaseCommand) {
        this.socket.emit("command", JSON.stringify(command))
    }

    private setupSocket() {
        // TODO: receive commands
    }

    private receiveCommand() {
        this.socket.on("command", (data: any) => {
            // push on subject
        });
    }

    private send() {
        // this.socket
    }
}