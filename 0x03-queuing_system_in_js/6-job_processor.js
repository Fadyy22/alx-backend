import { createQueue } from 'kue';


const queue = createQueue({ name: 'push_notification_code' });
const listener = queue.addListener('push_notification_code');

const sendNotification = (phoneNumber, message) => {
  console.log(`Sending notification to ${phoneNumber}, with message: ${message}`);
};
