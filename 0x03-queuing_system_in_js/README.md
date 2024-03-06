# Project: 0x03. Queuing System in JS

## Resources

#### Read or watch:

- [Redis quick start](https://intranet.alxswe.com/rltoken/8xeApIhnxgFZkgn54BiIeA)
- [Redis client interface](https://intranet.alxswe.com/rltoken/1rq3ral-3C5O1t67dbGcWg)
- [Redis client for Node JS](https://intranet.alxswe.com/rltoken/mRftfl67BrNvl-RM5JQfUA)
- [Kue](https://intranet.alxswe.com/rltoken/yTC3Ci2IV2US24xJsBfMgQ)

## Learning Objectives

- How to run a Redis server on your machine
- How to run simple operations with the Redis client
- How to use a Redis client with Node JS for basic operations
- How to store hash values in Redis
- How to deal with async operations with Redis
- How to use Kue as a queue system
- How to build a basic Express app interacting with a Redis server
- How to the build a basic Express app interacting with a Redis server and queue

## Tasks

| Task                                                            | File                                                                     |
| --------------------------------------------------------------- | ------------------------------------------------------------------------ |
| 0. Install a redis instance                                     | [README.md](./README.md), [dump.rdb](./dump.rdb)                         |
| 1. Node Redis Client                                            | [0-redis_client.js](./0-redis_client.js)                                 |
| 2. Node Redis client and basic operations                       | [1-redis_op.js](./1-redis_op.js)                                         |
| 3. Node Redis client and async operations                       | [2-redis_op_async.js](./2-redis_op_async.js)                             |
| 4. Node Redis client and advanced operations                    | [4-redis_advanced_op.js](./4-redis_advanced_op.js)                       |
| 5. Node Redis client publisher and subscriber                   | [5-subscriber.js](./5-subscriber.js), [5-publisher.js](./5-publisher.js) |
| 6. Create the Job creator                                       | [6-job_creator.js](./6-job_creator.js)                                   |
| 7. Create the Job processor                                     | [6-job_processor.js](./6-job_processor.js)                               |
| 8. Track progress and errors with Kue: Create the Job creator   | [7-job_creator.js](./7-job_creator.js)                                   |
| 9. Track progress and errors with Kue: Create the Job processor | [7-job_processor.js](./7-job_processor.js)                               |
| 10. Writing the job creation function                           | [8-job.js](./8-job.js)                                                   |
| 11. Writing the test for job creation                           | [8-job.test.js](./8-job.test.js)                                         |
| 12. In stock?                                                   | [9-stock.js](./9-stock.js)                                               |