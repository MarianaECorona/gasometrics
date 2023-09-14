import styles from "../styles"


const Hero = () =>{
    return(
        <div id="home" className={`flex md:flex-row flex-col ${styles.paddingY} `}>
            <div className="flex flex-row justify-between items-center w-full">
                <h1 className="flex-1 font-poppins font-semibold ss:text-[52px] text-[32px] text-white ss:leading-[100.8px] leading-[75px] ml-5">
                    No te quedes sin<br className="sm:block hidden" />{" "}

                    <span className="text-gradient ss:text-[72px] text-[52px]"> El Gas</span>{" "}
                    
                    <p className={`${styles.paragraph} max-w-[400px] text-white mt-5`}>
                    Revisa desde cualquier dispositivo el nivel restante gas 
                    en tu tanque estacionario
                    </p>
                </h1>
            </div>
                {/* Imagen de la portada */}
            <div>
               
            </div>
        </div>
    );
};

export default Hero