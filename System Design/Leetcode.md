## Non-Functional Requirements

* Optimize for availability over consistency; small scale (≤ ~400k users, ~4k problems).

* Isolation & security for code execution (containers, read-only FS, CPU/Mem limits, timeout ≤ 5s, no network, seccomp).

* Latency SLA: submission result in ≤ 5s (or async + rapid polling).

* Scale target: competitions up to 100k users (burst handling, horizontal scale).

* Simplicity over over-engineering; polling acceptable (e.g., 5s).

----------------------------------------------------------------------------------------------------------------------------------

## Core Entities

* Problem: id, title, level, tags, question, language code stubs, testCases[].

* Submission: userId, problemId, code, language, passed/result, timings.

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
Body: { "code": string, "language": string }

* Poll submission status (if async path) -->
GET /check/:submissionId                 -> { status, result? }

* Leaderboard (paged) -->
GET /leaderboard/:competitionId?page=1&limit=100 -> Leaderboard
Note: userId from session/JWT; timestamps server-side.

----------------------------------------------------------------------------------------------------------------------------------

## High-Level Design

* Client ↔ API Server (monolith OK); design flows per endpoint.

* Problems DB: NoSQL (e.g., DynamoDB). Problems embed testCases & codeStubs. Indexes for pagination.

* Code Execution: language-specific containers (avoid cold starts). API → container → result → persist.

* Leaderboard (basic path): derive from submissions; client polls ~5s.

* Editor: in-browser (Monaco).

----------------------------------------------------------------------------------------------------------------------------------

## Deep Dive (NF Focus)

* Execution Security: read-only FS; CPU/Mem limits; ≤5s timeout; no network (VPC/NACL); seccomp.

* Leaderboard @ scale: Redis Sorted Set per competition

* Update on pass: ZADD competition:leaderboard:{id} score userId

* Read top-N: ZREVRANGE ... 0 N-1 WITHSCORES

* Client polls ~5s; serve top 1k + server paging.

* Burst Handling (100k users): Queue (SQS) between API and workers; workers pull, run, persist, update Redis; client polls GET /check/:id ~1s. Adds retries/back-pressure.

* Test Harnessing: standardized serialization for inputs/outputs; per-lang harness deserializes (e.g., TreeNode) → invoke user code → compare to expected. One test spec, many languages.

* Trade-offs: polling ≪ complexity of WebSockets here; monolith fine for size; microservices optional.


