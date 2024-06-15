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

function setNewSchool(schooName, value) {
  // set in redis the value for the key schoolName
  client.set(schooName, value, (err, reply) => {
    if (err) {
      console.error(err);
    } else {
      // display a confirmation message using redis.print
      print(reply);
    }
  });
}

function displaySchoolValue(schoolName) {
  // log to the console the value for the key passed as argument
  client.get(schoolName, (err, value) => {
    if (err) {
      console.error(err);
    } else {
      console.log(value);
    }
  });
}

displaySchoolValue("Holberton");
setNewSchool("HolbertonSanFrancisco", "100");
displaySchoolValue("HolbertonSanFrancisco");
