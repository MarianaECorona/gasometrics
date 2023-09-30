const styles = {
    boxWidth: "xl:max-w-[1280px] w-full",

    heading1: "font-poppins font-bold xs:text-[65px] text-[45px] xs:leading-[77px] leading-[67px] w-full",  
    heading2: "font-poppins font-semibold xs:text-[45px] text-[35px] xs:leading-[56.8px] leading-[46.8px] w-full",
    paragraph: "font-poppins font-normal text-dimWhite text-[18px] leading-[30.8px]",
  
    flexCenter: "flex justify-center items-center",
    flexStart: "flex justify-center items-start",
  
    paddingX: "sm:px-15 px-5",
    paddingY: "sm:py-15 py-5",
    padding: "sm:px-16 px-6 sm:py-12 py-4",
  
    marginX: "sm:mx-16 mx-6",
    marginY: "sm:my-16 my-6",
  };
  
  export const layout = {
    section: `flex md:flex-row flex-col ${styles.paddingY}`,
    sectionReverse: `flex md:flex-row flex-col-reverse ${styles.paddingY}`,
  
    sectionImgReverse: `flex-1 flex ${styles.flexCenter} md:mr-10 mr-0 md:mt-0 mt-10 relative`,
    sectionImg: `flex-1 flex ${styles.flexCenter} md:ml-10 ml-0 md:mt-0 mt-10 relative`,
  
    sectionInfo: `flex-1 ${styles.flexStart} flex-col`,

    inputLog:`w-full border-2 border-gray-200 rounded-xl p-4 mt-1 bg-transparent`,
    labelLog:`text-lg font-medium`,

    logExtras:`mt-8 flex justify-between items-center`,
    buttonLog:`active:scale-[.98] active:duration-75 transition-all hover:scale-[1.01]  ease-in-out transform py-4 rounded-xl text-lg`,

  };
  
  export default styles;