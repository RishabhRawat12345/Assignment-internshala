import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { IssueService, Issue } from '../Services/issue.service';
import { IssueDetailComponent } from '../issue-list/issue-detail.component';

@Component({
  selector: 'app-issue-list',
  standalone: true,
  imports: [CommonModule, FormsModule, IssueDetailComponent],
  templateUrl: './issue-list.component.html',
})
export class IssueListComponent implements OnInit {
  issues: Issue[] = [];
  search = '';
  filters = { status: '', priority: '', assignee: '' };
  page = 1;
  pageSize = 5;
  selectedIssue: Issue | null = null;

  constructor(private issueService: IssueService) {}

  async ngOnInit() {
    await this.loadIssues();
  }

  async loadIssues() {
    this.issues = await this.issueService.getIssues({
      search: this.search,
      status: this.filters.status,
      priority: this.filters.priority,
      assignee: this.filters.assignee,
      page: this.page,
      pageSize: this.pageSize,
    });
  }

  async onSearchChange() {
    this.page = 1;
    await this.loadIssues();
  }

  async changePage(p: number) {
    this.page = p;
    await this.loadIssues();
  }

  selectIssue(issue: Issue) {
    this.selectedIssue = issue;
  }

  async editIssue(issue: Issue) {
    const updatedTitle = prompt('Edit Title', issue.title);
    if (updatedTitle) {
      await this.issueService.updateIssue(issue.id, { title: updatedTitle });
      await this.loadIssues();
    }
  }

  async createIssue() {
    const title = prompt('New Issue Title');
    if (title) {
      await this.issueService.createIssue({ title });
      await this.loadIssues();
    }
  }
}
