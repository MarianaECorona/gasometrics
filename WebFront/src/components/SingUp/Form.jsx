import { Link } from 'react-router-dom';
import {useForm} from "react-hook-form"
import styles,{layout} from "../../styles"

function Form  () {
{ /* funciones para controlar el formulario */}
  const {
    register,
    handleSubmit, 
    formState:{errors}, 
    watch
  } = useForm();

  console.log(errors)

  {/* visualizar que sucede cuando se envia la información */}
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
            <div className={`${layout.formBox}`}>
              {/* nombre */}
              <label htmlFor="name" className={`${layout.labelLog}`}>
                Nombre
              </label>
              <input type={"text"} className={`${layout.inputLog}`}
                {...register("name", {required:{
                    value:true,
                    message:"*Campo obligatorio"
                  },
                  minLength:{
                    value:5,
                    message:"No debe ser menor a 5 caracteres"
                  } 
                })} 
              />
              {errors.name && <span className="text-red-600">{errors.name.message}</span> }
            </div>
            
            <div className={`${layout.formBoxPd}`}>
              {/* correo */}
              <label htmlFor="email" className={`${layout.labelLog}`}>
                Correo
              </label>
              <input type={"email"} className={`${layout.inputLog}`}
                 {...register("email", {required:{
                  value:true,
                  message:"*Campo obligatorio"
                },
                  pattern:{
                    value: /^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$/,
                    message: "Correo no válido"
                  }
              })}
                placeholder="usuario@gasometrics.com" 
              />
              {errors.email && <span className="text-red-600">{errors.email.message}</span> }
            </div>
            
            <div className={`${layout.formBoxPd}`}>
              {/* contraseña */}
              <label htmlFor="password" className={`${layout.labelLog}`}>
                Contraseña
              </label>
              <input type={"password"} className={`${layout.inputLog}`}
                {...register("password", {required:{
                    value:true,
                    message:"*Campo requerido"
                  },
                  minLength:{
                    value:8,
                    message:"Contraseña no menor a 8 caracteres"
                  }
                })} 
              />
              {errors.password && <span className="text-red-600">
                {errors.password.message}
              </span> }
            </div>
            
            <div className={`${layout.formBoxPd}`}>
              {/* conf contraseña */}
              <label htmlFor="validatePassword" className={`${layout.labelLog}`}>
                Confirmar contraseña
              </label>
              <input type={"password"} className={`${layout.inputLog}`}
                {...register("validatePassword", {required:{
                  value:true,
                  message:"*Campo requerido"
                },
                // minLength:{
                //   value:8,
                //   massage:"Contraseña no menor a 8 caracteres"
                // },
                validate: (value) => value === watch ('password') || 'Las contraseña deben ser iguales'
              })} 
              />
                {errors.validatePassword && <span className="text-red-600">
                    {errors.validatePassword.message}
                  </span> }
            </div>

            <div className={`${layout.formBoxPd}`}>
              Direccion
              {/* Dirección */}
              <label htmlFor="street" className={`${layout.labelLog}`}></label>
            </div>

            <div className={`${layout.formBoxPd}`}>
              <label htmlFor="phone_num" className={`${layout.labelLog}`}>
                Telefono
              </label>
              <input type="tel" className={`${layout.inputLog}`}  
                placeholder="3333333333"
                {...register("phone_num", {maxLength:10, minLength:10})}
                />
                {errors.phone_num && <span className="text-red-600">
                    *Deben ser 10 digitos
                  </span> 
                }
            </div>

            <div className="mt-2">
              {/* conf contraseña */}
              <input type={"checkbox"} 
                {...register("policy", {required:true})} />
              <label htmlFor="policy" className={`ml-2 font-semibold text-base text-orange-600`}>
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

          <div className={`${layout.logExtras}`}>
            <div>
              <p className="font-medium text-base">
                Ya tengo una cuenta
                  <Link to="/login">
                    <button className='font-medium text-base ml-2 text-orange-600'>
                      Iniciar sesión
                    </button>
                  </Link>
              </p>
              
            </div>
          </div>
           <pre>
             {JSON.stringify(watch(), null, 2)}
           </pre>
        </form>
    </div>
  )
}

export default Form