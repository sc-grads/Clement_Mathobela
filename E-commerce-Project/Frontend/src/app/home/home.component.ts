import { Component } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';


@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.css']
})
export class HomeComponent {

  constructor(private http: HttpClient) { }

  products: any[] = [];

  ngOnInit(): void {
    this.getProducts();
  }

  getProducts(): void {
    this.http.get<any>('http://localhost:5000/products').subscribe(data => {
      this.products = data;
    });
  }

  addToCart(product: any): void {
    const headers = new HttpHeaders().set('Content-Type', 'application/json');
    const options = { headers, withCredentials: true };
    const url = 'http://localhost:5000/addToCart';
    const body = {
      user_email: 'example@example.com', // Replace with the actual user email
      product_id: product.product_id,
      quantity: 1, // Replace with the desired quantity
      total_amount: product.price // Replace with the appropriate calculation for the total amount
    };

    console.log("heyy")
    this.http.post(url, body).subscribe(response => {
      console.log(response); // Log the response or handle it as needed
      // Optionally, you can update the products list or perform other actions after adding to the cart
      this.getProducts();
    });
  }

}

