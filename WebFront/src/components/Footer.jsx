import styles from '../styles'
import logo from '../assets/logo_fondont.svg'

const Footer = () => {
  return (
    <section className={`${styles.flexCenter} ${styles.paddingY} flex-col`}>
        <div className={`${styles.flexStart} md:flex-row flex-col mb-8 w-full`}>
            <div className='flex-[1] flex flex-col justify-start mr-10'>
                <img src={logo} alt="logo" className="w-[170px] h-[25px] object-contain" />
            </div>
        </div>
        <div className="w-full flex justify-between items-center md:flex-row flex-col pt-6 ">
            <p className="font-poppins font-normal text-center text-[15px] leading-[27px] text-white">
                Copyright Ⓒ 2023 Gasometrics. All Rights Reserved.
            </p>
        </div>
    </section>
  )
}

export default Footer