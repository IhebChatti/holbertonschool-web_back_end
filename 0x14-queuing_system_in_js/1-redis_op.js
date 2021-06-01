import redis from 'redis';
const client = redis.createClient();

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

function displaySchoolValue(schoolName) {
  client.get(schoolName, function (error, res) {
    console.log(res);
  });
}

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
