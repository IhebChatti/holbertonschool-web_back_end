import redis from 'redis';

const channel = 'holberton school channel';
const client = redis.createClient();

client.on('ready', () => console.log('Redis client connected to the server'));
client.on('error', (error) => {
  console.log(`Redis client not connected to the server: ${error}`);
});
client.on('message', (channel, message) => {
  console.log(message);
  if (message === 'KILL_SERVER') {
    client.unsubscribe();
    client.quit();
  }
});
client.subscribe(channel);
