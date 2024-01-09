import logo from './logo.svg';
import './App.css';
import { googleProvider } from './config/authMethod';
import socialAuth from './service/auth';


function App() {

  const handleAuth=async(provider)=>{
    const res=await socialAuth(provider);
    console.log(res);
  }

  return (
    <>
    <button onClick={()=>handleAuth(googleProvider)}>Google</button>
    </>
  );
}

export default App;
