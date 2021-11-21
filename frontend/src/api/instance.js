import axios from 'axios'

const instance = axios.create({
    baseURL: 'http://0.0.0.0:8000/api/',
    method: 'GET',
    withCredentials: true,
    credentials: "same-origin",
    headers: {
        accept: 'application/json',
    }
})

export default instance