## Non-Functional Requirements

* availability > consistency; small scale (≤ ~400k users, ~4k problems).

* Isolation & security for code execution (containers, read-only file system, CPU/Mem limits, timeout ≤ 5s, no network (VPC), seccomp).

* Latency SLA: submission result in ≤ 5s

* Scale target: competitions up to 100k users (burst handling, horizontal scale).

* Simplicity over over-engineering; polling acceptable (e.g., 5s).

----------------------------------------------------------------------------------------------------------------------------------

## Core Entities

* Problem: (id, title, level, tags, question text, language code stubs, testCases[])

* Submission: (submissionID, userId, problemId, code, language, queued/running/passed/failed, time results)

* User: (userID, email)

* Leaderboard: competitionId → userId score/time rankings.

* Competition: id, start/end, problems[10], scoring rules (solves; tie-break by total time).

----------------------------------------------------------------------------------------------------------------------------------

## API Design

* Note: userId via session/JWT; server-generated timestamps.

* List problems (paged) --> 
GET /problems?page=1&limit=100           -> Partial<Problem>[]

* Get problem (with language stub) --> 
GET /problems/:id?language=python        -> Problem

* Submit solution (sync/async wrapper) -->
POST /problems/:id/submit                -> Submission

* Poll submission status (if async path) -->
GET /check/:submissionId                 -> Submission Result

* Leaderboard (paged) -->
GET /leaderboard/:competitionId?page=1&limit=100 -> Leaderboard
Note: userId from session/JWT; timestamps server-side.

----------------------------------------------------------------------------------------------------------------------------------

## High-Level Design

* Editor: in-browser (Monaco).

* Client ↔ API Server (monolith OK); design flows per endpoint.

* Primary DB: NoSQL (e.g., DynamoDB). Problems embed testCases & codeStubs. Indexes for pagination.

* Fallback query for competitions, Use Partition key on competition; add Sort key for rank ordering (via inverted score + time). Use a GSI on userId if you need fast “what’s this user’s score in comp XYZ?” lookups.

* Code Execution: language-specific lambdas with provisioned concurrency (avoid cold starts). API → container → result → persist.
can use quick 200 calls for less popular languages to avoid cold start

* Lambda container images (stored in ECR) because we have short-running executions and don't need complex docker

* Leaderboard (basic path): derive from submissions; client polls ~5s.

----------------------------------------------------------------------------------------------------------------------------------

## Deep Dive (NF Focus)

* Execution Security: read-only File System (tmp); CPU/Mem limits; ≤5s timeout; no network (VPC); seccomp

* Leaderboard @ scale: Redis Sorted Set per competition

* Update on pass: ZADD competition:leaderboard:{id} score userId

* Client polls ~5s; serve top 1k + server paging.

* Burst Handling (100k users): Queue (SQS) and workers, use S3 to store code; workers pull, run, persist, update Redis; client polls GET /check/:id ~1s. Adds retries/back-pressure.

* Test Harnessing: standardized serialization for inputs/outputs; per-lang harness deserializes (e.g., TreeNode) → invoke user code → compare to expected. One test spec, many languages.

* Trade-offs: polling ≪ complexity of WebSockets here; monolith fine for size; microservices optional.


