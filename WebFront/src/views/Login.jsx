// import logo from "../assets/logo_fondont.svg"
import Form from "../components/Login/Form"
import styles from "../styles"

const Login = () => {
  return (
   <div className="flex w-full h-screen bg-stone-100">
    <div className={`w-full ${styles.flexCenter}  lg:w-1/2`}>
      <Form/>
    </div>

    <div className="hidden relative w-1/2 h-full lg:flex items-center justify-center bg-gray-200">
        <div className="w-60 h-60 rounded-full bg-gradient-to-tr from-orange-600 to-yellow-500 animate-spin"/> 
        <div className="w-full h-1/2 absolute bottom-0 bg-white/10 backdrop-blur-lg" />
      </div>
   </div>
  )
}

export default Login