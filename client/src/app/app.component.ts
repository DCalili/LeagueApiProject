import { Component, OnInit } from '@angular/core';
import { SearchComponent } from "./search/search.component";

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css'] // Corrige para styleUrls
  ,
  imports: [SearchComponent]
})
export class AppComponent implements OnInit {
  title = 'client';

  ngOnInit(): void {}
}
