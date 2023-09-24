import styles from './styles'
import Navbar from './components/Navbar'
import Hero from './components/Hero'
import Services from './components/Services'
import ExtraService from './components/ExtraService'
import Partness from './components/Partness'
import GetStarted from './components/GetStarted'

const App = () => {
  return (
    
    <div className="bg-gradient-to-r from-secondary to-orange-400 w-full overflow-hidden">
      <div className={`${styles.paddingX} ${styles.flexCenter}`}>
        <div className={` ${styles.boxWidth}`}>
          <Navbar />
        </div>   
      </div>

      <div className={`${styles.flexStart}`}>
        <div className={` ${styles.boxWidth}`}>
          <Hero />
          <div className="text-center mt-5 bg-white text-secondary">
          </div>
        </div>
      </div>

      <div className={`bg-white ${styles.flexStart}`}>
        <div className={`${styles.boxWidth}`}>
          <h1 className={`justify-center ${styles.heading1} text-secondary flex mt-5`}>
              Te Ofrecemos
          </h1>
          <Services/>
        </div>
      </div>
      <div className={`bg-white ${styles.flexStart}`}>
        <div className={`${styles.boxWidth}`}>
          <ExtraService/> 
        </div>
      </div>

      <div className={`bg-white ${styles.flexStart}`}>
        <div className={`${styles.boxWidth}`}>
          <h1 className={`justify-center ${styles.heading1} text-secondary flex mt-10`}>
            Nuestros Socios
          </h1>
          <Partness/>
        </div>
      </div> 

      <div className={`${styles.flexStart} bg-white`}>
        <div className={`${styles.boxWidth}`}>
          <GetStarted/>
        </div>
      </div>
    </div>
  )
}

export default App