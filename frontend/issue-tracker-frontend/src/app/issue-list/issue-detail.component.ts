import { Component, Input } from '@angular/core';
import { CommonModule } from '@angular/common';
import { Issue } from '../Services/issue.service';

@Component({
  selector: 'app-issue-detail',
  standalone: true,
  imports: [CommonModule],  // <-- add this
  templateUrl: './issue-detail.component.html',
})
export class IssueDetailComponent {
  @Input() issue!: Issue;
}
