import { createQueue } from "kue";

const queue = createQueue();

const jobName = "push_notification_code";
const jobData = {
  phoneNumber: 123456789,
  message: "Hello World",
};

const job = queue.create(jobName, jobData);
job.save((err) => {
  if (err) console.error("Notification job failed");
  else console.log(`Notification job created: ${job.id}`);
});

job.on("complete", () => {
  console.log("Notification job completed");
});

function sendNotification(phoneNumber, message) {
  console.log(
    `Sending notification to ${phoneNumber}, with message: ${message}`
  );
}

queue.process("push_notification_code", (job, done) => {
  sendNotification(job.data.phoneNumber, job.data.message);
  done();
});
