import { Injectable } from '@angular/core';
import axios from 'axios';

export interface Issue {
  id: number;
  title: string;
  description?: string;
  status: string;
  priority: string;
  assignee?: string;
  createdAt: string;
  updatedAt: string;
}

@Injectable({ providedIn: 'root' })
export class IssueService {
  baseUrl = 'http://127.0.0.1:8000';

  async getIssues(params: any = {}): Promise<Issue[]> {
    const res = await axios.get(`${this.baseUrl}/issues`, { params });
    return res.data;
  }

  async getIssue(id: number): Promise<Issue> {
    const res = await axios.get(`${this.baseUrl}/issues/${id}`);
    return res.data;
  }

  async createIssue(issue: Partial<Issue>): Promise<Issue> {
    const res = await axios.post(`${this.baseUrl}/issues`, issue);
    return res.data;
  }

  async updateIssue(id: number, issue: Partial<Issue>): Promise<Issue> {
    const res = await axios.put(`${this.baseUrl}/issues/${id}`, issue);
    return res.data;
  }
}
