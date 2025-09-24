import { Component } from '@angular/core';
import { IssueListComponent } from './issue-list/issue-list.component';

@Component({
  selector: 'app-root',
  standalone: true,
  imports: [IssueListComponent],
  template: '<app-issue-list></app-issue-list>',
})
export class AppComponent {}
