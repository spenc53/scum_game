import BaseCommand from "./BaseCommand"

export default class RegisterUserCommand extends BaseCommand {
    data: any;
    constructor(data: any) {
        super("RegisterPlayerCommand")
        this.data = data;
    }
}