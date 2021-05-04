import axios from "axios";

export default axios.create({
  baseURL: "https://api.unsplash.com",
  headers: {
    Authorization: "Client-ID Um17iqms59G68GvP9L9kBT2V1RRKpRct7kppTOXAaTg",
  },
});
