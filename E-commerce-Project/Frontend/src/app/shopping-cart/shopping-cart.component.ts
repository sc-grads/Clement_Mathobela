import { Component, OnInit } from '@angular/core';
import { HttpClient } from '@angular/common/http';

@Component({
  selector: 'app-shopping-cart',
  templateUrl: './shopping-cart.component.html',
  styleUrls: ['./shopping-cart.component.css']
})
export class ShoppingCartComponent implements OnInit {
  cartItems: any[] = [];
  userEmail: string | null = null;

  constructor(private http: HttpClient) { }

  ngOnInit(): void {
    this.userEmail = localStorage.getItem('user_email'); // Update with the key you use to store the user email

    if (this.userEmail) {
      this.getCartItems();
    }
  }

  getCartItems(): void {
    const url = `http://localhost:5000/cart/${this.userEmail}`;

    this.http.get<any[]>(url).subscribe(data => {
      this.cartItems = data;
    });
  }
}
