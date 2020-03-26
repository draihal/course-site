import axios from 'axios';
import { catchAxiosError } from './error';


const baseConfig = {
  baseURL: `${process.env.basePath}`
};

const baseConfigWithHeaders = {
  baseURL: `${process.env.basePath}`,
  headers: {
    'accept': 'application/json',
    'Content-Type': 'application/json'
  },
};

export const post = (url, data) => {
  return axios.post(url, data, baseConfig).catch(catchAxiosError);
};

export const get = async (url, config = {}) => {
  const axiosConfig = {
    ...baseConfig,
    ...config,
  };
  return await axios.get(url, axiosConfig).catch(catchAxiosError)
};


