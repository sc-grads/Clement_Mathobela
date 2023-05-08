import { Component } from '@angular/core';
import { NavbarService } from './navbar/navbar.service';


@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})

export class AppComponent {
  title = 'Mobile-Store';
  constructor(private navbarService: NavbarService) { }

  onLogout(): void {
    this.navbarService.clearUserEmail();
  }
}
