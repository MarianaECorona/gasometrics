import {useState} from 'react'
import logo from '../assets/logo.svg'
import { navlinks } from '../constants';

const Navbar = () => {
  return (
    <nav className='bg-secondary w-full flex py-6 justify-between items-center navbar'>
      <img src={logo} alt="logo"className="w-[220px] h-[25px]"/>
      <ul className="list-none sm:flex ">

      </ul>
    </nav>
  )
}

export default Navbar