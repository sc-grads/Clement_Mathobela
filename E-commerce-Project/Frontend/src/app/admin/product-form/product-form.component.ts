import { Component, OnInit } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';

interface Product{
  name: string;
  brand: string;
  description: string;
  picture: string;
  color: string;
  stock: number;
  price: number;
}

interface ResponseData {
  message: string;
}

@Component({
  selector: 'app-product-form',
  templateUrl: './product-form.component.html',
  styleUrls: ['./product-form.component.css']
})
export class ProductFormComponent {
  product: Product = {
    name: '',
    brand: '',
    description: '',
    picture: '',
    color: '',
    stock: 0,
    price: 0
  };
  message: string = '';
 

  constructor(private http: HttpClient) { }

  new_product() {
    const headers = new HttpHeaders().set('Content-Type', 'application/json');
    const options = { headers, withCredentials: true };
    const body = JSON.stringify(this.product);
    this.http.post<ResponseData>('http://localhost:5000/insertProduct', body, options).subscribe(data => {
      this.message = data.message;
    }, error => {
      this.message = error.error.message;
    });
  }

}
