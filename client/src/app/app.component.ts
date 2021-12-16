import { Component } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  title = 'client';

  secret: any;


  constructor(private http: HttpClient) {}

  getSecret() {
    this.secret = this.http.post("/api/generate/" + "1" + "/", "");
  }
}
