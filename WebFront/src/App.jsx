import styles from './styles'
import Navbar from './components/Navbar'
import Hero from './components/Hero'
import Services from './components/Services'

const App = () => {
  return (
    
    <div className="bg-gradient-to-r from-secondary to-orange-400 w-full overflow-hidden">
      <div className={`${styles.paddingX} ${styles.flexCenter}`}>
        <div className={`bg-gradient-to-r from-secondary to-orange-400 ${styles.boxWidth}`}>
          <Navbar />
        </div>   
      </div>

      <div className={`bg-gradient-to-r from-secondary to-orange-400 ${styles.flexStart}`}>
        <div className={`bg-gradient-to-r from-secondary to-orange-400 ${styles.boxWidth}`}>
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