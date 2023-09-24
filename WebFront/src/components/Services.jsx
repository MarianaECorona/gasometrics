import styles, { layout } from "../styles"
import tanque from "../assets/tanque.png"
import shape from "../assets/shape1.svg"

const Services = () => {
  return (
    <section id="services" className={`${layout.section}`}>
      <div className={`${layout.sectionInfo}`}>
        <h2 className={`${styles.heading2} text-secondary mt-5 ml-4`}>
          Conoce el nivel restante <br className="sm:block hidden" />
          de gas en tu tanque
        </h2>
        <p className={`${styles.paragraph} text-slate-900 mt-1 ml-4`}>
          Nuestro sistema puede saber con precisión el nivel que resta <br className="sm:block hidden"/> 
          en tu tanque estacionario con <b className={`text-secondary`}>inteligencia artificial</b>
        </p>
      </div>
      <div className={`flex-1 flex ${styles.flexCenter} md:my-0 my-10 relative`} >
        <img src={tanque} alt="tanque estacionario" className="w-[80%] h-[80%] relative z-[5]"/>
        <div className="absolute z-[0] w-[90%] h-[95%]">
          <img src={shape} alt="shape"/>
        </div>
      </div>        
    </section>
  )
}

export default Services