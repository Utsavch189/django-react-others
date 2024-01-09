import { getAuth, signInWithPopup } from "firebase/auth";
import firebase from "../config/firebase-config"


const socialAuth = async(provider) => {
    return await signInWithPopup(getAuth(firebase), provider)
        .then((res) => {
            return res.user;
        })
        .catch((err) => {
            return err
        })
}

export default socialAuth