require("isomorphic-unfetch");
var Redis = require('ioredis')
const { promises: fs } = require("fs");
const path = require("path");

const redisPass = process.env.REDIS_PASS;
const redisHost = process.env.REDIS_HOST;

var redis = new Redis({
    port: 6379,          // Redis port
    host: redisHost,   	 // Redis host
    password: redisPass, // Redis pass
    db: 11,				 // Redis database
});

async function main() {
    const readmeTemplate = (
        await fs.readFile(path.join(process.cwd(), "./README.template.md"))
    ).toString("utf-8");
    
    const name = await redis.hget('current-track', 'Name')
    const artist = await redis.hget('current-track', 'Artist')
    const img = await redis.hget('current-track', 'Image')


    const readme = readmeTemplate
        .replace("{song}", name)
        .replace("{artist}", artist)
        .replace("{img}", img);

    await fs.writeFile("README.md", readme);
}

main();