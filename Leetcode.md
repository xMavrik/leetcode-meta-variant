## Non-Functional Requirements

Optimize for availability over consistency; small scale (≤ ~400k users, ~4k problems).

Isolation & security for code execution (containers, read-only FS, CPU/Mem limits, timeout ≤ 5s, no network, seccomp).

Latency SLA: submission result in ≤ 5s (or async + rapid polling).

Scale target: competitions up to 100k users (burst handling, horizontal scale).

Simplicity over over-engineering; polling acceptable (e.g., 5s).

----------------------------------------------------------------------------------------------------------------------------------

## Core Entities

Problem: id, title, level, tags, question, language code stubs, testCases[].

Submission: userId, problemId, code, language, passed/result, timings.

Leaderboard: competitionId → userId score/time rankings.

Competition: id, start/end, problems[10], scoring rules (solves; tie-break by total time).

----------------------------------------------------------------------------------------------------------------------------------

## API Design

* Note: userId via session/JWT; server-generated timestamps.

List problems (paged): GET /problems?page=1&limit=100 -> Partial<Problem>[]

Get problem (with stub): GET /problems/:id?language=python -> Problem

Submit solution: POST /problems/:id/submit {code, language} -> Submission

Check async status (if queued): GET /check/:submissionId -> {status,result?}

Leaderboard (paged): GET /leaderboard/:competitionId?page=1&limit=100 -> Leaderboard

----------------------------------------------------------------------------------------------------------------------------------

## High-Level Design

Editor: in-browser (e.g., Monaco) for multi-lang coding.

Client–Server (monolith OK): API Server + DB; orient flows per endpoint.

Problems storage: NoSQL (e.g., DynamoDB); nested testCases & codeStubs; proper indexes for pagination.

Code execution: isolated containers per language (avoid cold starts); API hands code → container → result → persist.

Leaderboard (basic): derive from submissions; return to client; client polls ~5s.

----------------------------------------------------------------------------------------------------------------------------------

## Deep Dive (NF Focus)

Execution Security: read-only FS; CPU/Mem limits; hard timeout (≤5s); no network (VPC rules/NACLs); seccomp to restrict syscalls.

Leaderboard at scale: Redis Sorted Set per competition

Updates on submission: ZADD competition:leaderboard:{id} score userId

Reads: ZREVRANGE ... 0 N-1 WITHSCORES; 5s polling; serve top N + paging.

Handling 100k users / bursts: add queue (e.g., SQS) between API and workers; workers pull, execute, persist, update Redis; /check/:id polled ~1s.

Test harnessing: standardized serialization for inputs/outputs; per-lang harness deserializes (e.g., TreeNode), invokes user code, compares to expected; one test spec works across languages.

Trade-offs: Polling ≪ complexity of WebSockets here; queue adds retries/back-pressure; monolith fine at this scale, microservices optional.



