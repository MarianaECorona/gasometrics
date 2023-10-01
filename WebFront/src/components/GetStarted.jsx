import { Link } from 'react-router-dom';
import styles, {layout} from '../styles';

const GetStarted = () => {
  return (
    <section id="get-started">
      <div className={`${styles.flexCenter} ${styles.paddingY}`}>
        <Link to="/login">
          <button className={`${layout.buttonLog} px-16 py-4 font-bold text-2xl text-white bg-secondary`}>
            Comenzar
          </button>
        </Link>
      </div>
    </section>
    
  )
}

export default GetStarted