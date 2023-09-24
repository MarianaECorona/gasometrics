import {BrowserRouter, Route, Routes} from 'react-router-dom'
import Index from './Index'
import Login from './views/Login'

const App = () => {
  return (
    
   
      <BrowserRouter>
        <Routes>
        <Route path="/" element={<Index/>}/>
        <Route path="/login" element={<Login/>}/>
      </Routes>
    </BrowserRouter>
    
  )
}

export default App