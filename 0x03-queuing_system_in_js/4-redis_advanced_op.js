import { createClient, print } from "redis";

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

// key: 'HolbertonSchools'
// value:
//     Portland=50
//     Seattle=80
//     New York=20
//     Bogota=20
//     Cali=40
//     Paris=2
const schoolHashKey = "HolbertonSchools";
const schoolValues = {
  Portland: 50,
  Seattle: 80,
  "New York": 20,
  Bogota: 20,
  Cali: 40,
  Paris: 2,
};

for (let [place, count] of Object.entries(schoolValues)) {
  client.hset(schoolHashKey, place, count, print);
}

client.hgetall(schoolHashKey, (err, object) => {
  if (err) {
    console.error(err);
  } else {
    console.log(object);
  }
});
