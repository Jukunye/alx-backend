import { createClient } from "redis";

const client = createClient({
  host: "localhost",
  port: 6379,
});

client.on("error", (err) => {
  console.error("Redis client not connected to the server: ", err);
});

client.on("connect", () => {
  console.log("Redis client connected to the server");
});

// Subscribe to a channel
client.on("message", (channel, message) => {
  if (message === "KILL_SERVER") {
    // unsubscribe and quit
    client.unsubscribe("holberton school channel");
    client.quit();
  }
  console.log(message);
});
client.subscribe("holberton school channel");
