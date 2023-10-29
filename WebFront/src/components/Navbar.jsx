import { Link } from 'react-router-dom';
import {useState} from 'react'
import logo from '../assets/logo_fondont.svg'
import close from '../assets/close.svg'
import menu from '../assets/menu.svg'
import { navlinks } from '../constants';
import {layout} from '../styles'

const Navbar = () => {

  // Elemento activo
  const [active, setActive] = useState("Inicio");
  // Mostrar/ocultar elementos
  const [toggle, setToggle] = useState(false);

  return (
    <nav className='w-full flex py-6 justify-between items-center navbar'>
      <a href="#">
        <img src={logo} alt="logo"className="w-[170px] h-[25px]"/>
      </a>
      
      {/* Mostrar los enlaces */}
      <ul className="list-none sm:flex hidden justify-end items-center flex-1">
        {navlinks.map((nav, index) => (
          <li
            key={nav.id}
            className={`font-poppins font-medium cursor-pointer text-[16px] ${
              active === nav.title ? "text-white" : "text-dimWhite"
            } ${index === navlinks.length - 1 ? "mr-0" : "mr-10"}`}
            onClick={() => setActive(nav.title)}
          >
            <a href={`#${nav.id}`}>{nav.title}</a>
          </li>
        ))}
        <Link to="/login">
          <button className={`${layout.buttonLog} font-bold px-4 py-2 text-secondary bg-white ml-3`}>
            Iniciar Sesión
          </button>
        </Link>
      </ul>

      {/* Menu de hamburgesa */}
      <div className="sm:hidden flex flex-1 justify-end items-center">
            <img src={toggle ? close : menu} alt="menu" 
              className='w-[30px] h-[30 px] object-contain mr-2'
              onClick={() => setToggle((prev) => (!prev))}
            />

      <div
          className={`${
            !toggle ? "hidden" : "flex"
          } p-6 bg-orange-500 absolute top-20 right-0 mx-4 my-2 min-w-[140px] rounded-xl sidebar`}
        >
          <ul className="list-none flex justify-end items-start flex-1 flex-col">
            {navlinks.map((nav, index) => (
              <li
                key={nav.id}
                className={`font-poppins font-medium cursor-pointer text-[16px] ${
                  active === nav.title ? "text-white" : "text-dimWhite"
                } ${index === navlinks.length - 1 ? "mb-0" : "mb-4"}`}
                onClick={() => setActive(nav.title)}
              >
                <a href={`#${nav.id}`}>{nav.title}</a>
              </li>
            ))}
            <div>
        <Link to="/login">
          <button className={`${layout.buttonLog} font-semibold text-white`}>
            Iniciar Sesión
          </button>
        </Link>
      </div>
          </ul>
        </div>
      </div>
    </nav>
  );
};

export default Navbar