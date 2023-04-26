import { Component } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';

interface User {
  email: string;
  first_name: string;
  last_name: string;
  password: string;
}

interface ResponseData {
  message: string;
}

@Component({
  selector: 'app-register',
  templateUrl: './register.component.html',
  styleUrls: ['./register.component.css']
})
export class RegisterComponent {
  user: User = {
    email: '',
    first_name: '',
    last_name: '',
    password: ''
  };
  message: string = '';

  constructor(private http: HttpClient) { }

  register() {
    const headers = new HttpHeaders().set('Content-Type', 'application/json');
    const options = { headers, withCredentials: true };
    const body = JSON.stringify(this.user);
    this.http.post<ResponseData>('http://localhost:5000/register', body, options).subscribe(data => {
      this.message = data.message;
    }, error => {
      this.message = error.error.message;
    });
  }

  validateEmail(): boolean {
    const email = (<HTMLInputElement>document.getElementById("email")).value;
    const pattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    if (pattern.test(email)) {
      alert("Valid email address!");
      return true;
    } else {
      alert("Invalid email address!");
      return false;
    }
  }




}









