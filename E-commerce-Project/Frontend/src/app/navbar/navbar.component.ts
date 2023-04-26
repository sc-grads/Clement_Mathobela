import { Component, OnInit } from '@angular/core';
import { NavbarService } from './navbar.service';
import { Router } from '@angular/router';

@Component({
  selector: 'navbar',
  templateUrl: './navbar.component.html',
  styleUrls: ['./navbar.component.css']
})
export class NavbarComponent implements OnInit {
  email: string = '';
  password: string = '';
  user_role: string = '';

  constructor(private navbarService: NavbarService, private router: Router) { }

  ngOnInit() {
    if (this.navbarService.isLoggedIn()) {
      const userEmail = this.navbarService.getUserEmail();
      if (userEmail) {
        this.navbarService.getUserRole(userEmail).subscribe(
          (userRole: string) => {
            if (userRole) {
              this.user_role = userRole;
              console.log('User role:', this.user_role);
            } else {
              console.log('Error getting user role:', userRole);
            }
          },
          (error: any) => {
            console.log('Error getting user role:', error);
          }
        );
      }
    }
  }




  login() {
    const credentials = { email: this.email, password: this.password };
    this.navbarService.login(credentials).subscribe((response) => {
      if (response && response.success) {
        this.email = '';
        this.password = '';
        alert('Login successful!');
        this.navbarService.setUserEmail(response.email);
        this.router.navigate(['/']);
      } else {
        alert('Login failed!');
      }
    });
  }

  logout() {
    this.navbarService.logout();
  }

  get userEmail(): string | undefined {
    return this.navbarService.getUserEmail();
  }

  get isLoggedIn(): boolean {
    console.log('isLoggedIn:', this.navbarService.isLoggedIn());
    return this.navbarService.isLoggedIn();
  


  }

  get userRole(): string | undefined {
    let role: string | undefined;
    const userEmail = this.userEmail;
    if (userEmail) {
      this.navbarService.getUserRole(userEmail).subscribe(
        response => role = response,
        error => console.log(error)
      );
    }
    return role;
  }


}

