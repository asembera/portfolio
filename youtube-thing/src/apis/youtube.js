import axios from "axios";

const KEY = "AIzaSyBx8KrHEJ16MqmQ7BNcQa8TKJ6sw-xjI00";

export default axios.create({
  baseURL: "https://www.googleapis.com/youtube/v3",
  params: {
    part: "snippet",
    type: "video",
    maxResults: 5,
    key: KEY,
  },
});
