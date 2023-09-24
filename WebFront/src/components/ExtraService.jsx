import styles, { layout } from "../styles"
import autotanq from "../assets/auto.png"
import shape from "../assets/shape2.svg"

const ExtraService = () => {
  return (
    <section className={`${layout.section}`}>
        <div className={`flex-1 flex  ${styles.flexCenter} md:my-0 my-10 relative`}>
            <img src={autotanq} alt="autorellenador" className="w-[100%] h-[100%] relative z-[5]"/>
            <div className="absolute z-[0] w-[70%] ">
                <img src={shape} alt="forma" />
            </div>
        </div>

        <div className={`${layout.sectionInfo}`}>
            <h2 className={`${styles.heading2} text-secondary mt-1 ml-2`}>
                Conecta con diversos proveedores
            </h2>
            <p className={`${styles.paragraph} text-slate-900 mt-1 ml-4`}>
                Desde la aplicación podrás conectar con diferentes <br className="sm:block hidden"/>
                proveedores de Gas LP para <b className="text-secondary">rellenar tu tanque estacionario</b>
            </p>
        </div>
        
    </section>
  )
}

export default ExtraService