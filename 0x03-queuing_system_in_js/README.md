0x03. Queuing System in JS

Resources
Read or watch:

Redis quick start
Redis client interface
Redis client for Node JS
Kue deprecated but still use in the industry
Learning Objectives
At the end of this project, you are expected to be able to explain to anyone, without the help of Google:

How to run a Redis server on your machine
How to run simple operations with the Redis client
How to use a Redis client with Node JS for basic operations
How to store hash values in Redis
How to deal with async operations with Redis
How to use Kue as a queue system
How to build a basic Express app interacting with a Redis server
How to the build a basic Express app interacting with a Redis server and queue
Requirements
All of your code will be compiled/interpreted on Ubuntu 18.04, Node 12.x, and Redis 5.0.7
All of your files should end with a new line
A README.md file, at the root of the folder of the project, is mandatory
Your code should use the js extension
Required Files for the Project
package.json
Click to show/hide file contents
.babelrc
Click to show/hide file contents
and…
Don’t forget to run $ npm install when you have the package.json

Tasks
0. Install a redis instance
mandatory
Download, extract, and compile the latest stable Redis version (higher than 5.0.7 - <https://redis.io/download/>):

$ wget <http://download.redis.io/releases/redis-6.0.10.tar.gz>
$ tar xzf redis-6.0.10.tar.gz
$ cd redis-6.0.10
$ make
Start Redis in the background with src/redis-server
$ src/redis-server &
Make sure that the server is working with a ping src/redis-cli ping
PONG
Using the Redis client again, set the value School for the key Holberton
127.0.0.1:[Port]> set Holberton School
OK
127.0.0.1:[Port]> get Holberton
"School"
Kill the server with the process id of the redis-server (hint: use ps and grep)
$ kill [PID_OF_Redis_Server]
Copy the dump.rdb from the redis-5.0.7 directory into the root of the Queuing project.

Requirements:

Running get Holberton in the client, should return School
Repo:

GitHub repository: alx-backend
Directory: 0x03-queuing_system_in_js
File: README.md, dump.rdb
  
1. Node Redis Client
mandatory
Install node_redis using npm

Using Babel and ES6, write a script named 0-redis_client.js. It should connect to the Redis server running on your machine:

It should log to the console the message Redis client connected to the server when the connection to Redis works correctly
It should log to the console the message Redis client not connected to the server: ERROR_MESSAGE when the connection to Redis does not work
Requirements:

To import the library, you need to use the keyword import
bob@dylan:~$ ps ax | grep redis-server
 2070 pts/1    S+     0:00 grep --color=auto redis-server
bob@dylan:~$
bob@dylan:~$ npm run dev 0-redis_client.js

> queuing_system_in_js@1.0.0 dev /root
> nodemon --exec babel-node --presets @babel/preset-env "0-redis_client.js"

[nodemon] 2.0.4
[nodemon] to restart at any time, enter `rs`
[nodemon] watching path(s): *.*
[nodemon] watching extensions: js,mjs,json
[nodemon] starting `babel-node --presets @babel/preset-env 0-redis_client.js`
Redis client not connected to the server: Error: Redis connection to 127.0.0.1:6379 failed - connect ECONNREFUSED 127.0.0.1:6379
Redis client not connected to the server: Error: Redis connection to 127.0.0.1:6379 failed - connect ECONNREFUSED 127.0.0.1:6379
Redis client not connected to the server: Error: Redis connection to 127.0.0.1:6379 failed - connect ECONNREFUSED 127.0.0.1:6379
^C
bob@dylan:~$
bob@dylan:~$ ./src/redis-server > /dev/null 2>&1 &
[1] 2073
bob@dylan:~$ ps ax | grep redis-server
 2073 pts/0    Sl     0:00 ./src/redis-server *:6379
 2078 pts/1    S+     0:00 grep --color=auto redis-server
bob@dylan:~$
bob@dylan:~$ npm run dev 0-redis_client.js

> queuing_system_in_js@1.0.0 dev /root
> nodemon --exec babel-node --presets @babel/preset-env "0-redis_client.js"

[nodemon] 2.0.4
[nodemon] to restart at any time, enter `rs`
[nodemon] watching path(s): *.*
[nodemon] watching extensions: js,mjs,json
[nodemon] starting `babel-node --presets @babel/preset-env 0-redis_client.js`
Redis client connected to the server
^C
bob@dylan:~$
Repo:

GitHub repository: alx-backend
Directory: 0x03-queuing_system_in_js
File: 0-redis_client.js
  
2. Node Redis client and basic operations
mandatory
In a file 1-redis_op.js, copy the code you previously wrote (0-redis_client.js).

Add two functions:

setNewSchool:
It accepts two arguments schoolName, and value.
It should set in Redis the value for the key schoolName
It should display a confirmation message using redis.print
displaySchoolValue:
It accepts one argument schoolName.
It should log to the console the value for the key passed as argument
At the end of the file, call:

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
Requirements:

Use callbacks for any of the operation, we will look at async operations later
bob@dylan:~$ npm run dev 1-redis_op.js

> queuing_system_in_js@1.0.0 dev /root
> nodemon --exec babel-node --presets @babel/preset-env "1-redis_op.js"

[nodemon] 2.0.4
[nodemon] to restart at any time, enter `rs`
[nodemon] watching path(s): *.*
[nodemon] watching extensions: js,mjs,json
[nodemon] starting `babel-node --presets @babel/preset-env 1-redis_op.js`
Redis client connected to the server
School
Reply: OK
100
^C

bob@dylan:~$
Repo:

GitHub repository: alx-backend
Directory: 0x03-queuing_system_in_js
File: 1-redis_op.js
