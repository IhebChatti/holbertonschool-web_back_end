import redis from 'redis';
const client = redis.createClient();
const { promisify } = require("util");
const getAsync = promisify(client.get).bind(client);

client.on("connect", () => {
  console.log("Redis client connected to the server");
});

client.on("error", (error) => {
	console.error(`Redis client not connected to the server: ${error}`);
})

function setNewSchool(schoolName, value) {
  client.set(schoolName, value, function (error, res) {
    redis.print(`Reply: ${res}`);
  });
}

async function displaySchoolValue(schoolName) {
  const value = await getAsync(schoolName);
  console.log(value);
}

(async function main() {
  await displaySchoolValue('Holberton');
  setNewSchool('HolbertonSanFrancisco', '100');
  await displaySchoolValue('HolbertonSanFrancisco');
}());
