import styles from './styles'
import Navbar from './components/Navbar'
import Hero from './components/Hero'
import Services from './components/Services'

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
        </div>
      </div>

      <div className={`bg-white ${styles.flexStart}`}>
        <div className={`${styles.boxWidth}`}>
          <Services/>
        </div>
      </div>
    </div>
  )
}

export default App