import { Component } from '@angular/core';
import { Account } from '../_models/account';
import { Mastery } from '../_models/mastery';
import { HttpClient } from '@angular/common/http';
import { FormsModule } from '@angular/forms';
import { CommonModule, NgFor} from '@angular/common';
import { Champion } from '../_models/champion';
import { forkJoin, Observable } from 'rxjs';
import { Match } from '../_models/match';
import { Info } from '../_models/info';
import { Metadata } from '../_models/metadata';

@Component({
  selector: 'app-search',
  imports:[FormsModule, CommonModule, NgFor],
  templateUrl: './search.component.html',
  styleUrls: ['./search.component.css'] 
})
export class SearchComponent {
  account: Account | any;
  mastery: Mastery[] = [];
  champion: Champion[] = []
  championsWithMastery: { name: string; championPoints: number; championLevel: number }[] = []; // Dados combinados
  isLoading: boolean = false;
  matchesId: string[] = [];
  match: Match | any;
  matches: Match[] = [];
  info: Info | any;
  metadata: Metadata | any


  constructor(private httpClient: HttpClient) {}

  getAccount(name: string, tag: string): void {
    this.httpClient.get<Account>(`http://localhost:5000/api/summoner?name=${name}&tag=${tag}`).subscribe({
      next: (response) => {
        this.isLoading = true;
        this.championsWithMastery = [];
        this.account = response;
        this.getMastery(this.account.puuid);
        this.getMatchesId(this.account.puuid);
        
        // Wait until matchesId array is populated before making requests
        this.httpClient.get<string[]>(`http://localhost:5000/api/summoner/matches?puuid=${this.account.puuid}`).subscribe({
          next: (matchIds) => {
            this.matchesId = matchIds;
            
            // Create an array of observables for the match requests
            const matchRequests = this.matchesId.map(matchId => this.getMatch(matchId));
            console.log(matchRequests);
            forkJoin(matchRequests).subscribe({
              next: (matchesData: Match[]) => {
                this.matches = matchesData;
              },
              error: (error) => console.log('Erro ao obter partidas:', error),
              complete: () => {
                console.log('Todas as partidas carregadas');
                console.log(this.matches);
                this.isLoading = false;
              }
            });
          },
          error: (error) => {
            console.log(error),
            this.isLoading = false;
          }
        });
      },
      error: (error) => {
        console.log(error),
        this.isLoading = false;
      },
      complete: () => console.log(this.account)
    });
  }
  
  

  getMastery(puuid: string): void {
    this.httpClient.get<Mastery[]>(`http://localhost:5000/api/summoner/mastery?puuid=${puuid}`).subscribe({
      next: (response) => {
        // Ordena as três maiores maestrias
        this.mastery = response.sort((a, b) => b.championPoints - a.championPoints).slice(0, 3);
        this.mastery = response.sort((a, b) => b.championLevel - a.championLevel).slice(0, 3);

        // Faz requisições paralelas para os campeões
        const championRequests = this.mastery.map((masteryItem) =>
          this.httpClient.get<Champion>(`http://localhost:5000/api/summoner/champion?championId=${masteryItem.championId}`)
        );

        forkJoin(championRequests).subscribe({
          next: (champions) => {
            // Combina as informações de maestria e campeões
            this.championsWithMastery = champions.map((champion, index) => ({
              name: champion.name,
              championPoints: this.mastery[index].championPoints,
              championLevel: this.mastery[index].championLevel
            }));
          },
          error: (error) => {
            console.error('Erro ao buscar campeões:', error),
            this.isLoading = false;
          },
        });
      },
      error: (error) => {
        console.error('Erro ao buscar maestria:', error),
        this.isLoading = false;
      },
    });
  }


  getChampionName(championId: number){
    this.httpClient.get<Champion>(`http://localhost:5000/api/summoner/champion?championId=${championId}`).subscribe({
      next: response => this.champion.push(response),
      error: error => console.log(error),
      complete: () => console.log(this.champion)
    })
  }


  getMatchesId(puuid: string): void{
    this.httpClient.get<string[]>(`http://localhost:5000/api/summoner/matches?puuid=${puuid}`).subscribe({
      next: response => this.matchesId = response,
      error: error => console.log(error),
      complete: () => console.log(this.matchesId)
    })
  }

  getMatch(matchId: string): Observable<Match> {
    return this.httpClient.get<Match>(`http://localhost:5000/api/summoner/matches/match?matchId=${matchId}`);
  }
  



}

