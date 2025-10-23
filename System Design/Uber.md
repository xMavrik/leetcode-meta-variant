## Non-Functional Requirements

Low latency matching: target <1 min to match/fail.

Strong consistency: no double-assign (one ride/driver at a time).

High throughput: handle event spikes (e.g., 100k reqs from one area).

(Below the line: security/GDPR, resilience/failover, monitoring/alerting, CI/CD.)

----------------------------------------------------------------------------------------------------------------------------------

## Core Entities

Rider (profile, payment)

Driver (profile, vehicle, availability)

Fare (pickup, dest, ETA, est. price)

Ride (rider, driver, route, state, actual fare, timestamps)

Location (driver lat/long, lastUpdated)

----------------------------------------------------------------------------------------------------------------------------------

## API Design

Estimate fare: POST /fare -> Fare 
(body: pickupLocation, destination)

Request ride: POST /rides -> Ride 
(body: fareId)

Update driver location: POST /drivers/location -> Success 
(lat,long; driverId from JWT)

Accept/decline ride: PATCH /rides/:rideId -> Ride 
(body: accept|deny)

If we want to add polling driver location to user 
GET /rides/{rideId}/driver-location -> Location<>

----------------------------------------------------------------------------------------------------------------------------------

## High-Level Design

Clients: Rider app, Driver app.

Gateway: auth, rate-limit, routing.

Services: Ride Service (fares, ride state), Location Service (driver positions), Ride Matching Service (select drivers), Notification Service (APN/FCM).

Infra: DB (Fare/Ride), Redis (geo/locks), third-party Maps, queue (Kafka/SQS).

Flows:

Fare: Rider → /fare → Ride Service ↔ Maps → DB → client.

Request: Rider → /rides → Ride Service → trigger Matching.

Match: Location Service ingests updates → Matching picks nearby → notify driver → driver PATCH accept/deny.

----------------------------------------------------------------------------------------------------------------------------------

## Deep Dive (Quick Hits)

Geo scale & proximity: Redis GEOADD/GEOSEARCH; TTL on locations; persistence/Sentinel for HA.

Reduce update load: adaptive client intervals (speed/direction/status-aware).

Single assignment: Redis distributed lock per driver (TTL≈10s) to serialize requests.

Peak demand durability: enqueue ride requests (Kafka/SQS); process FCFS/priority; commit offsets after match.

Timeouts/retries: durable workflows (Temporal/Step Functions) for 10s timeouts, retries, resume on crash.

Horizontal scale/latency: geo-shard services/queues/DB; read replicas; consistent hashing; boundary scatter-gather only when needed.