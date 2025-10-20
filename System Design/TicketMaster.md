## Non-Functional Requirements

Avail > Consistency for view/search; Consistency first for booking (no double-sell).

Scale: hot events (10M users, 1 event); Reads 100:1 write.

Latency: search <500 ms (cache + search index).

Read-heavy: aggressive caching, horizontal scale, LB.

----------------------------------------------------------------------------------------------------------------------------------

## Core Entities

Event: id, name/desc, type, dates, venueId, performerIds.

Performer: id, name, meta.

Venue: id, address, capacity, seatMap.

Ticket: id, eventId, seat (section/row/seat), price, status.

User: id.

Booking: id, userId, ticketIds[], total, status (in-progress/confirmed).

----------------------------------------------------------------------------------------------------------------------------------

## API Design

View event (+ seat map): GET /events/:eventId -> Event, Venue, Performer[], Ticket[]

Search (paged): GET /events/search?keyword&start&end&pageSize&page -> Event[]

Book (simple start): POST /bookings/:eventId {ticketIds,paymentDetails} -> bookingId

(Evolved) Reserve/confirm split:
POST /bookings/reserve {ticketId} -> bookingId
POST /bookings/:bookingId/confirm {paymentToken} -> Booking

----------------------------------------------------------------------------------------------------------------------------------

## High-Level Design

Clients → API Gateway → Services: Event Service (reads), Search Service, Booking Service.

Data: Events/Performers/Venues in SQL; Tickets & Bookings in PostgreSQL (ACID).

Editor/Seat Map: render from Ticket availability.

Scaling reads: cache (Redis/Memcached), LB, stateless services, CDN for static/seat assets.

----------------------------------------------------------------------------------------------------------------------------------

## Deep Dive (quick hits)

Double-booking prevention: Postgres transactions + row locks/OCC; confirm after payment webhook.

Reserve UX: Redis distributed lock + TTL (e.g., 10 min) on ticketId → holds seat during checkout; release on confirm/expiry.

Hot-event surge: Virtual waiting room (admin-toggled), enqueue users, notify via WebSocket; gate entry to booking page.

Search <500 ms: Elasticsearch (inverted index, fuzzy); CDC from Postgres → ES to stay in sync.

Read scale: cache event/venue/performer blobs (event:{id}), TTLs + invalidation on updates; CDN + query/result caching for frequent searches.