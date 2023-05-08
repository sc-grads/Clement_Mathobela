import { Component } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Router } from '@angular/router';
import { NavbarService } from '../navbar/navbar.service';


interface LoginResponse {
  success: boolean;
  message: string;
  token?: string;
  error?: string;
  email?: string;
}

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})
export class LoginComponent {
  email: string = '';
  password: string = '';
  errorMessage: string = '';

  constructor(private http: HttpClient, private router: Router, private navbarService: NavbarService) { }

  onSubmit() {
    const data = {
      email: this.email,
      password: this.password
    };

    this.http.post<LoginResponse>('http://localhost:5000/login', data).subscribe((response) => {
      if (response.success) {
        localStorage.setItem('user_email', this.email); // Store email in local storage
        if (response.email !== undefined) {
          this.navbarService.setUserEmail(response.email); // Set the user email in the navbar service
          this.navbarService.getUserRole(response.email).subscribe((userRole) => {
            localStorage.setItem('user_role', userRole); // Store user role in local storage
            this.navbarService.setUserRole(userRole); // Set the user role in the navbar service
            this.router.navigate(['/home']);
          });
        }
      } else {
        this.errorMessage = response.error || response.message;
      }
    });
  }



}


