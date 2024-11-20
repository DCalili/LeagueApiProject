import { Component } from '@angular/core';
import { Account } from '../_models/account';
import { Mastery } from '../_models/mastery';
import { HttpClient } from '@angular/common/http';
import { FormsModule } from '@angular/forms';
import { CommonModule} from '@angular/common';
import { Champion } from '../_models/champion';

@Component({
  selector: 'app-search',
  imports:[FormsModule, CommonModule],
  templateUrl: './search.component.html',
  styleUrls: ['./search.component.css'] 
})
export class SearchComponent {
  account: Account | any;
  mastery: Mastery[] = [];
  champion: Champion[] = []

  constructor(private httpClient: HttpClient) {}

  getAccount(name: string, tag: string): void {
    this.httpClient.get<Account>(`http://localhost:5000/api/summoner?name=${name}&tag=${tag}`).subscribe({
      next: response => {
        this.account = response;
        this.getMastery(this.account.puuid)
        this.champion = []
      },
      error: error => console.log(error),
      complete: () => console.log(this.account)
    });
  }

  getMastery(puuid: string): void{
    this.httpClient.get<Mastery[]>(`http://localhost:5000/api/summoner/mastery?puuid=${puuid}`).subscribe({
      next: response => {
        this.mastery = response;
        for(let i=0;i<=2;i++){
          this.getChampionName(this.mastery[i].championId)
        }
   
      }
    })
  }

  getChampionName(championId: number){
    this.httpClient.get<Champion>(`http://localhost:5000/api/summoner/champion?championId=${championId}`).subscribe({
      next: response => this.champion.push(response),
      error: error => console.log(error),
      complete: () => console.log(this.champion)
    })
  }

  getMasterybyKey(key: number): number{
    for(let i=0; i<=2; i++){
      if (this.mastery[i].championId == key){
        return this.mastery[i].championPoints;
      } 
    }
    return 0;
  }

  
}

