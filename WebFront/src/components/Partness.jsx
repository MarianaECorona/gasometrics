import styles, { layout } from "../styles"
import gas1 from "../assets/gas1.png"
import gas2 from "../assets/gas2.png"
import gas3 from "../assets/gas3.png"


const Partness = () => {
  return (
    <section id="partners" className={`${layout.section} `}>
      <div className={`flex-1 flex ${layout.sectionImg} md:my-0 my-10 relative`}>
        <img src={gas1} alt="logo" className="w-[60%] h-[40%] relative" />
      </div>
      <div className={`flex-1 flex ${layout.sectionImg} md:my-0 my-10 relative`}>
        <img src={gas2} alt="logo" className="w-[50%] h-[90%] relative" />
      </div>
      <div className={`flex-1 flex ${layout.sectionImg} md:my-0 my-10 relative`}>
        <img src={gas3} alt="logo" className="w-[45%] h-[90%] relative" />
      </div>
    </section>
  )
}

export default Partness