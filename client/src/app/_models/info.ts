import { Participant } from "./participant";

export interface Info{
    endOfGameResult: string;
    gameCreation: number;
    gameDuration: number;
    gameId: number;
    gameMode: string;
    participants: Participant[];
}