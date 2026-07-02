# Resume Upload API

## Endpoint
POST /resume/upload

## Request
multipart/form-data

Parameter:
- file (PDF)

## Success Response
{
  "message": "Resume uploaded successfully",
  "resume_id": 1
}

## Error Responses
400 - Only PDF files are allowed
500 - Internal server error