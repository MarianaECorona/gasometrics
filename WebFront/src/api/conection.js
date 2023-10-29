import axios, { Axios } from "axios";

const testApi = axios.create({
    baseURL: 'http://localhost:8080/'
})

export const gettestApi = () =>{
    .then((result) => {
        return testApi.get('/')    
    }).catch((err) => {
        
    });
}