from pydantic import BaseModel
from typing import Optional

class Issue(BaseModel):
    id: int
    title: str
    description: Optional[str] = None
    status: str = "open"       # open, in-progress, closed
    priority: str = "medium"   # low, medium, high
    assignee: Optional[str] = None
    createdAt: str
    updatedAt: str

class IssueCreate(BaseModel):
    title: str
    description: Optional[str] = None
    status: Optional[str] = "open"
    priority: Optional[str] = "medium"
    assignee: Optional[str] = None
