import { Link } from 'react-router-dom';
import styles, {layout} from "../styles"
import img from "../assets/bannerC-hd.png"


const Hero = () =>{
    return(
        <div id="" className={`flex md:flex-row flex-col ${styles.paddingY} `}>
            <div className="flex flex-row justify-between items-center w-full">
                <h1 className="flex-1 font-poppins font-semibold ss:text-[68px] text-[52px] text-white ss:leading-[100.8px] leading-[75px] ml-5">
                    No te quedes sin<br className="sm:block hidden" />{" "}

                    <span className="text-gradient ss:text-[100px] text-[75px]"> El Gas</span>{" "}
                    
                    <p className={`${styles.paragraph} max-w-[400px] text-white mt-5`}>
                    Revisa desde cualquier dispositivo el nivel restante gas 
                    en tu tanque estacionario
                    </p>

                    <div className={`${styles.flexCenter} ${styles.paddingY}`}>
                        <Link to="/login">
                            <button className={`${layout.buttonLog} font-bold px-5 py-4 text-2xl text-secondary bg-slate-200`}>
                                Comenzar
                            </button>
                        </Link>
                    </div>
                    
                </h1>
            </div>
                <img src={img} alt="banner" className="w-[100%] h-[100%] md:w-[50%] md:h-[50%] relative" />
            <div>
                           
            </div>
        </div>
    );
};

export default Hero