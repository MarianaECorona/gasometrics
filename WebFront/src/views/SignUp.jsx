import styles from "../styles"
import Form from "../components/SingUp/Form"

const SignUp = () => {
  return (
    <div className="bg-gradient-to-r from-secondary to-orange-400 flex w-full h-screen">
      <div className={`w-full ${styles.flexCenter}  lg:w-3/3`}>
        <Form/>
      </div>
    </div>
  )
}

export default SignUp