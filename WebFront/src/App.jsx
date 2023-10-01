import {BrowserRouter, Route, Routes} from 'react-router-dom'
import Index from './Index'
import Login from './views/Login'
import Register from './views/Register'

const App = () => {
  return (
    
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<Index/>}/>
        <Route path="/login" element={<Login/>}/>
        <Route path="/register" element={<Register/>}/>
      </Routes>
    </BrowserRouter>
  
  );
}

export default App