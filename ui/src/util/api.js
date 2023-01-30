// const axios = require("axios")
import axios from "axios";

const baseUrl = `http://${document.location.hostname}:8081/`;

export const getDrives = async () => {
  return await axios.get(`${baseUrl}get_drives`);
};
// async function getDrives() {
//     return await axios.get(`${baseUrl}get_drives`);

// }

export const getDirList = async (path) => {
  return await axios.get(`${baseUrl}list_dir?path=${path}`);
};
// async function getDirList(path) {
//     return await axios.get(`${baseUrl}list_dir?path=${path}`)
// }

// getDrives().then(({data}) => console.log(data))
