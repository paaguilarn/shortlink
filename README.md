[![codecov](https://codecov.io/gh/paaguilarn/shortlink/graph/badge.svg?token=RDOR6BQBZT)](https://codecov.io/gh/paaguilarn/shortlink)

## ShortLink challenge  
  
The ShortLink challenge description can be consulted [here](https://porfin.notion.site/ShortLink-Challenge-76e66a7d62364c819cdf48c2530605c5). The core of the challenge is to create a couple of endpoints:  
1. an endpoint that responds with a short URL given an arbitrary URL,  
2. an endpoint that responds with the original URL given a short URL.  
  
Additional to this, the expectation is that the endpoints can be integrated into a  
distributed architecture.  
  
### Proposal  
A specific proposal requires information that is not provided in the challenge   
description. Additional relevant information could be, for example:  
1. How many URLs the service should transform into short links.  
2. How many read and write operations per unit of time we should be able to handle.  
  
We make a proposal that addresses functional as well as scalability aspects,   
according to assumptions we make with respect to the parameters that have to  
be set in order to have a complete challenge specification.  
  
#### URL transformation  
The URL shortening method is described as follows:
1. Take a URL to shorten.
2. Assign it a sequential integer ID or any bounded integer ID not previously assigned to another URL. This bound is related to the maximum length of the shortened URLs, as we will explain below.
3. Transform the integer ID to base 62. The alphabet for base 62 consists of lowercase and uppercase ASCII letters, as well as digits. The shortened URL is a path parameter in a URL, which is constrained to contain only characters in the aforementioned 62 base alphabet. If we fix the maximum length of short URLs to *n*, the largest integer that can be converted to base 62 with *n* characters is $62^n$.
4. Return the ID in base 62.

#### Endpoints
A couple of endpoints suffice to encode/decode URLs:
```text
POST /urls
```
This endpoint takes an URL, produces a short URL according to the 
algorithm we described above and stores the mapping between both URLs.
```text
GET /{short_url}
```
This endpoint takes a short URL as path parameter and performs a redirection 
to the original URL. 

The complete documentation of these endpoints is provided by the OpenAPI documentation. 
Information about URLs, payloads, responses, headers, and status codes.

#### Events
In order to track both the encoding and decoding of URLs, a simple event system is 
implemented. Each time an URL is encoded or decoded, an event is registered. These 
events are persisted in storage and later used for usage tracking. The generation
and storage of events are performed asynchronously and therefore do not interfere 
with the endpoints latency nor make the endpoints fail. Considering the possibility that
a single event might trigger several processes, in addition to only storing the event log,
we have implemented an additional layer consisting of the observer pattern.

In order to track usage, a query as simple as 
```postgresql
select action, count(id) as usage
from event
where "timestamp" between :timestamp_start and :timestamp_end
group by action;
```
is sufficient, where `timestamp_start` and `timestamp_end` limit the time window over 
which we want measure.

#### Storage
We store our data in a SQL database. We do not consider a KV store because we are
considering an scenario in which the number of encoded URLs grows considerably. 
Assuming an average URL size of 100 ASCII characters, storing 1 billion URLs requires
(1 billion) $\times$ (100 characters) $\times$ (1 byte) = 100 GB.

As event records grow, migrating to a columnar database would provide lower query
times, as well as cost reduction due to data compression.

### Execution
A [makefile](https://github.com/paaguilarn/shortlink/blob/main/Makefile) has been provided
for executing several operations on our project. The most important is
```bash
$ make start
```
for starting the application. Once the application is running, we can navigate 
[here](http://localhost:8080/docs/shortlink) as an 
interface for the endpoints and [here](http://localhost:8080/redoc/shortlink)
for details about the endpoints.
