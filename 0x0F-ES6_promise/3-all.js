import {uploadPhoto, createUser} from 'utils.js';

export default function handleProfileSignup() {
  let body;
  let firstName;
  let lastName;

  return uploadPhoto()
    .then((res) => {
      body = res.body;
      createUser()
        .then((res) => {
          firstName = res.firstName;
          lastName = res.lastName;
          console.log(`${body} ${firstName} ${lastName}`);
        })
        .catch(() => console.log('Signup system offline'));
    })
    .catch(() => console.log('Signup system offline'));
}
