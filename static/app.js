const baseAPI = "https://api.spotify.com/v1";
const auth = "https://accounts.spotify.com/authorize";

async function getArtist() {
    const response = await axios.get(`${baseAPI}/artists/1wAkNf5IFauLqZgJFY2mAg`);
    console.log(response);
}