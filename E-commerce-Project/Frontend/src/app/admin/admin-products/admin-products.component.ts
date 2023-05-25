import { Component } from '@angular/core';
import { HttpClient } from '@angular/common/http';

@Component({
  selector: 'app-admin-products',
  templateUrl: './admin-products.component.html',
  styleUrls: ['./admin-products.component.css']
})
export class AdminProductsComponent {

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

  deleteProduct(product: any): void {
    const url = `http://localhost:5000/deleteProduct`;
    const body = {
      name: product.name,
      color: product.color
    };

    this.http.post(url, body).subscribe(response => {
      console.log(response); // Log the response or handle it as needed
      // Optionally, you can also update the products list by fetching the updated data
      this.getProducts();
    });
  }

}

