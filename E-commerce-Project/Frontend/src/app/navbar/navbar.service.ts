import { Injectable } from '@angular/core';
import { HttpClient, HttpResponse } from '@angular/common/http';
import { map } from 'rxjs/operators';
import { Observable } from 'rxjs';

interface LoginResponse {
  success: boolean;
  email?: string;
  error?: string;
}

interface UserRoleResponse {
  user_role?: string;
  error?: string;
}

@Injectable({
  providedIn: 'root'
})
export class NavbarService {
  private baseUrl = 'http://localhost:5000';
  private userEmail: string | undefined;

  constructor(private http: HttpClient) {
    // When the service is initialized, try to retrieve the user email from local storage
    const storedEmail = localStorage.getItem('userEmail');
    if (storedEmail) {
      this.userEmail = storedEmail;
    }
  }

  login(credentials: { email: string, password: string }) {
    return this.http.post(`${this.baseUrl}/login`, credentials, { observe: 'response' }).pipe(
      map((response: HttpResponse<any>) => {
        if (response.body && response.body.success) {
          this.setUserEmail(response.body.email);
          this.setUserRole(response.body.user_role); // Add this line to set the user role
          // Store the user email and role in local storage
          localStorage.setItem('userEmail', response.body.email);
          localStorage.setItem('userRole', response.body.user_role);
        }
        return response.body;
      })
    );
  }


 

  setUserEmail(email: string) {
    console.log('Setting user email:', email);
    this.userEmail = email;
  }

  getUserEmail(): string | undefined {
    return this.userEmail;
  }

  clearUserEmail() {
    this.userEmail = undefined;
    // Remove the user email from local storage
    localStorage.removeItem('userEmail');
  }

  isLoggedIn(): boolean {
    console.log('Checking if user is logged in:', !!this.userEmail);
    return !!this.userEmail;
  }


  setUserRole(role: string) {
    console.log('Setting user role:', role);
    localStorage.setItem('userRole', role);
  }

  getUserRole(email: string) {
    return this.http.get(`${this.baseUrl}/getUserRole?email=${email}`).pipe(
      map((response: any) => response.user_role)
    );
  }


  logout() {
    this.clearUserEmail();
  }
}

