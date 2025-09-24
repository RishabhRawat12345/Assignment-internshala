from fastapi import FastAPI, HTTPException
from models import Issue, IssueCreate
from typing import List, Optional
from datetime import datetime
import itertools
from fastapi.middleware.cors import CORSMiddleware
app = FastAPI()


origins = [
    "http://localhost:4200",
    "http://127.0.0.1:4200"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,       # allow Angular frontend
    allow_credentials=True,
    allow_methods=["*"],         # allow all HTTP methods
    allow_headers=["*"],         # allow all headers
)
# In-memory storage
issues: List[Issue] = []
counter = itertools.count(1)

# --- Add some sample issues ---
now = datetime.utcnow().isoformat()
issues.append(Issue(id=next(counter), title="Fix login bug", description="Users cannot log in with Google", status="open", priority="high", assignee="Alice", createdAt=now, updatedAt=now))
issues.append(Issue(id=next(counter), title="Update README", description="Add API usage examples", status="in-progress", priority="medium", assignee="Bob", createdAt=now, updatedAt=now))

# --- Health check ---
@app.get("/health")
def health():
    return {"status": "ok"}

# --- List issues with filters, search, sort, pagination ---
@app.get("/issues", response_model=List[Issue])
def list_issues(
    search: Optional[str] = None,
    status: Optional[str] = None,
    priority: Optional[str] = None,
    assignee: Optional[str] = None,
    sortBy: Optional[str] = None,
    sortOrder: str = "asc",
    page: int = 1,
    pageSize: int = 10,
):
    result = issues

    # Filters
    if search:
        result = [i for i in result if search.lower() in i.title.lower()]
    if status:
        result = [i for i in result if i.status == status]
    if priority:
        result = [i for i in result if i.priority == priority]
    if assignee:
        result = [i for i in result if i.assignee == assignee]

    # Sorting
    if sortBy:
        reverse = sortOrder == "desc"
        result = sorted(result, key=lambda x: getattr(x, sortBy), reverse=reverse)

    # Pagination
    start = (page - 1) * pageSize
    end = start + pageSize
    return result[start:end]

# --- Get single issue ---
@app.get("/issues/{issue_id}", response_model=Issue)
def get_issue(issue_id: int):
    for issue in issues:
        if issue.id == issue_id:
            return issue
    raise HTTPException(status_code=404, detail="Issue not found")

# --- Create issue ---
@app.post("/issues", response_model=Issue)
def create_issue(data: IssueCreate):
    now = datetime.utcnow().isoformat()
    new_issue = Issue(
        id=next(counter),
        title=data.title,
        description=data.description,
        status=data.status,
        priority=data.priority,
        assignee=data.assignee,
        createdAt=now,
        updatedAt=now
    )
    issues.append(new_issue)
    return new_issue

# --- Update issue ---
@app.put("/issues/{issue_id}", response_model=Issue)
def update_issue(issue_id: int, data: IssueCreate):
    for idx, issue in enumerate(issues):
        if issue.id == issue_id:
            updated = issue.copy(update={
                "title": data.title or issue.title,
                "description": data.description or issue.description,
                "status": data.status or issue.status,
                "priority": data.priority or issue.priority,
                "assignee": data.assignee or issue.assignee,
                "updatedAt": datetime.utcnow().isoformat()
            })
            issues[idx] = updated
            return updated
    raise HTTPException(status_code=404, detail="Issue not found")
