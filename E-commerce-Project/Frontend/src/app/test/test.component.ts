import { Component } from '@angular/core';
import { TestService } from '../services/test.service';

@Component({
  selector: 'app-test',
  templateUrl: './test.component.html',
  styleUrls: ['./test.component.css']
})
export class TestComponent {
  response: any;

  constructor(private testService: TestService) { }

  getTest() {
    this.testService.getTest().subscribe(response => {
      this.response = response;
    });
  }
}


