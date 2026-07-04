Analyze the Apache-style access log at `/app/access.log` and write a JSON report to `/app/report.json`.

The report must satisfy these criteria:

1. `/app/report.json` exists and contains a JSON object.
2. `total_requests`: the number of non-empty log records in `/app/access.log`.
3. `unique_ips`: the number of distinct client IP addresses. The client IP is the first field on each log line.
4. `top_path`: the request path that appears most often inside the quoted HTTP request field.

For the provided log, the correct report is:

```json
{
  "total_requests": 6,
  "unique_ips": 3,
  "top_path": "/index.html"
}
```

Write only `/app/report.json`. Do not modify `/app/access.log`.

You have 120 seconds to complete the task.
