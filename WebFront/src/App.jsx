import {BrowserRouter, Route, Routes} from 'react-router-dom'
import Index from './Index'
import Login from './views/Login'
import Register from './views/SignUp'

const App = () => {
  return (
    
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<Index/>}/>
        <Route path="/login" element={<Login/>}/>
        <Route path="/signup" element={<Register/>}/>
      </Routes>
    </BrowserRouter>
  
  );
}

export default App