import kue from 'kue';

const jobData = {
		phoneNumber: "",
		message: "",
};

const Q = kue.createQueue();
let job = Q.create('push_notification_code', jobData).save(() => {
	console.log(`Notification job created: ${job.id}`);
})

job.on('complete', () => console.log('Notification job completed'));
job.on('failed', () => console.log('Notification job failed'));
