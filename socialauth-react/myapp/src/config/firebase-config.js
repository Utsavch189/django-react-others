import { initializeApp } from "firebase/app";
// TODO: Add SDKs for Firebase products that you want to use
// https://firebase.google.com/docs/web/setup#available-libraries

// Your web app's Firebase configuration
const firebaseConfig = {
    apiKey: "AIzaSyDsYYahVK3C4Z1spikN0fCo90U4OJHUw6I",
    authDomain: "myyapp-a7b9a.firebaseapp.com",
    projectId: "myyapp-a7b9a",
    storageBucket: "myyapp-a7b9a.appspot.com",
    messagingSenderId: "45797504349",
    appId: "1:45797504349:web:b27a22d804d1d94d3564b4"
};

// Initialize Firebase
const firebase = initializeApp(firebaseConfig);

export default firebase