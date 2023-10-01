import styles,{layout} from "../../styles"
import {useForm} from "react-hook-form"

function Form  () {
  const {register,handleSubmit, formState:{errors}} = useForm();
  console.log(errors)
  const onSubmit = handleSubmit((data) => {
    console.log(data)
  })
  
  return (
    
    <div className="w-11/12 max-w-[700px] px-10 py-5 rounded-3xl bg-white border-2 border-gray-100">
        <h2 className={`${styles.heading2} text-5x1 text-secondary`}>
          Crear una cuenta
        </h2>
        <p className={`${styles.paragraph} text-slate-700`}>
          Esto tomará poco tiempo
        </p>
        <form onSubmit ={onSubmit}>
          <div className={`${styles.paddingY}`}>
            <div className="flex flex-col">
              {/* nombre */}
              <label htmlFor="name" className={`${layout.labelLog}`}>
                Nombre
              </label>
              <input type={"text"} className={`${layout.inputLog}`}
                {...register("name", {required:true})} 
              />
              {errors.name && <span className="text-red-600">*Campo obligatorio</span> }
            </div>
            
            <div className="flex flex-col mt-2">
              {/* correo */}
              <label htmlFor="email" className={`${layout.labelLog}`}>
                Correo
              </label>
              <input type={"email"} className={`${layout.inputLog}`}
                {...register("email", {required:true})} 
              />
              {errors.email && <span className="text-red-600">*Campo obligatorio</span> }
            </div>
            
            <div className="flex flex-col mt-2">
              {/* contraseña */}
              <label htmlFor="password" className={`${layout.labelLog}`}>
                Contraseña
              </label>
              <input type={"password"} className={`${layout.inputLog}`}
                {...register("email", {required:true})} 
              />
              {errors.password && <span className="text-red-600">*Campo obligatorio</span> }
            </div>
            
            <div className="flex flex-col mt-2">
              {/* conf contraseña */}
              <label htmlFor="password" className={`${layout.labelLog}`}>
                Confirmar contraseña
              </label>
              <input type={"password"} className={`${layout.inputLog}`}
                {...register("email", {required:true})} 
              />
                {errors.password && <span className="text-red-600">*Campo obligatorio</span> }
            </div>

            <div className="mt-2">
              {/* conf contraseña */}
              <input type={"checkbox"} 
                {...register("policy", {required:true})} />
              <label htmlFor="policy" className={`ml-2 font-semibold text-base text-secondary`}>
                Acepto Termirminos y Condiciones de Servicios
              </label>
              {errors.name && <span className="text-red-600"><br/>*Acepte los terminos para continuar</span> }
            </div>
          </div>

          <div className={`mt-1 flex flex-col gap-y-4`}>
            <button type={"submit"} className={`${layout.buttonLog} font-bold text-white bg-secondary`}>
              Registrarse
            </button>
          </div>
        </form>

    </div>
  )
}

export default Form