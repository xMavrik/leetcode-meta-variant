## Non-Functional Requirements

Consistency: atomic swipe→instant match; no re-shows.

Scale: ~20M DAU × ~100 swipes/day.

Latency: feed load <300 ms.

Avoid repeats: never show already-swiped profiles.

(Below line: anti-fraud, monitoring/alerting.)

----------------------------------------------------------------------------------------------------------------------------------

## Core Entities

User/Profile (prefs: age, distance, interests).

Swipe (from_user → to_user, decision).

Match (user_a ↔ user_b, timestamps).

----------------------------------------------------------------------------------------------------------------------------------

## API Design

Create/Update profile: POST /profile -> Profile

Get swipe feed: GET /feed?lat=&long=&distance= -> User[]

Swipe on user: POST /swipe/:userId -> {matched: bool}

----------------------------------------------------------------------------------------------------------------------------------

## High-Level Design

Clients: iOS/Android apps.

Gateway: auth, rate limit, routing.

Services/Stores:

Profile Service → User DB (profiles/prefs).

Swipe Service → Swipe DB (Cassandra) for write-heavy swipes.

Feed/Recommend path (simple start; later: precompute cache + indexed search).

Push: APNS/FCM for “It’s a match!”.

Flow: profile set → fetch feed (by prefs+location) → swipe write → check inverse swipe → instant match notify (both sides).

----------------------------------------------------------------------------------------------------------------------------------

## Deep Dive (Quick Hits)

Swipe consistency + speed: Redis atomic op (Lua) per pair key (swipes:{minId}:{maxId}) for match detection; flush to Cassandra for durability.

Fast feed: hybrid—precompute & cache initial stack; top-up via indexed search (e.g., Elasticsearch/geo index). TTL & background refresh; trigger refresh on location/pref change.

No repeats: keep per-user “seen” set; for large histories, use Bloom filter (tunable FP) during feed build.

Data/scale: partition swipe data by swiping_user_id; separate Swipe DB from Profile DB to scale writes independently.